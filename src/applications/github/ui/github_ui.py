from src.applications.github.ui.base_page import BasePage
from selenium.webdriver.common.by import By
from src.applications.github.endpoints import Endpoints


class GitHubUiLoginPage(BasePage):
    """Current class contains Login page elements and methods"""

    def __init__(self, driver, domain: str) -> None:
        super().__init__(driver)
        self.domain = domain

    @property
    def login_field(self):
        return self.find_element(By.ID, "login_field")

    @property
    def password_field(self):
        return self.find_element(By.ID, "password")

    @property
    def submit_button(self):
        return self.find_clikable_button(By.NAME, "commit")

    def navigate_to_login_page(self) -> None:
        self.get_url(self.domain, Endpoints.login)
        self.find_element(By.ID, "login")

    def try_to_login(self, username, password) -> None:
        self.login_field.send_keys(username)
        self.password_field.send_keys(password)

        self.submit_button.click()

    def check_error_message(self) -> None:
        error_message = self.find_element(By.ID, "js-flash-container")

        return error_message.text == "Incorrect username or password."

from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
from src.applications.github.endpoints import Endpoints


class GitHubUiLoginPage:
    """Current class contains Login page elements and methods"""

    def __init__(self, domain: str) -> None:
        self.driver = webdriver.Chrome()
        self.domain = domain

    @property
    def login_field(self):
        return self.driver.find_element(By.ID, "login_field")

    @property
    def password_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def submit_button(self):
        return self.driver.find_element(By.NAME, "commit")

    def navigate_to_login_page(self) -> None:
        self.driver.get(urllib.parse.urljoin(self.domain, Endpoints.login))

    def try_to_login(self, username, password) -> None:
        self.login_field.send_keys(username)
        self.password_field.send_keys(password)

        self.submit_button.click()

    def check_error_message(self) -> None:
        error_message = self.driver.find_element(By.ID, "js-flash-container")

        return error_message.text == "Incorrect username or password."

    def close_browser(self) -> None:
        self.driver.quit()

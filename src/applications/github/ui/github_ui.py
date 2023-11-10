from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
from src.applications.github.endpoints import Endpoints


class GitHubUiLoginPage:
    """Current class contains Login page elements and methods"""

    def __init__(self, domain: str) -> None:
        self.driver = webdriver.Chrome()
        self.domain = domain

    @property
    def login_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        return self.driver.find_element(By.ID, "login_field")

    @property
    def password_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        return self.driver.find_element(By.ID, "password")

    @property
    def submit_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "commit"))
        )
        return self.driver.find_element(By.NAME, "commit")

    def navigate_to_login_page(self) -> None:
        self.driver.get(urllib.parse.urljoin(self.domain, Endpoints.login))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )

    def try_to_login(self, username, password) -> None:
        self.login_field.send_keys(username)
        self.password_field.send_keys(password)

        self.submit_button.click()

    def check_error_message(self) -> None:
        error_message = self.driver.find_element(By.ID, "js-flash-container")
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "js-flash-container"), "Incorrect username or password."
            )
        )

        return error_message.text == "Incorrect username or password."

    def close_browser(self) -> None:
        self.driver.quit()

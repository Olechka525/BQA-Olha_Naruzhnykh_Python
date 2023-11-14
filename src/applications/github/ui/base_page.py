from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, find_by, locator_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((find_by, locator_name))
        )
        return self.driver.find_element(find_by, locator_name)

    def find_clikable_button(self, find_by, locator_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((find_by, locator_name))
        )
        return self.driver.find_element(find_by, locator_name)

    def get_url(self, domain, endpoint):
        return self.driver.get(urllib.parse.urljoin(domain, endpoint))

    def close_browser(self) -> None:
        self.driver.quit()

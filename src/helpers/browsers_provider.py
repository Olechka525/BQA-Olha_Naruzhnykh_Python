from selenium import webdriver


class BrowserProvider:
    """
    Returns the initialized driver for desired browser
    """

    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "ff":
            driver = webdriver.FireFox()

        return driver

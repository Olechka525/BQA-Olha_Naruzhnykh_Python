from selenium import webdriver


class BrowserProvider:
    """
    Returns the initialized driver for desired browser
    """

    @staticmethod
    def get_driver(browser_name, isremote: bool):
        if isremote == True: 
            if browser_name == "chrome":
                options = webdriver.ChromeOptions()
                driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
            elif browser_name == "ff":
                options = webdriver.FirefoxOptions()
                driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
        else :
            if browser_name == "chrome":
                driver = webdriver.Chrome()
            elif browser_name == "ff":
                driver = webdriver.FireFox()
        return driver
 
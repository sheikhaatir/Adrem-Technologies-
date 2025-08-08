from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver():
        # Initialize Chrome WebDriver; can be extended for other browsers
        return webdriver.Chrome()
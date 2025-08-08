import pytest
import allure
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage 

from utils.json_reader import JsonReader

logger = logging.getLogger(__name__)

@allure.feature("E-commerce Checkout")
@allure.story("End-to-End Checkout Flow")
def test_checkout_flow(driver):
    try:
        # Load test data
        with allure.step("Load test data"):
            test_data = JsonReader.read_test_data("test_data.json")

        # Step 1: Login
        with allure.step("Login to the application"):
            login_page = LoginPage(driver)
            driver.get("https://demowebshop.tricentis.com/login")
            logger.info("Navigating to login page")
            login_page.login(test_data['email'], test_data['password'])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            logger.info("Login successful")
            assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed(), "Login failed"
            
    except Exception as e:
        logger.error("Lgin Failed : %s", str(e))
        screenshot_path = f"screenshots/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Login Failed Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
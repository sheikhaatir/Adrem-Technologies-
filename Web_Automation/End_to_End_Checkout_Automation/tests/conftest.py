import pytest
import logging
from selenium import webdriver
from utils.driver_factory import DriverFactory

logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver():
    logger.info("Setting up WebDriver")
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    yield driver
    logger.info("Tearing down WebDriver")
    driver.quit()
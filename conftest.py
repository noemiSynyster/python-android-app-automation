import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.capabilities import DEFAULT_CAPABILITIES

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options().load_capabilities(DEFAULT_CAPABILITIES)
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield driver
    driver.quit()
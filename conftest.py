import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.capabilities import DEFAULT_CAPABILITIES

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# Same "OK" button confirmed via Appium Inspector for the
# "Android App Compatibility" system dialog.
SYSTEM_DIALOG_OK_BUTTON = (AppiumBy.ID, "android:id/button2")


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options().load_capabilities(DEFAULT_CAPABILITIES)
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

    _dismiss_compatibility_dialog_if_present(driver)

    yield driver
    driver.quit()


def _dismiss_compatibility_dialog_if_present(driver, timeout=5):
    """
    Best-effort: on some emulator/API combinations, Android shows a system
    'App Compatibility' warning (16KB page alignment) right after install,
    which can cover the login form. Dismiss it once per session if present.
    """
    try:
        driver.find_element(*SYSTEM_DIALOG_OK_BUTTON).click()
    except (NoSuchElementException, TimeoutException):
        pass
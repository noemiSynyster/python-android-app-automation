from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the Swag Labs login screen.
    Locators obtained via Appium Inspector (accessibility id).
    """

    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    # Fallback locator for the "Android App Compatibility" system dialog,
    # in case it appears and blocks interaction with the login form.
    SYSTEM_DIALOG_OK_BUTTON = (AppiumBy.ID, "android:id/button2")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)
        return self

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        return self

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username, password):
        """Convenience method to perform a full login flow in one call."""
        self.dismiss_system_dialog_if_present(self.SYSTEM_DIALOG_OK_BUTTON, timeout=3)
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()
        return self

    def wait_for_login_success(self, timeout=15):
        """
        Wait until the login screen has actually transitioned away
        (Username field no longer present), instead of checking once
        immediately after tapping LOGIN — avoids false negatives caused
        by the app's transition animation still being in progress.
        """
        self.wait_for_element_to_disappear(self.USERNAME_FIELD, timeout=timeout)
        return self

    def is_login_screen_displayed(self):
        return self.is_displayed(self.USERNAME_FIELD, timeout=10)
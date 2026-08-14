import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

# Sauce Labs / Swag Labs demo credentials, loaded from .env (see .env.example).
# NOTE: password default of "secret_sauce" matches the Sauce Labs demo app family —
# verify against the "tap to autofill" list in the app if login fails.
STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER", "locked_out_user")
PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")


class TestLogin:
    """
    Smoke tests for the Swag Labs login screen.
    Mirrors the structure used in the Toolshop (Selenium) project's test_login.py.
    """

    def test_login_screen_is_displayed_on_launch(self, driver):
        """Sanity check: the app opens directly on the login screen."""
        login_page = LoginPage(driver)
        assert login_page.is_login_screen_displayed(), (
            "Expected the login screen (Username field) to be visible on app launch"
        )

    def test_successful_login_with_standard_user(self, driver):
        """A valid user should be able to log in and leave the login screen."""
        login_page = LoginPage(driver)
        login_page.login(STANDARD_USER, PASSWORD)
        login_page.wait_for_login_success()

    @pytest.mark.skip(
        reason="Error message locator not yet confirmed via Appium Inspector — "
        "verify the element shown for locked_out_user before enabling."
    )
    def test_locked_out_user_cannot_login(self, driver):
        """A locked-out user should see an error and remain on the login screen."""
        login_page = LoginPage(driver)
        login_page.login(LOCKED_OUT_USER, PASSWORD)

        assert login_page.is_login_screen_displayed(), (
            "Expected locked_out_user to remain on the login screen after a failed login"
        )
        # TODO: once the error banner's locator is confirmed in Inspector, add:
        # assert login_page.is_displayed(login_page.ERROR_MESSAGE)
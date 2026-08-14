from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    """
    Base class for all Page Objects.
    Provides common wait/interaction methods shared across pages,
    following the same POM pattern used in the Selenium (Toolshop) project.
    """

    DEFAULT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)

    def find_element(self, locator, timeout=None):
        """Wait for and return a single element located by (AppiumBy, value)."""
        wait = self._get_wait(timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(
                f"Element not found with locator: {locator} after {timeout or self.DEFAULT_TIMEOUT}s"
            )

    def find_elements(self, locator, timeout=None):
        """Wait for and return a list of elements located by (AppiumBy, value)."""
        wait = self._get_wait(timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return []
        return self.driver.find_elements(*locator)

    def click(self, locator, timeout=None):
        """Wait until element is clickable, then tap/click it."""
        wait = self._get_wait(timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def send_keys(self, locator, text, timeout=None, clear_first=True):
        """Wait for element, optionally clear it, then type text into it."""
        element = self.find_element(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator, timeout=None):
        """Return the visible text of an element."""
        return self.find_element(locator, timeout).text

    def is_displayed(self, locator, timeout=5):
        """Return True/False without raising, useful for conditional checks."""
        try:
            return self.find_element(locator, timeout).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """Wait until an element is no longer present (e.g. a loading spinner or dialog)."""
        wait = self._get_wait(timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    def dismiss_system_dialog_if_present(self, ok_button_locator, timeout=3):
        """
        Best-effort dismissal of unexpected system/app dialogs (e.g. the
        'Android App Compatibility' warning) so they don't block a test.
        Silently does nothing if the dialog isn't present.
        """
        if self.is_displayed(ok_button_locator, timeout=timeout):
            self.click(ok_button_locator, timeout=timeout)

    def scroll_to_element(self, text, timeout=None):
        """
        Scroll an Android list/view until an element with the given visible
        text is found, using UiAutomator2's UiScrollable helper.
        """
        locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().textContains("{text}"))'
        )
        return self.find_element(locator, timeout)

    def _get_wait(self, timeout=None):
        if timeout is None:
            return self.wait
        return WebDriverWait(self.driver, timeout)
import os

# src/config/capabilities.py -> project root is three levels up
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APK_PATH = os.path.join(PROJECT_ROOT, "apps", "Android.SauceLabs.Mobile.Sample.app.2.7.1.apk")

DEFAULT_CAPABILITIES = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:app": APK_PATH,
    "appium:appPackage": "com.swaglabsmobileapp",
    "appium:appWaitActivity": "*",
    "appium:noReset": False,
    "appium:newCommandTimeout": 3600,
}
import os

APK_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apps", "Android.SauceLabs.Mobile.Sample.app.2.7.1.apk")

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
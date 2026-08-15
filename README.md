# Mobile Automation Framework — Python + Appium + pytest

Mobile UI automation framework for the [Sauce Labs Sample App](https://github.com/saucelabs/sample-app-mobile)
(Swag Labs), built with Python, Appium, and pytest, following the Page Object Model
design pattern and targeting Android via UiAutomator2.

This is the second project in a portfolio designed to demonstrate automation
fundamentals across different tech stacks:

1. Python + Selenium — web automation ([Toolshop demo site](https://practicesoftwaretesting.com))
2. **Python + Appium (this project)** — native mobile automation

## Overview

This project demonstrates a mobile QA automation workflow: environment setup for Android
emulation, element inspection via Appium Inspector, Page Object implementation, and test
execution with pytest — applied to a real e-commerce-style native app.

- **UI testing**: login flow, including successful login and locked-out user error handling
- **Design pattern**: Page Object Model
- **Target platform**: Android (emulator)

## Tech stack

| Category | Tool |
|---|---|
| Language | Python 3.9 |
| Test framework | pytest |
| Mobile automation | Appium Server 2.x + UiAutomator2 driver |
| Environment management | python-dotenv, venv |
| Element inspection | Appium Inspector |

## Project structure

```
python-android-app-automation/
├── apps/                    # APK under test (not committed — see Setup below)
├── src/
│   ├── config/
│   │   └── capabilities.py  # Appium/UiAutomator2 desired capabilities
│   └── pages/
│       ├── base_page.py     # Shared wait/interaction methods for all pages
│       └── login_page.py    # Login screen Page Object
├── tests/
│   └── test_login.py        # Login test suite
├── docs/
│   ├── requirements.md
│   ├── test_cases.md
│   ├── ARCHITECTURE.md
│   └── ISSUES_AND_SOLUTIONS.md
├── conftest.py                # Pytest fixtures (driver setup/teardown)
├── pytest.ini
├── requirements.txt
├── .env.example
└── LICENSE
```

## Architecture

Design decisions (Page Object Model, locator strategy, fixtures, handling of async UI
transitions) are documented in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Getting started

### Prerequisites
- macOS (Apple Silicon) — this guide targets that setup specifically
- Homebrew
- Android Studio (provides the SDK, `adb`, and the emulator)

### 1. Install the JDK
```bash
brew install openjdk@17
sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
echo 'export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v17)' >> ~/.zshrc
source ~/.zshrc
```

### 2. Install Android Studio and configure the SDK
Download from [developer.android.com/studio](https://developer.android.com/studio), run
the Standard setup, then confirm your SDK path from **Settings > Languages & Frameworks
> Android SDK** and add it to your shell:
```bash
echo 'export ANDROID_HOME=$HOME/Library/Android/sdk' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator' >> ~/.zshrc
source ~/.zshrc
```

### 3. Create an emulator
Inside Android Studio: **More Actions > Virtual Device Manager > Create Device**. A Pixel
device with a recent Android system image (API 33/34, Google APIs) works well.

### 4. Install Node.js, Appium, and the UiAutomator2 driver
```bash
brew install node
npm install -g appium
appium driver install uiautomator2
```

### 5. Install Appium Inspector
Download the `.dmg` for your architecture from the
[Appium Inspector releases page](https://github.com/appium/appium-inspector/releases).

### 6. Clone the repo and set up the Python environment
```bash
git clone https://github.com/noemiSynyster/python-android-app-automation.git
cd python-android-app-automation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 7. Environment variables
```bash
cp .env.example .env
```
The default values already work with the sample app's demo accounts.

### 8. Download the app under test
This project automates the [Sauce Labs Sample App](https://github.com/saucelabs/sample-app-mobile),
version 2.7.1. The APK is **not committed to this repo** — download it from the
[releases page](https://github.com/saucelabs/sample-app-mobile/releases/tag/2.7.1) and
place it under `apps/`:
```
apps/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk
```

## Running the tests

With the emulator open and Appium running in a separate terminal (`appium`):
```bash
pytest tests/ -v
```

## What's covered so far

- Login flow: successful login, locked-out user error handling
- Handling of native Android system dialogs
- Handling of async UI transitions (React Native screen animations)

## Test documentation

- [Functional requirements](docs/requirements.md)
- [Test cases](docs/test_cases.md)

## Roadmap

- [ ] Products / catalog page object and tests
- [ ] Cart and checkout flow
- [ ] CI/CD pipeline (GitHub Actions + Android emulator runner)
- [ ] Allure reporting

## Issues resolved during development

Real problems encountered and how they were solved are documented transparently in
[`docs/ISSUES_AND_SOLUTIONS.md`](docs/ISSUES_AND_SOLUTIONS.md) — including a wrong
assumed app package, a native system dialog blocking sessions, an empty-text element,
and a false test failure caused by animation timing.
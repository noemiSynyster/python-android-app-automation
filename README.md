# Mobile Automation Framework — Python + Appium

A mobile UI automation framework built with **Python**, **Appium**, **pytest**, and
**UiAutomator2**, targeting **Android** apps. This is the third project in a
three-part portfolio designed to demonstrate automation fundamentals across different
tech stacks:

1. [Python + Selenium](#) — web automation ([Toolshop demo site](https://practicesoftwaretesting.com))
2. TypeScript + Playwright — web automation
3. **Python + Appium (this project)** — native mobile automation

## Tech stack

- **Language:** Python 3.9
- **Automation engine:** Appium Server 2.x + UiAutomator2 driver
- **Test runner:** pytest
- **Design pattern:** Page Object Model (POM)
- **Target app:** [Sauce Labs Sample App](https://github.com/saucelabs/sample-app-mobile) (Android, v2.7.1)
- **Environment:** Android Emulator (macOS, Apple Silicon)
- **Config management:** `python-dotenv` for credentials

## Project structure

```
├── apps/               # APK under test (not committed — see docs/SETUP.md)
├── src/
│   ├── config/          # Appium capabilities
│   └── pages/           # Page Object classes
├── tests/               # Test suites
├── docs/                # Setup, architecture, and issue documentation
├── conftest.py           # Pytest fixtures
├── pytest.ini
├── requirements.txt
├── .env.example
└── LICENSE
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for design details.

## Getting started

Full setup instructions (Homebrew, JDK, Android SDK, emulator, Appium, Python env) are in
[`docs/SETUP.md`](docs/SETUP.md).

Quick start once everything is installed:
```bash
source venv/bin/activate
appium &                          # in one terminal, keep it running
pytest tests/ -v
```

## What's covered so far

- Login flow: successful login, locked-out user error handling
- Handling of native Android system dialogs
- Handling of async UI transitions (React Native screen animations)

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
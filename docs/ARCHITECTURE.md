# Architecture

This framework follows the same Page Object Model (POM) approach used in the
[Selenium/Toolshop portfolio project](https://github.com/noemiSynyster/python-website-automation),
adapted for mobile with Appium.

## Project structure

```
python-android-app-automation/
├── apps/                    # APK under test (git-ignored, see README)
├── src/
│   ├── config/
│   │   └── capabilities.py  # Appium/UiAutomator2 desired capabilities
│   └── pages/
│       ├── base_page.py     # Shared wait/interaction methods for all pages
│       └── login_page.py    # Login screen Page Object
├── tests/
│   └── test_login.py        # Login test suite
├── conftest.py                # Pytest fixtures (driver setup/teardown)
├── pytest.ini
├── requirements.txt
├── .env.example
└── docs/
```

Imports follow the same `src/` convention used in the Selenium project (e.g.
`from src.pages.login_page import LoginPage`).

## Design decisions

### Page Object Model
Every screen is represented by a class inheriting from `BasePage`. Locators are declared
as class attributes (tuples of `(AppiumBy, value)`), and each page exposes intent-revealing
methods (`login()`, `enter_username()`, etc.) rather than exposing raw Appium calls to the
tests. This mirrors the pattern used in the Selenium project, swapping Selenium's `By` for
Appium's `AppiumBy`.

### Locator strategy
Locators are pulled directly from the app via **Appium Inspector**, preferring, in order:
1. `accessibility id` — most stable, doesn't depend on tree structure or wording
2. Structural `xpath` (parent/child relationship) — used when no accessibility id exists
   on the specific element (e.g. text nested inside a container)
3. `resource-id` — used for native Android system dialogs (permissions, compatibility
   warnings), which expose generic Android SDK IDs rather than app-specific ones

Exact-text xpath is avoided where possible, since UI copy can change independently of
element structure.

### Fixtures (`conftest.py`)
A single `driver` fixture (function-scoped) creates a new Appium session per test and
tears it down afterward. `noReset` is kept as `False` so each test starts from a clean
app install — slower, but avoids state leaking between tests (saved sessions, cart
contents, etc.).

The fixture also handles dismissing the Android "App Compatibility" system dialog that
can appear after a fresh install, so individual tests don't need to worry about it unless
they specifically need to.

### Handling asynchronous UI transitions
Since the app under test is built with React Native, screen transitions involve animation
time that a single immediate assertion can miss. Rather than checking screen state once,
page methods like `wait_for_login_success()` poll (via `WebDriverWait`) until the expected
state is reached, up to a timeout — see `docs/ISSUES_AND_SOLUTIONS.md` for the specific
issue this solved.

### Credentials
Test credentials are loaded from environment variables via `python-dotenv` (see
`.env.example`), rather than hardcoded in test files — consistent with how secrets are
handled in the Selenium project.
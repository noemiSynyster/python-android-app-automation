# Functional Requirements — Swag Labs Mobile Sample App

## Scope
This document describes the functional requirements covered (or planned) by the mobile
automation suite in this project, for the
[Sauce Labs Sample App](https://github.com/saucelabs/sample-app-mobile) ("Swag Labs"),
an Android native e-commerce demo application, automated via Appium.

## Modules covered

### 1. Authentication
- FR-01: A user must be able to log in with a valid username and password.
- FR-02: The system must reject login for a locked-out account and display an
  explanatory error message.
- FR-03: The login screen must remain displayed after a failed login attempt.
- FR-04: The app must open directly on the login screen on a fresh launch.

### 2. Product catalog (planned)
- FR-05: The system must list available products after a successful login.
- FR-06: Each product must display name, price, and image.
- FR-07: A user must be able to open a product's detail screen.

### 3. Shopping cart (planned)
- FR-08: A user must be able to add one or more products to the cart.
- FR-09: A user must be able to remove a product from the cart.
- FR-10: The cart icon must reflect the current number of items.

### 4. Checkout (planned)
- FR-11: A user must be able to complete checkout with valid shipping information.
- FR-12: The system must validate required fields before allowing progress.

## Out of scope
- iOS (this project targets Android only, via UiAutomator2).
- Native device features not related to the shopping flow: biometrics (Touch/Face ID),
  geolocation, QR code scanner, and the drawing/"Sauce Bolt" feature.
- Real payments (the app is a demo and does not process real payments).
- Load or performance testing.
- Security testing (penetration testing).

## Status
As of this writing, only the **Authentication** module (FR-01 to FR-04) has automated
coverage — see [`test_cases.md`](test_cases.md) for current test status. The remaining
modules are documented here to guide upcoming work (see the Roadmap in the main
[README](../README.md)).
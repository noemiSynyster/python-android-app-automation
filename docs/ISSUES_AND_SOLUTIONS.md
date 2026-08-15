# Issues & Solutions

Documenting real problems encountered while building this framework, and how they were
resolved — in the same spirit of transparency as the Selenium/Toolshop project's
documented CI and routing issues.

## 1. Wrong `appPackage` assumed from documentation

**Problem:** initial capabilities were configured with a guessed `appPackage`
(`com.saucelabs.mydemoapp.rn`) based on general Sauce Labs demo app naming conventions.
Appium Inspector failed to start a session, raising a `WebDriverError` referencing a
different, unexpected activity.

**Solution:** the actual package name (`com.swaglabsmobileapp`) was confirmed directly
from the Appium Inspector session error message and the "Currently Active App ID" field
in Session Information, rather than relying on assumed values. Lesson: always confirm
`appPackage`/`appActivity` empirically via Inspector rather than from generic examples.

## 2. Android "App Compatibility" system dialog blocking sessions

**Problem:** because `noReset` is `False`, the app reinstalls on every test session. Some
emulator/API level combinations trigger a native Android dialog ("This app isn't 16 KB
compatible...") on first launch after install, which covers the login form and causes
Appium to time out waiting for the expected activity.

**Solution:** rather than handling this per-test, the `driver` fixture in `conftest.py`
performs a best-effort dismissal of the dialog (via its generic Android `resource-id`,
`android:id/button2`) immediately after creating the session, wrapped in a try/except so
it's a no-op when the dialog doesn't appear.

## 3. Error message element returning empty text

**Problem:** the "locked out" error banner's container (identified via its
`accessibility id`, `test-Error message`) returned an empty string from `.text`, causing
assertions on the error message content to fail even though the element was correctly
located and visibly displayed on screen.

**Root cause:** the container is a non-text `ViewGroup`; the actual message lives in a
child `TextView` with no accessibility id of its own.

**Solution:** added a second, structural locator (`ERROR_MESSAGE_TEXT`) using a relative
xpath that targets the `TextView` child of the known container, instead of depending on
the container's own (empty) text attribute, or on the exact wording of the message.

## 4. False negative on login success due to transition timing

**Problem:** `test_successful_login_with_standard_user` failed intermittently even when
login visibly succeeded on the emulator — the assertion checking that the login screen
had disappeared ran before the app's transition animation had completed.

**Solution:** replaced the one-shot `is_displayed()` check with
`wait_for_login_success()`, which uses `WebDriverWait` with `invisibility_of_element_located`
to actively poll (up to 15s) until the login screen's Username field is gone, instead of
checking once immediately after the tap.
# Test Cases

Format: ID | Requirement | Description | Precondition | Expected result | Type

## Authentication

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-MOB-01 | FR-04 | App opens directly on the login screen | Fresh app launch | Username field is visible | Automated |
| TC-MOB-02 | FR-01 | Log in with valid credentials (`standard_user`) | App is on the login screen | Login screen is dismissed; user reaches the next screen | Automated |
| TC-MOB-03 | FR-02, FR-03 | Log in with a locked-out account (`locked_out_user`) | App is on the login screen | Error message "Sorry, this user has been locked out." is displayed; user remains on the login screen | Automated |

## Product catalog (planned)

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-MOB-04 | FR-05 | Product list loads after login | User is logged in | At least one product is visible | Planned |
| TC-MOB-05 | FR-07 | Opening a product shows its detail screen | User is on the product list | Product name, price, and description are visible | Planned |

## Shopping cart (planned)

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-MOB-06 | FR-08 | Add a product to the cart | User is on the product list | Cart icon count increases by 1 | Planned |
| TC-MOB-07 | FR-09 | Remove a product from the cart | At least one product in the cart | Cart icon count decreases by 1 | Planned |

## Checkout (planned)

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-MOB-08 | FR-11 | Complete checkout with valid shipping info | At least one product in the cart | Order confirmation is displayed | Planned |
| TC-MOB-09 | FR-12 | Attempt checkout with a required field empty | At least one product in the cart | Validation error is shown; checkout is blocked | Planned |
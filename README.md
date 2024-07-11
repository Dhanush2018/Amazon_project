Amazon Automation Tests

This repository contains automated tests for Amazon using Selenium and Python.

Project Structure:

1. pages/base.py: Contains the BaseClass that provides common methods for interacting with web elements using Selenium WebDriver.
2. pages/amazon_page.py: Defines the AmazonPage class that inherits from BaseClass and contains page-specific methods and locators for interacting with        elements on the Amazon website.
3. test_cases/config.py: Configuration file containing constants like URL, user credentials, and product information used in the tests.
4. test_cases/conftest.py: Contains fixtures and helper functions used across multiple test files.
5. tests/test_login.py: Test suite for testing the login functionality on Amazon.
6. tests/test_add_to_cart.py: Test suite for testing adding products to the cart on Amazon.
7. tests/test_invalid_user.py: Test suite for testing login with invalid credentials on Amazon.
8. tests/test_multi_products.py: Test suite for testing adding multiple products to the cart on Amazon.

Prerequisites:

Python 3.12.3
Selenium WebDriver
pytest

Clone the repository:

git clone <repository_url>
cd amazon-automation
Install dependencies:

pip install -r requirements.txt

Update USER_EMAIL and USER_PASSWORD in config.py with your Amazon credentials.
Running Tests
Run all tests:

pytest:
Run tests for a specific file:

pytest tests/test_login.py
Run tests in parallel (if supported by pytest-xdist):

pytest -n auto
Notes
Screenshots are captured and saved in case of test failures.

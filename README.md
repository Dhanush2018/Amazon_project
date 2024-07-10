
Amazon Automation Tests
This repository contains automated tests for Amazon using Selenium and Python.

Project Structure
pages/base.py: Contains the BaseClass that provides common methods for interacting with web elements using Selenium WebDriver.
pages/amazon_page.py: Defines the AmazonPage class that inherits from BaseClass and contains page-specific methods and locators for interacting with elements on the Amazon website.
test_cases/config.py: Configuration file containing constants like URL, user credentials, and product information used in the tests.
test_cases/conftest.py: Contains fixtures and helper functions used across multiple test files.
tests/test_login.py: Test suite for testing the login functionality on Amazon.
tests/test_add_to_cart.py: Test suite for testing adding products to the cart on Amazon.
tests/test_invalid_user.py: Test suite for testing login with invalid credentials on Amazon.
tests/test_multi_products.py: Test suite for testing adding multiple products to the cart on Amazon.
Prerequisites
Python 3.x
Selenium WebDriver
pytest
ChromeDriver / GeckoDriver (for respective browsers)
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository_url>
cd amazon-automation
Install dependencies:

Copy code
pip install -r requirements.txt
Set up WebDriver:

Download the appropriate WebDriver for your browser (Chrome, Firefox, etc.) and place it in your PATH.
Update configuration:

Update USER_EMAIL and USER_PASSWORD in config.py with your Amazon credentials.
Running Tests
Run all tests:

Copy code
pytest
Run tests for a specific file:

bash
Copy code
pytest tests/test_login.py
Run tests in parallel (if supported by pytest-xdist):

arduino
Copy code
pytest -n auto
Notes
Screenshots are captured and saved in case of test failures.

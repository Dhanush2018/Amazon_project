import pytest
from test_cases.config import URL, user_email, invalid_password
from pages.base import BaseClass
from pages.amazon_page import AmazonPage
from test_cases.conftest import _capture_screenshot

@pytest.mark.usefixtures("driver")
def test_invalid_user(driver):
    BaseClass(driver)

    # Navigate to the Amazon login page
    driver.get(URL)

    log = BaseClass.getLogger()

    # Create an instance of AmazonLoginPage
    amazon_page = AmazonPage(driver)

    log.info("Invalid Login Page Script started...")
    amazon_page.click_login_button_on_header()

    # Call the do_login function on the instance
    amazon_page.do_login(user_email, invalid_password)

    try:
        # Assertion
        assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More" in driver.title
    except AssertionError:
        # Capture screenshot on assertion failure
        _capture_screenshot(driver, "invalid_user.png")
        raise

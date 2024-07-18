import time
import pytest
from test_cases.config import URL, PRODUCT, user_email, user_password
from pages.base import BaseClass
from pages.amazon_page import AmazonPage
from test_cases.conftest import _capture_screenshot

@pytest.mark.usefixtures("driver")
def test_customer_reviews(driver):

    base_instance = BaseClass(driver)

    # Navigate to the Amazon login page
    driver.get(URL)

    # Create instances of page objects
    amazon_page = AmazonPage(driver)

    # Perform login
    amazon_page.click_login_button_on_header()
    amazon_page.do_login(user_email, user_password)

    # Search for the product
    amazon_page.enter_product_on_search_field(PRODUCT)
    amazon_page.click_on_search_button()

    # Clicking on product
    amazon_page.click_on_product()

    driver.switch_to.window(driver.window_handles[1])

    print(amazon_page.get_customer_ratings_element())

    try:
        # Assertion
        assert "Apple iPhone 15 Pro Max (256 GB) - Black Titanium : Amazon.in: Electronics" in driver.title
    except AssertionError:
        # Capture screenshot on assertion failure
        _capture_screenshot(driver, "invalid_page.png")
        raise
import pytest
from test_cases.config import URL, PRODUCT, USER_EMAIL, USER_PASSWORD
from pages.base import BaseClass
from pages.amazon_page import AmazonPage
from test_cases.conftest import _capture_screenshot

@pytest.mark.usefixtures("driver")
def test_add_to_cart(driver):
    BaseClass(driver)

    # Navigate to the Amazon login page
    driver.get(URL)

    # Create instances of page objects
    amazon_page = AmazonPage(driver)

    # Perform login
    amazon_page.click_login_button_on_header()
    amazon_page.do_login(USER_EMAIL, USER_PASSWORD)

    # Search for the product
    amazon_page.enter_product_on_search_field(PRODUCT)
    amazon_page.click_on_search_button()

    # Add product to cart
    amazon_page.click_product_add_to_cart()

    # Click on cart icon
    amazon_page.click_on_cart()

    # Click on delete button (example, adjust as per your actual test flow)
    amazon_page.click_delete_product_from_cart()

    try:
        # Assertion
        assert "Amazon.in Shopping Cart" in driver.title
    except AssertionError:
        # Capture screenshot on assertion failure
        _capture_screenshot(driver, "invalid_user.png")
        raise

import time
import pytest
from test_cases.config import URL, PRODUCTS, USER_EMAIL, USER_PASSWORD
from pages.base import BaseClass
from pages.amazon_page import AmazonPage

@pytest.mark.usefixtures("driver")
def test_multi_products(driver):
    BaseClass(driver)

    # Navigate to the Amazon login page
    driver.get(URL)

    # Create instances of page objects
    amazon_page = AmazonPage(driver)

    # Perform login
    amazon_page.click_login_button_on_header()
    amazon_page.do_login(USER_EMAIL, USER_PASSWORD)

    # Loop through each product
    for product in PRODUCTS:
        # Search for the product
        amazon_page.enter_product_on_search_field(product)
        amazon_page.click_on_search_button()

        # Add product to cart
        amazon_page.click_product_add_to_cart()

        time.sleep(3)

        # Optionally, navigate to cart
        amazon_page.click_on_cart()

    amazon_page.get_all_products_price()
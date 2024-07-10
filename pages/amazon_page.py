from pages.base import BaseClass
from selenium.webdriver.common.by import By
from test_cases.config import PRODUCTS

class AmazonPage(BaseClass):
    # Login Locators
    email_text_field = (By.XPATH, "//input[@class = 'a-input-text']")
    continue_button = (By.ID, 'continue')
    password_text_field = (By.ID, 'ap_password')
    sign_in_button = (By.ID, 'signInSubmit')

    # Function to perform login with provided email and password
    def do_login(self, email, password):
        self.send_keys(self.email_text_field, email)
        self.do_click(self.continue_button)
        self.send_keys(self.password_text_field, password)
        self.do_click(self.sign_in_button)

    # HomePage Locators
    login_button = (By.CSS_SELECTOR, "#nav-link-accountList")
    search_field = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")
    cart_button = (By.ID, "nav-cart-count")
    add_to_cart_button = (By.ID, "add-to-cart-button")
    added_to_cart_confirmation = (By.CSS_SELECTOR, "#huc-v2-order-row-messages span")

    # Click the login button on the header
    def click_login_button_on_header(self):
        self.do_click(self.login_button)

    # Clear the search field
    def clear_search_field(self):
        self.clear(self.search_field)

    # Enter product name on the search field
    def enter_product_on_search_field(self, product_name):
        self.send_keys(self.search_field, product_name)

    # Click on the search button
    def click_on_search_button(self):
        self.do_click(self.search_button)

    # Click on the cart button
    def click_on_cart(self):
        self.do_click(self.cart_button)

    # Add a product to the cart
    def add_product_to_cart(self):
        self.do_click(self.add_to_cart_button)

    # Get confirmation text after adding to cart
    def get_added_to_cart_confirmation(self):
        return self.get_element_text(self.added_to_cart_confirmation)

    # CartPage Locators
    product_locator = (By.XPATH, "(//button[text() = 'Add to cart'])[1]")
    delete_product_from_cart_locator = (By.XPATH, "//input[@class = 'a-color-link'][1]")

    # Fuction to click on the product (add to cart button)
    def click_product_add_to_cart(self):
        self.do_click(self.product_locator)

    # Fuction to delete a product from cart
    def click_delete_product_from_cart(self):
        self.do_click(self.delete_product_from_cart_locator)

    # Function that calculates the total price of items in the cart by summing the prices of each product, and then checks if this total matches with sub total.
    def get_all_products_price(self):
        total_price = 0
        prices = []
        for i in range(len(PRODUCTS)):
            price_path = f"(//span[@class = 'a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold'])[{i + 1}]"
            price_element = self.find_element_1(By.XPATH, price_path)
            price_text = price_element.text.strip().replace(',', '').replace('₹', '')  # Clean up the price text
            price_value = float(price_text)  # Convert to float
            total_price += price_value
            prices.append(price_text)
            print(price_element.text.strip())

        # Get the subtotal element
        subtotal_path = "(//span[@class = 'a-size-medium a-color-base sc-price sc-white-space-nowrap'])[2]"
        subtotal_element = self.find_element_1(By.XPATH,subtotal_path)
        subtotal_text = subtotal_element.text.strip().replace(',', '').replace('₹', '')  # Clean up the subtotal text
        subtotal_value = float(subtotal_text)  # Convert to float

        print("Total Price:", total_price)
        print("Subtotal:", subtotal_value)

        # Assertion: Compare total_price with subtotal_value
        assert total_price == subtotal_value, f"Total price ({total_price}) does not match Subtotal ({subtotal_value})"

        return total_price, prices
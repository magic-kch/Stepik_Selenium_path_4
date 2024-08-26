from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_product_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product.text
        assert product_name == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Product name is incorrect"

    def should_be_product_price(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product.text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price is incorrect {} != {}".format(product_price, basket_price)
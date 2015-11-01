__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from base_page_object import BasePage

class ShoppingCartSummaryPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "unit_price":(By.CLASS_NAME,"special-price"),
        "total_price":(By.ID,"total_price"),
        "proceed_to_checkout":(By.LINK_TEXT,"Proceed to checkout")
    }




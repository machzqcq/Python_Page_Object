__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from base_page_object import BasePage

class SummerDressesCatalogPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "category_name":(By.CLASS_NAME,"cat-name"),
        "size_short":(By.ID,"layered_id_attribute_group_1"),
        "size_medium":(By.ID,"layered_id_attribute_group_2"),
        "color_white":(By.ID,"layered_id_attribute_group_8")
    }

    class PrintedSummerDress1(BasePage):
        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url='http://www.automationpractice.com')

        locator_dictionary = {
            "img_dress1":(By.XPATH,"//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img"),
            "add_cart_dress1":(By.XPATH,"//*[@id='center_column']/ul/li[1]/div/div[2]/div[2]/a[1]"),
            "product_price":(By.CLASS_NAME,"product-price")
                            }
        class CartPopup(BasePage):
            def __init__(self, context):
                BasePage.__init__(
                    self,
                    context.browser,
                    base_url='http://www.automationpractice.com')

            locator_dictionary = {
                "continue_shopping":(By.XPATH,"//*[@title='Continue shopping']"),
                "proceed_to_checkout":(By.XPATH,"//*[@title='Proceed to checkout']")
                                }

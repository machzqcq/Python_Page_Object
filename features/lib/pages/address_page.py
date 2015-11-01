__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from base_page_object import BasePage

class AddressPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "page_heading": (By.CLASS_NAME, 'page-heading'),
        "firstname": (By.ID, 'firstname'),
        "lastname": (By.ID, 'lastname'),
        "address1": (By.ID, 'address1'),
        "city": (By.ID, 'city'),
        "state": (By.ID, 'id_state'),
        "country": (By.ID, 'id_country'),
        "post_code": (By.ID, 'postcode'),
        "home_phone": (By.ID, 'phone'),
        "mobile_phone": (By.ID, 'phone_mobile'),
        "address_title":(By.ID, "alias"),
        "save_button": (By.ID, 'submitAddress'),
        "message": (By.NAME, 'message'),
        "proceed_to_checkout": (By.NAME, 'processAddress')
                }

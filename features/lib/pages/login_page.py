__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from base_page_object import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "signin_button": (By.ID, 'SubmitLogin')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.practiceselenium.com/')

    def login(self,username="abc@xyz.com",passwd="Test@123"):
        self.find_element(*self.locator_dictionary['email']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['signin_button']).click()

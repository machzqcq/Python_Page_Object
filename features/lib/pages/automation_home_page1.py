from selenium.webdriver.common.by import By
from base_page_object import BasePage


class AutomationHomePage1(BasePage):
    locator_dictionary = {
        "startButton_loc3":(By.LINK_TEXT, 'Welcome'),
        "startButton_loc4":(By.LINK_TEXT, 'Welcome1'),
        "startButton_loc5":(By.LINK_TEXT, 'Welcome2')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.seleniumframework.com/')

    def apple(self):
        print self.find_element(*self.startButton_loc).click()


    # def __getattr__(self, what):
    #     print self.locator_dictionary
    #     try:
    #         if what in self.locator_dictionary.keys():
    #         # return super(AutomationHomePage, self).__getattribute__(what)
    #             return self.find_element(*self.locator_dictionary[what])
    #     except AttributeError:
    #         super(AutomationHomePage, self).__getattribute__("method_missing")(what)
    #
    # def method_missing(self, what):
    #     print "No %s here!"%what

    # def __getattr__(self, method_name):
    #     def get(self, **kwargs):
    #         print self.method_dictionary
    #         if method_name in self.method_dictionary:
    #             print("inside if")
    #             return get.__get__(self)
    #         else:
    #             print("inside else")
    #             # If the method isn't in our dictionary, act normal.
    #             raise AttributeError, method_name

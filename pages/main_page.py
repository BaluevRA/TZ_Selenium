from locators import Locators
from base_page import BasePage


class Login(BasePage):
    def click_on_login_button(self):
        return self.find_element(Locators.LOGIN_BUTTON, time=2).click()

    def click_on_avatar(self):
        return self.find_element(Locators.AVATAR, time=2).click()

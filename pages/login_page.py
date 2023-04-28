from locators import Locators
from base_page import BasePage


class Auth(BasePage):
    def enter_email(self):
        email_field = self.find_element(Locators.LOGIN_FIELD)
        email_field.click()
        email_field.send_keys('fortzuser')

    def click_on_email_button(self):
        return self.find_element(Locators.CHOOSE_EMAIL_BUTTON, time=2).click()

    def click_on_enter_button(self):
        return self.find_element(Locators.EMAIL_LOGIN_BUTTON).click()

    def enter_password(self):
        pwd_field = self.find_element(Locators.PASSWORD_FIELD)
        #pwd_field.click()
        pwd_field.send_keys('121212AbC')
        return self.click_on_enter_button()

    def skip_email_add(self):
        return self.find_element(Locators.NOT_NOW).click()

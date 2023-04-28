from locators import Locators
from base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Captcha(BasePage):

    def activate_human_checkbox(self):
        return self.find_element(Locators.CAPTCHA_CHECKBOX).click()

    def time_to_captcha(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON),
                                                      message=f"Невозможно найти элемент {Locators.LOGIN_BUTTON}")

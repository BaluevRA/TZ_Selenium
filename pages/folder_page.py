import time
from locators import Locators
from base_page import BasePage
from random import randint


class Folder(BasePage):
    def create_doc(self):
        doc_name = f'Document-{randint(0, 300)}'
        self.find_element(Locators.BUTTON_CREATE, time=2).click()
        time.sleep(10)
        self.find_element(Locators.CREATE_DOC, time=2).click()
        field = self.find_element(Locators.RENAME_DOC_FIELD, time=2)
        field.send_keys("")
        time.sleep(3)
        field.send_keys(doc_name)
        self.find_element(Locators.CREATE_DOC_BUTTON, time=2).click()
        print('\n'+doc_name)
        return doc_name


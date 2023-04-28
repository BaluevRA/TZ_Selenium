import time
import pyautogui
from locators import Locators
from base_page import BasePage
from random import randint


class Disk(BasePage):
    def create_folder(self):
        folder_name = f'Folder-{randint(0, 300)}'
        self.find_element(Locators.BUTTON_CREATE, time=2).click()
        self.find_element(Locators.CREATE_FOLDER, time=2).click()
        field = self.find_element(Locators.RENAME_FIELD, time=2)
        field.send_keys("")
        time.sleep(3)
        field.send_keys(folder_name)
        self.find_element(Locators.RENAME_BUTTON, time=2).click()

    def open_folder(self):
        self.find_element(Locators.FOLDER).click()
        pyautogui.press('Enter')

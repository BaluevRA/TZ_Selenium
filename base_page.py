from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"
        self.disk_url = "https://disk.yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Невозможно найти элемент {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def element_click(self, locator):
        return self.find_element(self, locator).click()

    def go_to_disk(self):
        return self.driver.get(self.disk_url)

    def switch_windows(self, number):
        doc_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(doc_window)

    def get_windows(self):
        print(self.driver.window_handles)
        return self.driver.window_handles()

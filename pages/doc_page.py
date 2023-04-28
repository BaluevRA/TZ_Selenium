import time

from base_page import BasePage


class Doc(BasePage):
    def switch(self):
        self.switch_windows(1)

    def close_window(self):
        time.sleep(5)
        self.driver.close()

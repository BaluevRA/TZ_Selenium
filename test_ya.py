from pages.main_page import Login
from pages.login_page import Auth
from pages.captcha_page import Captcha
from pages.disk_page import Disk
from pages.folder_page import Folder
from pages.doc_page import Doc
import time


def test_yandex_open(browser):
    yandex_main_page = Login(browser)
    yandex_main_page.go_to_site()


def test_yandex_captcha(browser):
    captcha_page = Captcha(browser)
    try:
        captcha_page.activate_human_checkbox()
        time.sleep(10)
        captcha_page.time_to_captcha()
    except:
        pass


def test_yandex_login(browser):
    yandex_main_page = Login(browser)
    yandex_main_page.click_on_login_button()


def test_yandex_auth(browser):
    ya_auth_page = Auth(browser)
    ya_auth_page.click_on_email_button()
    ya_auth_page.enter_email()
    ya_auth_page.click_on_enter_button()
    ya_auth_page.enter_password()


def test_go_to_disk(browser):
    ya_main_page = Login(browser)
    ya_main_page.click_on_avatar()
    ya_main_page.go_to_disk()


def test_create_folder(browser):
    ya_disk_page = Disk(browser)
    ya_disk_page.create_folder()


def test_open_folder(browser):
    ya_disk_page = Disk(browser)
    ya_disk_page.open_folder()


def test_create_doc(browser):
    folder_page = Folder(browser)
    folder_page.create_doc()


def test_return_to_disk(browser):
    doc_page = Doc(browser)
    doc_page.switch()
    doc_page.close_window()
    time.sleep(6)

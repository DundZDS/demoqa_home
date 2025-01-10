from pages.base_page import BasePage
from tests.swag_labs import SwagLabs


def test_check_icon(browser):
    sauce_demo_page = SwagLabs(browser)
    sauce_demo_page.visit()
    sauce_demo_page.exist_icon()

def test_check_user(browser):
    sauce_demo_page = BasePage(browser)
    sauce_demo_page.visit()
    sauce_demo_page.find_element(locator='#user-name')

def test_check_password(browser):
    sauce_demo_page = BasePage(browser)
    sauce_demo_page.visit()
    sauce_demo_page.find_element(locator='#password')



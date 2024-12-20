from selenium.common import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_field(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True



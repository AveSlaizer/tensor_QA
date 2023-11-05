from .base_page import BasePage
from .locators import SbisLocators


class SbisPage(BasePage):
    url = "https://sbis.ru/"

    def go_to_contacts(self):
        header_contacts_link = self.browser.find_element(*SbisLocators.HEADER_CONTACTS_LINK)
        header_contacts_link.click()

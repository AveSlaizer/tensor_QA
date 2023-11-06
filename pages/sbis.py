import time

from .base_page import BasePage
from .locators import SbisLocators


class SbisPage(BasePage):
    url = "https://sbis.ru/"

    def go_to_contacts(self):
        header_contacts_link = self.browser.find_element(*SbisLocators.HEADER_CONTACTS_LINK)
        header_contacts_link.click()

    def go_to_downloads(self):
        downloads_page_link = self.browser.find_element(*SbisLocators.DOWNLOAD_SBIS_FOOTER_LINK)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", downloads_page_link)
        # self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        downloads_page_link.click()

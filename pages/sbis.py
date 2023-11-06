from .base_page import BasePage
from .locators import SbisLocators


class SbisPage(BasePage):
    url = "https://sbis.ru/"

    def go_to_contacts(self):
        """
        Переход на страницу sbis.ru/contacts
        """
        header_contacts_link = self.browser.find_element(*SbisLocators.HEADER_CONTACTS_LINK)
        header_contacts_link.click()

    def go_to_downloads(self):
        """
        Переход на страницу sbis.ru/downloads
        """
        downloads_page_link = self.browser.find_element(*SbisLocators.DOWNLOAD_SBIS_FOOTER_LINK)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", downloads_page_link)
        downloads_page_link.click()

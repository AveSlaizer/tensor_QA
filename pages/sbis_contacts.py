from .base_page import BasePage
from .locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    url = "https://sbis.ru/contacts/"

    def go_to_tensor_site(self):
        tensor_banner = self.browser.find_element(*SbisContactsLocators.TENSOR_BANNER)
        tensor_banner.click()

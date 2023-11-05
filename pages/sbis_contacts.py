import time

from .base_page import BasePage
from .locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    url = "https://sbis.ru/contacts/"

    def go_to_tensor_site(self):
        tensor_banner = self.browser.find_element(*SbisContactsLocators.TENSOR_BANNER)
        tensor_banner.click()

    def check_region_name_element(self, region_verbose_name: str):
        region_name_element = self.browser.find_element(*SbisContactsLocators.REGION_NAME_NEAR_TITLE_CONTACTS)
        region_name = region_name_element.text
        assert region_name.find(region_verbose_name) != -1, f"{region_verbose_name}: not contains in region name!"

    def should_see_partner_list(self):
        partner_list = self.browser.find_elements(*SbisContactsLocators.PARTNER_LIST)
        if partner_list:
            return partner_list
        raise AssertionError("Partner list not visible!")

    def change_region(self, region_verbose_name: str):
        region_change_link = self.browser.find_element(*SbisContactsLocators.REGION_NAME_NEAR_TITLE_CONTACTS)
        region_change_link.click()
        self.browser.find_element(*SbisContactsLocators.link_to_change_region(region_verbose_name)).click()
        time.sleep(0.1)

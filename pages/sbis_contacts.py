import time

from .base_page import BasePage
from .locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    url = "https://sbis.ru/contacts/"

    def go_to_tensor_site(self):
        """
        Переход на страницу tensor.ru
        """
        tensor_banner = self.browser.find_element(*SbisContactsLocators.TENSOR_BANNER)
        tensor_banner.click()

    def check_region_name_element(self, region_verbose_name: str):
        """
        Вызывает AssertionError если на странице не отображается название региона
        :param region_verbose_name:  название региона, которое должно отображаться на сайте
        """
        region_name_element = self.browser.find_element(*SbisContactsLocators.REGION_NAME_NEAR_TITLE_CONTACTS)
        region_name = region_name_element.text
        assert region_name.find(region_verbose_name) != -1, f"{region_verbose_name}: not contains in region name!"

    def should_see_partner_list(self):
        """
        Возвращает список партнеров, отображаемых на странице, иначе AssertionError
        """
        partner_list = self.browser.find_elements(*SbisContactsLocators.PARTNER_LIST)
        if partner_list:
            return partner_list
        raise AssertionError("Partner list not visible!")

    def change_region(self, region_verbose_name: str):
        """
        Переключает регион на переданный
        :param region_verbose_name: регион, на который следует переключиться
        """
        region_list_link = self.browser.find_element(*SbisContactsLocators.REGION_NAME_NEAR_TITLE_CONTACTS)
        region_list_link.click()
        region_name_link = self.browser.find_element(*SbisContactsLocators.link_to_change_region(region_verbose_name))
        region_name_link.click()
        time.sleep(0.1)

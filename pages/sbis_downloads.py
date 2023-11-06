import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

from .base_page import BasePage
from .locators import SbisDownloadsLocators


class SbisDownloadsPage(BasePage):
    url = "https://sbis.ru/download"
    __downloads_directory = os.getcwd() + '\\downloads\\'
    __file_size_on_page: float
    __file_name: str

    def download_sbis_plugin_for_windows_installer(self):
        """
        Скачивает вэб установщик плагина для Windows. Проверяет, что он действительно скачался.
        """
        time.sleep(0.5)  # Со слипом работает стабильней
        plugin_category_link = self.browser.find_element(*SbisDownloadsLocators.SBIS_PLUGIN_CATEGORY)
        plugin_category_link.click()

        plugin_for_windows_category_link = WebDriverWait(self.browser, 5).\
            until(EC.element_to_be_clickable(SbisDownloadsLocators.SBIS_PLUGIN_FOR_WINDOW))
        plugin_for_windows_category_link.click()

        sbis_plugin_for_windows_link = self.browser.find_element(
            *SbisDownloadsLocators.SBIS_PLAUGIN_FOR_WINDOWS_DOWNLOAD_LINK
        )
        visible_link_text = sbis_plugin_for_windows_link.text
        download_url = sbis_plugin_for_windows_link.get_attribute('href')

        self.__file_size_on_page = self.__get_file_size_from_link_visible_text(visible_link_text)
        self.__file_name = download_url[download_url.rfind('/') + 1:]

        response = requests.get(download_url)
        if response.status_code == 200:

            if not os.path.isdir(self.__downloads_directory):
                os.mkdir(self.__downloads_directory)

            with open(self.__downloads_directory + self.__file_name, 'wb') as f:
                f.write(response.content)
        else:
            assert False, "Cant download file, server is not responding!"
        self.__is_file_downloaded()

    def is_file_sizes_on_page_and_disk_in_megabytes_same(self):
        """
        Проверяет, что размер файла отображаемый на сайте равен размеру файла да диске после скачивания.
        Иначе AssertionError
        """
        size_on_disk = self.__get_rounded_file_size_in_megabytes_from_bytes()
        assert size_on_disk == self.__file_size_on_page, \
            f"Error! File size on disk: '{size_on_disk} Mb', file size on page: '{self.__file_size_on_page} Mb'."

    def __get_rounded_file_size_in_megabytes_from_bytes(self):
        """
        Возвращает округленный до 2-х знаков размер файла на диске в мегабайтах
        :return: float Размер файла
        """
        stats = os.stat(self.__downloads_directory + self.__file_name)
        rounded_size_in_mega_bytes = round((stats.st_size / 1048576), 2)
        return rounded_size_in_mega_bytes

    @staticmethod
    def __get_file_size_from_link_visible_text(link_visible_text: str) -> float:
        """
        Возвращает размер файла, отображаемый в тексте на странице сайта.
        :param link_visible_text:
        :return:
        """
        file_size = ''

        for symbol in link_visible_text:
            if symbol.isdigit() or symbol == ".":
                if file_size == '' and symbol == '.':
                    continue
                file_size += symbol

        if file_size.endswith('.'):
            while file_size.endswith('.'):
                file_size = file_size[:-1]

        if ".." in file_size:
            while ".." in file_size:
                file_size = file_size.replace("..", ".")

        return float(file_size)

    def __is_file_downloaded(self):
        """
        Вызывает AssertionError, если файл не найден в директории (не был скачан)
        """
        file_list = os.listdir(self.__downloads_directory)
        assert self.__file_name in file_list, f"'{self.__file_name}' not founded in '{self.__downloads_directory}'!"

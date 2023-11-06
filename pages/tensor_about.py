from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    url = "https://tensor.ru/about"

    def should_be_block_named_working(self):
        """
        Вызывает AssertionError, если блок "Работаем" не отображен на странице
        """
        assert self.is_element_present(*TensorAboutPageLocators.BLOCK_NAMED_WORKING_TITLE)

    def find_images_in_block_working(self) -> list:
        """
        Возвращает список картинок, отображенных в блоке "Работаем", иначе AssertionError
        :return: list: список картинок
        """
        images = self.browser.find_elements(*TensorAboutPageLocators.BLOCK_NAMED_WORKING_IMAGES)
        if images:
            return images
        assert False, "Images not found!"

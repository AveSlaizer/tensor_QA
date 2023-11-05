import time

from .base_page import BasePage
from .locators import TensorPageLocators


class TensorPage(BasePage):
    url = 'https://tensor.ru/'

    def should_be_block_strength_in_people(self):
        assert self.is_element_present(*TensorPageLocators.STRENGTH_IN_PEOPLE_BLOCK)

    def go_to_tensor_about(self):
        button = self.browser.find_element(*TensorPageLocators.STRENGTH_IN_PEOPLE_BLOCK_LINK_ABOUT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

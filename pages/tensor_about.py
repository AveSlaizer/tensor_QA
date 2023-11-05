from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    url = "https://tensor.ru/about"

    def should_be_block_named_working(self):
        assert self.is_element_present(*TensorAboutPageLocators.BLOCK_NAMED_WORKING_TITLE)

    def find_images_in_block_working(self):
        images = self.browser.find_elements(*TensorAboutPageLocators.BLOCK_NAMED_WORKING_IMAGES)
        if images:
            return images
        assert False, "Images not found!"

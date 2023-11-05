from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser: WebDriver, url: str, time_out: [float, int] = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(time_to_wait=time_out)

    @staticmethod
    def get_image_size(image: WebElement) -> tuple[str, str]:
        return image.get_attribute("width"), image.get_attribute("height")

    @staticmethod
    def images_should_have_same_size(images):
        sizes_set = set()
        for image in images:
            sizes_set.add(BasePage.get_image_size(image))
        assert len(sizes_set) == 1, f"Images have {len(sizes_set)} different sizes!"

    def is_element_present(self, by: str, value: str):
        try:
            element = self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True

    def is_symbols_in_current_url(self, symbols: str):
        current_url = self.browser.current_url
        assert current_url.find(symbols) != -1

    def open(self):
        self.browser.get(self.url)

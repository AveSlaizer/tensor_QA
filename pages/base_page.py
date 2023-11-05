from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url: str, time_out: [float, int] = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(time_to_wait=time_out)

    def is_element_present(self, by: str, value: str):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True

    def is_symbols_in_current_url(self, symbols: str):
        current_url = self.browser.current_url
        assert current_url.find(symbols) != -1

    def open(self):
        self.browser.get(self.url)

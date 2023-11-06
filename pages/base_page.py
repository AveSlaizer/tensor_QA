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
        """
        Возвращает значения параметров width и height картинки, отображаемой на странице
        :param image: WebElement элемент страницы
        :return: tuple: ( ширина, высота)
        """
        return image.get_attribute("width"), image.get_attribute("height")

    @staticmethod
    def images_should_have_same_size(images: list[WebElement]):
        """
        Вызывает AssertionError если размеры переданных картинок разные
        :param images: list список картинок
        """
        sizes_set = set()
        for image in images:
            sizes_set.add(BasePage.get_image_size(image))
        assert len(sizes_set) == 1, f"Images have {len(sizes_set)} different sizes!"

    @staticmethod
    def is_element_lists_are_different(first__element_list: list, second_element_list: list):
        """
        Вызывает AssertionError если переданные списки элементов одинаковые
        :param first__element_list: первый список элементов
        :param second_element_list: второй список элементов
        """
        assert first__element_list != second_element_list, "Element lists are the same!"

    def is_element_present(self, by: str, value: str):
        """
        Возвращает True, если элемент представлен на странице, иначе False
        :param by: Метод поиска элемента
        :param value: Значение для метода поиска
        :return: True | False
        """
        try:
            element = self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True

    def is_symbols_in_current_url(self, symbols: str):
        """
        Вызывает AssertionError если переданная строка не содержится в текущем url браузера
        :param symbols: строка
        """
        current_url = self.browser.current_url
        assert current_url.find(symbols) != -1, f"'{symbols}' not in current url!"

    def open(self):
        """
        Открывает страницу в браузере
        """
        self.browser.get(self.url)

from pages.sbis import SbisPage
from pages.sbis_contacts import SbisContactsPage
from pages.tensor import TensorPage
from pages.tensor_about import TensorAboutPage
from pages.sbis_downloads import SbisDownloadsPage


class TestScenarioOne:
    """
    Первый тестовый сценарий:
        1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Найти баннер Тензор, кликнуть по нему
        3) Перейти на https://tensor.ru/
        4) Проверить, что есть блок "Сила в людях"
        5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
            https://tensor.ru/about
        6) Находим раздел Работаем и проверяем, что у всех фотографии
            хронологии одинаковые высота (height) и ширина (width)
    """

    def test_guest_can_go_to_sbis_contacts_page(self, browser):
        page = SbisPage(browser, SbisPage.url)
        page.open()
        page.go_to_contacts()

    def test_guest_can_go_to_tensor_page(self, browser):
        page = SbisContactsPage(browser, browser.current_url)
        page.go_to_tensor_site()
        tabs = page.browser.window_handles
        page.browser.switch_to.window(tabs[1])

    def test_guest_can_see_block_strength_in_people(self, browser):
        page = TensorPage(browser, browser.current_url)
        page.should_be_block_strength_in_people()

    def test_guest_can_go_to_tensor_about_page(self, browser):
        page = TensorPage(browser, browser.current_url)
        page.go_to_tensor_about()
        page.is_symbols_in_current_url('tensor.ru/about')

    def test_images_have_same_sizes(self, browser):
        page = TensorAboutPage(browser, browser.current_url)
        page.should_be_block_named_working()
        images = page.find_images_in_block_working()
        page.images_should_have_same_size(images)


class TestScenarioTwo:
    """
    Второй тестовый сценарий
        1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Проверить, что определился ваш регион (в нашем примере
            Ярославская обл.) и есть список партнеров.
        3) Изменить регион на Камчатский край
        4) Проверить, что подставился выбранный регион, список партнеров
            изменился, url и title содержат информацию выбранного региона
    """

    @classmethod
    def setup_class(cls):
        cls.partner_list_to_check = []
        cls.current_region_verbose_name = 'Ярославская'
        cls.region_name_in_url = 'kamchatskij-kraj'
        cls.region_verbose_name = 'Камчатский край'

    def test_guest_can_go_to_sbis_contacts_page(self, browser):
        page = SbisPage(browser, SbisPage.url)
        page.open()
        page.go_to_contacts()

    def test_guest_can_see_region_name_element(self, browser):
        page = SbisContactsPage(browser, browser.current_url)
        page.check_region_name_element(self.current_region_verbose_name)

    def test_guest_can_see_list_of_partners(self, browser):
        page = SbisContactsPage(browser, browser.current_url)
        self.partner_list_to_check = page.should_see_partner_list()

    def test_guest_can_change_region(self, browser):
        page = SbisContactsPage(browser, browser.current_url)
        page.change_region(self.region_verbose_name)

    def test_region_was_changed(self, browser):
        page = SbisContactsPage(browser, browser.current_url)
        page.check_region_name_element(self.region_verbose_name)
        page.is_symbols_in_current_url(self.region_name_in_url)
        new_partner_list = page.should_see_partner_list()
        page.is_element_lists_are_different(self.partner_list_to_check, new_partner_list)


class TestScenarioThree:
    """
    Третий тестовый сценарий
    1) Перейти на https://sbis.ru/
    2) В Footer'e найти и перейти "Скачать СБИС"
    3) Скачать СБИС Плагин для вашей для windows, веб-установщик в
        папку с данным тестом
    4) Убедиться, что плагин скачался
    5) Сравнить размер скачанного файла в мегабайтах. Он должен
        совпадать с указанным на сайте.
    """
    def test_guest_can_go_to_downloads_page(self, browser):
        page = SbisPage(browser, SbisPage.url)
        page.open()
        page.go_to_downloads()

    def test_guest_can_download_sbis_plugin_for_windows(self, browser):
        page = SbisDownloadsPage(browser, browser.current_url)
        page.download_sbis_plugin_for_windows_installer()
        page.is_file_sizes_on_page_and_disk_in_megabytes_same()

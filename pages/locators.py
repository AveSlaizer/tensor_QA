from selenium.webdriver.common.by import By


class SbisLocators:
    """
    Локаторы для страницы "https://sbis.ru/"
    """
    # Ссылка "Контакты" в хэдэре
    HEADER_CONTACTS_LINK = (
        By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]'
    )
    # ССылка "Скачать СБИС" в футере
    DOWNLOAD_SBIS_FOOTER_LINK = (
        By.XPATH,
        '//a[text()="Скачать СБИС"]'
    )


class SbisContactsLocators:
    """
    Локаторы для страницы "https://sbis.ru/contacts/"
    """
    # Баннер "Тензор"
    TENSOR_BANNER = (
        By.CSS_SELECTOR,
        '#contacts_clients a[title="tensor.ru"]'
    )
    # Список партнеров в блоке "Партнеры"
    PARTNER_LIST = (
        By.CSS_SELECTOR,
        'div.sbisru-Contacts-List__name'
    )
    # Ссылка-название региона около заголовка "Контакты"
    REGION_NAME_NEAR_TITLE_CONTACTS = (
        By.XPATH,
        '(//span)[contains(@class, "sbis_ru-link")][1]'
    )

    @staticmethod
    def link_to_change_region(region_verbose_name: str):
        """
        Ссылка для смены региона.
        :param region_verbose_name: Русское название региона отображаемое на странице сайта.
        :return: tuple: метод поиска и значение, по которому искать.
        """
        return By.CSS_SELECTOR, f'span[title="{region_verbose_name}"]'


class SbisDownloadsLocators:
    """
    Локаторы для страницы "https://sbis.ru/download"
    """
    # Ссылка выбора категории "СБИС Плагин"
    SBIS_PLUGIN_CATEGORY = (
        By.CSS_SELECTOR,
        'div[data-id="plugin"]'
    )
    # Ссылка выбора установщиков плагина для Windows
    SBIS_PLUGIN_FOR_WINDOW = (
        By.CSS_SELECTOR,
        'div[data-for="plugin"] div[data-id="default"]'
    )
    # Ссылка на файл СБИС плагин для Windows
    SBIS_PLAUGIN_FOR_WINDOWS_DOWNLOAD_LINK = (
        By.CSS_SELECTOR,
        'a[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]'
    )


class TensorPageLocators:
    """
    Локаторы для страницы 'https://tensor.ru/'
    """
    # Блок "Сила в людях"
    STRENGTH_IN_PEOPLE_BLOCK = (
        By.XPATH,
        '//div/p[1][text()="Сила в людях"]'
    )
    # Ссылка "Подробнее" в блоке "Сила в людях"
    STRENGTH_IN_PEOPLE_BLOCK_LINK_ABOUT = (
        By.XPATH,
        '//div/p/a[@href="/about"]'
    )


class TensorAboutPageLocators:
    """
    Локаторы для страницы "https://tensor.ru/about"
    """
    # Блок "Работаем"
    BLOCK_NAMED_WORKING_TITLE = (
        By.XPATH,
        '//h2[text()="Работаем"]'
    )
    # Картинки в блоке "Работаем"
    BLOCK_NAMED_WORKING_IMAGES = (
        By.CSS_SELECTOR,
        "img.tensor_ru-About__block3-image"
    )

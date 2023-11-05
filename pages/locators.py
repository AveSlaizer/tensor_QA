from selenium.webdriver.common.by import By


class SbisLocators:
    # Ссылка "Контакты" в хэдэре
    HEADER_CONTACTS_LINK = (
        By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]'
    )


class SbisContactsLocators:
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


class TensorPageLocators:
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

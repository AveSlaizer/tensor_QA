from selenium.webdriver.common.by import By


class SbisLocators:
    HEADER_CONTACTS_LINK = (
        By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]'
    )  # Ссылка "Контакты" в хэдэре


class SbisContactsLocators:
    TENSOR_BANNER = (
        By.CSS_SELECTOR,
        '#contacts_clients a[title="tensor.ru"]'
    )  # Баннер "Тензор"


class TensorPageLocators:
    STRENGTH_IN_PEOPLE_BLOCK = (
        By.XPATH,
        '//div/p[1][text()="Сила в людях"]'
    )  # Блок "Сила в людях"
    STRENGTH_IN_PEOPLE_BLOCK_LINK_ABOUT = (
        By.XPATH,
        '//div/p/a[@href="/about"]'
    )  # Ссылка "Подробнее" в блоке "Сила в людях"


class TensorAboutPageLocators:
    BLOCK_NAMED_WORKING_TITLE = (
        By.XPATH,
        '//h2[text()="Работаем"]'
    )
    BLOCK_NAMED_WORKING_IMAGES = (
        By.CSS_SELECTOR,
        "img.tensor_ru-About__block3-image"
    )

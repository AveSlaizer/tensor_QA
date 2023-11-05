from pages.sbis import SbisPage
from pages.sbis_contacts import SbisContactsPage
from pages.tensor import TensorPage
from pages.tensor_about import TensorAboutPage


class TestScenarioOne:

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

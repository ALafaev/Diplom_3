import allure

from ..pages.base_page import BasePage
from urls import PageUrls


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = PageUrls.ORDER_FEED_PAGE

    @allure.step('Проверка, что текущий url соответствует url страницы "Лента заказов"')
    def check_current_url(self):
        return self.wait_url_to_be(self.url)
from PageObject.Locators.main_page_loc import MainPageLoc
from PageObject.Pages.base_page import BasePage
from PageObject.Locators.basket_page_loc import BasketPageLoc


class BasketPage(BasePage):

    def verify_basket_page_url(self): # Проверка URL страницы корзины.
        basket_page_url = self.chrome.current_url
        assert basket_page_url == BasketPageLoc.basket_page_url_loc, 'Basket page URL is not equall recieved link!'

    def verify_basket_is_empty(self):
        assert self.element_is_present(MainPageLoc.basket_empty_loc), 'Basket is not empty!'

    # Проверка на добавление в корзину faded short
    def verify_faded_short_in_basket(self):
        assert self.element_is_present(BasketPageLoc.added_to_basket_faded_short), "Faded short isn't add to basket!"

    # Проверка на добавление в корзину blouse
    def verify_blouse_in_basket(self):
        assert self.element_is_present(BasketPageLoc.added_to_basket_blouse), "Blouse isn't add to basket!"
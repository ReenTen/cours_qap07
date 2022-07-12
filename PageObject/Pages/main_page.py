from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from PageObject.Pages.base_page import BasePage
from PageObject.Locators.main_page_loc import MainPageLoc


class MainPage(BasePage):

    def verify_main_page_url(self):
        main_page_url = self.chrome.current_url
        assert main_page_url == MainPageLoc.main_page_url_loc, 'Main page URL is not equall recieved link!'

    def open_login_page(self): # Открыть страницу логина
        time.sleep(3)
        login_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.login_loc))    #Импорт локатора логина из файла main_page_loc класса MainPageLoc. Используем явное ожидание, т.к. переход на страницу логина ломает сайт
        login_link.click()

    def verify_login_link(self): # Метод "Проверка ссылки на страницу логина"
        assert self.element_is_present(MainPageLoc.login_loc), "Login link is not presen at this page!"

    def verify_basket_is_empty(self): #Проверка, что корзина пуста
        assert self.element_is_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def open_basket_page(self): # Открыть страницу корзины
        time.sleep(3)
        basket_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.basket_loc))    #Импорт локатора логина из файла main_page_loc класса MainPageLoc. Используем явное ожидание, т.к. переход на страницу логина ломает сайт
        basket_link.click()

    def add_to_basket_faded_short(self):
        time.sleep(3)
        add_faded_short = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(
            MainPageLoc.button_add_to_basket_faded_short_loc))
        add_faded_short.click()

    def add_to_basket_blouse(self):
        time.sleep(3)
        add_blouse = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(
            MainPageLoc.button_add_to_basket_blouse_loc))
        add_blouse.click()

    def close_product_window(self):
        close_window = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(
            MainPageLoc.close_window_loc))
        close_window.click()

    def open_contact_page(self): # Открыть страницу contact_us
        time.sleep(3)
        contact_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.contact_loc))    #Импорт локатора логина из файла main_page_loc класса MainPageLoc. Используем явное ожидание, т.к. переход на страницу логина ломает сайт
        contact_link.click()
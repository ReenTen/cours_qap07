from PageObject.Pages.basket_page import BasketPage
from PageObject.Pages.login_page import LoginPage
from PageObject.Pages.main_page import MainPage
from PageObject.Pages.contact_page import ContactPage
from selenium import webdriver
import pytest


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')


def test_guest_can_go_to_login_page(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url

    try:
        main_page.open()  # Открываем страницу (описан в base_page)
        main_page.verify_login_link()
        main_page.open_login_page()  # Выполняем метод страницы — переходим на страницу логина (описан в main_page)
        login_page = LoginPage(browser, url=browser.current_url) # Открываем страницу логина по указаной ссылке
        login_page.verify_login_page_url()
        login_page.verify_login_link()


    finally:
        browser.quit()

def test_go_to_contact_page(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url

    try:
        main_page.open()  # Открываем страницу (описан в base_page)
        main_page.open_contact_page()
        contact_page = ContactPage(browser, 'http://automationpractice.com/index.php?controller=contact')
        contact_page.verify_text()

    finally:
        browser.quit()


def test_basket_is_empty(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.verify_basket_is_empty()
    finally:
        browser.quit()


def test_add_to_basket(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.add_to_basket_faded_short()
        main_page.close_product_window()
        main_page.add_to_basket_blouse()
        main_page.close_product_window()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.verify_faded_short_in_basket()
        basket_page.verify_blouse_in_basket()

    finally:
        browser.quit()

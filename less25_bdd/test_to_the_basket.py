from PageObject.Pages.basket_page import BasketPage
from PageObject.Pages.main_page import MainPage
from selenium import webdriver
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios(r'C:\Users\Admin\PycharmProjects\pythonProject\less24_bdd\to_the_basket_test.feature')


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
    yield browser
    browser.quit()


@given('User open main page')
def open_site(open_browser):
    global main_page
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    main_page.open()


@when('User click at the basket link')
def open_basket(open_browser):
    main_page.open_basket_page()


@then('User check, that this is basket')
def verify_basket_page(open_browser):
    link = 'http://automationpractice.com/index.php?controller=order'
    basket_page = BasketPage(browser, link)
    basket_page.verify_basket_page_url()

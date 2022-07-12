from PageObject.Locators.login_page_loc import LoginPageLoc
from PageObject.Locators.main_page_loc import MainPageLoc
from PageObject.Pages.base_page import BasePage


class LoginPage(BasePage):

    def verify_login_page_url(self): # Проверка URL страницы авторизации.
        login_page_url = self.chrome.current_url
        assert login_page_url == LoginPageLoc.login_page_url_loc, 'Login page URL is not equall recieved link!'

    def verify_login_link(self): # Проверка ссылки на страницу логина на странице логина
        assert self.element_is_present(MainPageLoc.login_loc), "Login link is not present at this page!"

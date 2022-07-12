from selenium.common.exceptions import NoSuchElementException


# # Действия в base_page относятся ко всей странице
# # В конструкторе больше редко что-то указывается
# # По функциям - можно сколько угодно

class BasePage():
    def __init__(self, browser, url):
        self.chrome = browser
        self.url = url
        self.chrome.implicitly_wait(5)

    def open(self):
        self.chrome.get(self.url)

    def element_is_present(self, locator):
        try:
            self.chrome.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

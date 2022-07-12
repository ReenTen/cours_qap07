import time

from PageObject.Locators.main_page_loc import MainPageLoc
from PageObject.Pages.base_page import BasePage
from PageObject.Locators.contact_page_loc import ContactPageLoc


class ContactPage(BasePage):

    def verify_text(self):
        time.sleep(2)
        text = self.chrome.find_element(*ContactPageLoc.text_loc).text
        assert text == 'CUSTOMER SERVICE - CONTACT US', 'Something wrong!'

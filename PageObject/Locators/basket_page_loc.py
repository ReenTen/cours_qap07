from selenium.webdriver.common.by import By


class BasketPageLoc:

    basket_page_url_loc = 'http://automationpractice.com/index.php?controller=order'

    added_to_basket_faded_short = (By.XPATH, '//dt//img[@alt="Faded Short Sleeve T-shirts"]')
    added_to_basket_blouse = (By.XPATH, '//dt//img[@alt="Blouse"]')

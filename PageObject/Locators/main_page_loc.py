from selenium.webdriver.common.by import By


class MainPageLoc:

    main_page_url_loc = 'http://automationpractice.com/index.php'

    login_loc = (By.CSS_SELECTOR, '.login') # Локатор для перехода на страницу логина
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]') # Локатор на проверку того, что корзина пуста
    basket_loc = (By.XPATH, '//a[@title="View my shopping cart"]') # Локатор для перехода в корзину

    button_add_to_basket_faded_short_loc = (By.XPATH, '//a[@data-id-product="1"]')
    button_add_to_basket_blouse_loc = (By.XPATH, '//a[@data-id-product="2"]')

    close_window_loc = (By. XPATH, '//span[@title="Close window"]')

    contact_loc = (By. XPATH, '//a[@title="Contact Us"]')

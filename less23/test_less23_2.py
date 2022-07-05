from selenium import webdriver
from selenium.webdriver.common.by import By


def test_boxes():
    global chrome
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()
        chrome.implicitly_wait(5)

        checkbox = chrome.find_element(By.XPATH, '//input[@type="checkbox"]')
        checkbox.click()
        remove_button = chrome.find_element(By.XPATH, '//button[@onclick="swapCheckbox()"]')
        remove_button.click()
        text = chrome.find_element(By.CSS_SELECTOR, "p#message").text
        assert 'It\'s gone!' == text, 'Something wrong!!!'

        # Проверка checkbox на присутствие.
        # find_elements возвращает список найденных элементов.
        # Если элемент не найден, то длина списка > 0, если нет, то <=0.
        if len(chrome.find_elements(By.XPATH, '//input[@type="checkbox"]/..'))>0:
            print('\nCheckbox on it\'s place.')
        else:
            print('\nCheckbox gone.')

        input_field = chrome.find_element(By.XPATH, '//input[@type="text"]')

        if input_field.is_enabled():
            print('\nInput field is ENABLE')
        else:
            print('\nInput field is NOT ENABLE')

        enable_button = chrome.find_element(By.XPATH, '//button[@onclick="swapInput()"]')
        enable_button.click()
        text_2 = chrome.find_element(By.XPATH, '//p[@id="message"]').text
        assert 'It\'s enabled!' == text_2, 'Something wrong!!!'

        if input_field.is_enabled():
            print('Input field is ENABLE NOW')
        else:
            print('Input field is NOT ENABLE NOW')

    finally:
        chrome.quit()

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_button():
    global chrome
    url = 'https://ultimateqa.com/complicated-page/'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        button = chrome.find_element(By.CSS_SELECTOR, '.et_pb_button.et_pb_button_4')
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

        button = chrome.find_element(By.CLASS_NAME, 'et_pb_button.et_pb_button_4.et_pb_bg_layout_light')
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

        button = chrome.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light']")
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

    finally:
        chrome.quit()
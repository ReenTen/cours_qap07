from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_select_menu():
    global chrome
    url = 'https://demoqa.com/select-menu'

    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.fullscreen_window()

        old_style_select = Select(chrome.find_element(By.ID, 'oldSelectMenu'))
        old_style_select.select_by_value('4')
        time.sleep(2)

        standart_ms = Select(chrome.find_element(By.NAME, 'cars'))
        standart_ms.select_by_value('opel')
        time.sleep(2)

        select_value = chrome.find_element(By.XPATH, ('//*[@id="withOptGroup"]/div'))
        select_value.click()
        time.sleep(2)
        list_select_value = chrome.find_element(By.ID, 'react-select-2-option-0-0')
        list_select_value.click()
        time.sleep(2)

        select_one = chrome.find_element(By.XPATH, '//*[@id="selectOne"]/div')
        select_one.click()
        time.sleep(2)
        list_select_one = chrome.find_element(By.XPATH, ("//*[contains(text(), 'Mrs.')]"))
        list_select_one.click()
        time.sleep(2)

        multiselect = chrome.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div')
        multiselect.click()
        time.sleep(2)
        list_multiselect = chrome.find_element(By.ID, 'react-select-4-option-2')
        list_multiselect.click()
        time.sleep(2)
        list_multiselect = chrome.find_element(By.ID, 'react-select-4-option-3')
        list_multiselect.click()
        time.sleep(2)

    finally:
        chrome.quit()



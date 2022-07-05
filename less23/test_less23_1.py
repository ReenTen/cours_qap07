from selenium import webdriver
from selenium.webdriver.common.by import By


def test_iframe_text():
    global chrome
    url = 'http://the-internet.herokuapp.com/frames'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        iframe_link = chrome.find_element(By.XPATH, '//a[@href="/iframe"]')
        iframe_link.click()

        iframe = chrome.switch_to.frame(chrome.find_element(By.ID, 'mce_0_ifr'))
        check_text = chrome.find_element(By.XPATH, '//p').text
        assert 'Your content goes here.' == check_text, f'This text is not equall {check_text}!!!'

        chrome.switch_to.default_content()
        chrome.close()

    finally:
        chrome.quit()

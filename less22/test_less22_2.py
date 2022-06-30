from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_feedback_form():
    global chrome
    url = 'https://ultimateqa.com/filling-out-forms/'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        name_input = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name_input.send_keys('John Doe')
        time.sleep(2)

        message_input = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        message_input.send_keys('There was an angry comment from a hungry man.')
        time.sleep(2)

        button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

        out_message = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message').text
        assert 'Thanks for contacting us' == out_message, f'Try again'

        out_message_displayed = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message')
        out_message_displayed.is_displayed()

    finally:
        chrome.quit()


def test_only_name_form():
    global chrome
    url = 'https://ultimateqa.com/filling-out-forms/'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        name_input = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name_input.send_keys('John Doe')
        time.sleep(2)

        button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

        out_message = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message').text
        assert 'Please, fill in the following fields:\nMessage' == out_message, f'Try again'

        out_message_displayed = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message')
        out_message_displayed.is_displayed()

    finally:
        chrome.quit()


def test_only_message_form():
    global chrome
    url = 'https://ultimateqa.com/filling-out-forms/'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        message_input = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        message_input.send_keys('There was an angry comment from a hungry man.')
        time.sleep(2)

        button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        button_move = ActionChains(chrome).move_to_element(button)
        button_move.perform()
        button.click()
        time.sleep(2)

        out_message = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message').text
        assert 'Please, fill in the following fields:\nName' == out_message, f'Try again'

        out_message_displayed = chrome.find_element(By.CSS_SELECTOR, '.et_pb_contact_form_0>.et-pb-contact-message')
        out_message_displayed.is_displayed()

    finally:
        chrome.quit()


if __name__ == '__main_':
    test_feedback_form()
    test_only_name_form()
    test_only_message_form()

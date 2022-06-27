from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_test_box_page():
    global chrome
    url = 'https://demoqa.com/text-box'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.maximize_window()

        full_name_input = chrome.find_element(By.ID, 'userName')
        full_name_input.send_keys('Ian')

        email_input = chrome.find_element(By.ID, 'userEmail')
        email_input.send_keys('ian@yahoo.com')

        curr_address_input = chrome.find_element(By.ID, 'currentAddress')
        curr_address_input.send_keys('1880, Elm street')

        perm_address_input = chrome.find_element(By.ID, 'permanentAddress')
        perm_address_input.send_keys('10050, Cielo Drive')
        time.sleep(5)

        submit_button = chrome.find_element(By.ID, 'submit')
        chrome.execute_script("arguments[0].click();", submit_button)
        time.sleep(5)

        out_name = chrome.find_element(By.ID, 'name').text
        out_email = chrome.find_element(By.ID, 'email').text
        out_curr_address = chrome.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]').text
        out_perm_address = chrome.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]').text

        assert 'Name:Ian' == out_name, f'Ian is not equall {out_name}'
        assert 'Email:ian@yahoo.com' == out_email, f'ian@yahoo.com is not equall {out_email}'
        assert 'Current Address :1880, Elm street' == out_curr_address,\
            f'1880, Elm street is not equall {out_curr_address}'
        assert 'Permananet Address :10050, Cielo Drive' == out_perm_address,\
            f'10050, Cielo Drive не равно {out_perm_address}'

    finally:
        chrome.quit()

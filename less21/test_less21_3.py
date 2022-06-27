from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_register_form():
    global chrome
    url = 'http://demo.guru99.com/test/newtours/register.php'
    try:
        chrome = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')
        chrome.get(url)
        chrome.fullscreen_window()

        first_name = chrome.find_element(By.NAME, 'firstName')
        first_name.send_keys('Jack')

        last_name = chrome.find_element(By.NAME, 'lastName')
        last_name.send_keys('Grub')

        phone = chrome.find_element(By.NAME, 'phone')
        phone.send_keys('(303) 993-5517')

        email = chrome.find_element(By.NAME, 'userName')    #strange name for this filed, but OK
        email.send_keys('jackgrub@yahoo.com')

        address = chrome.find_element(By.NAME, 'address1')
        address.send_keys('1050 Marshall St')

        city = chrome.find_element(By.NAME, 'city')
        city.send_keys('Denver')

        state = chrome.find_element(By.NAME, 'state')
        state.send_keys('Colorado')

        postal_code = chrome.find_element(By.NAME, 'postalCode')
        postal_code.send_keys('80214')

        country = Select(chrome.find_element(By.NAME, 'country'))
        country.select_by_value('UNITED STATES')

        user_name = chrome.find_element(By.NAME, 'email')    #another strange name..
        user_name.send_keys('Jack-GR')

        password = chrome.find_element(By.NAME, 'password')
        password.send_keys('123qwerty321')

        confirm_pass = chrome.find_element(By.NAME, 'confirmPassword')
        confirm_pass.send_keys('123qwerty321')

        button = chrome.find_element(By.NAME, 'submit')
        button.click()
        time.sleep(3)

        name_verification = chrome.find_element(By.XPATH, '(.//tr//table//font)[4]').text
        assert 'Dear Jack Grub,' == name_verification, f'Your name is not equall {name_verification}'

        user_name_verification = chrome.find_element(By.XPATH, '(.//tr//table//font)[6]').text
        assert 'Note: Your user name is Jack-GR.' == user_name_verification, f'Your username is not equall {user_name_verification}'

    finally:
        chrome.quit()
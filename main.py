#
#
from selenium import webdriver
from requestium import Session, Keys
import time
# initialize chrome
s = Session(webdriver_path=r'C:\chromedriver\chromedriver.exe',
            browser='chrome',
            default_timeout=15)

# go to kaalaak.com
s.driver.get('https://www.kaalaak.com')

# login in to kaalaak
login_menu = '//*[(@id = "login-button")]'
s.driver.ensure_element_by_xpath(login_menu, timeout=10).ensure_click()

username_xpath = '//*[@id="username"]'
password_xpath = '//*[@id="password"]'

s.driver.ensure_element_by_xpath(username_xpath, timeout=5).send_keys('amirhosseinfardi94@gmail.com')
s.driver.ensure_element_by_xpath(password_xpath, timeout=5).send_keys('123456')

login_button = '//*[@id="login_form"]/div[5]/button'
s.driver.ensure_element_by_xpath(login_button, timeout=60).ensure_click()
time.sleep(30)




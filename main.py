#
#
from selenium import webdriver
from requestium import Session, Keys
import time

# initialize chrome
s = Session(webdriver_path=r'C:\chromedriver\chromedriver.exe',
            browser='chrome',
            default_timeout=15,
            )
s.driver.maximize_window()
# --------------------- go to kaalaak.com -------------------------
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
time.sleep(2)

# -------------------- go to product page-----------------------

# pishkhan_xpath = '//*[(@id = "login-button")]'
# s.driver.ensure_element_by_xpath(pishkhan_xpath, timeout=10).ensure_click()
pishkhan_address = 'https://www.kaalaak.com/dashboard'
s.driver.get(pishkhan_address)
time.sleep(2)
sidebar_shopping_manager_xpath = '//*[@id="sidebar_main"]/div/div[1]/div[2]/ul/li[7]/a'
s.driver.ensure_element_by_xpath(sidebar_shopping_manager_xpath,
                                 state='clickable',
                                 timeout=10).ensure_click()

sidebar_shopping_manager_product_xpath = '//*[@id="sidebar_main"]/div/div[1]/div[2]/ul/li[7]/ul/li[1]/a'
s.driver.ensure_element_by_xpath(sidebar_shopping_manager_product_xpath, timeout=10).ensure_click()
# pishkhan_address = 'https://www.kaalaak.com/dashboard'
#
# product_page = 'https://www.kaalaak.com/dashboard?VER=6.7#!/products/manage'
# s.driver.get(product_page)

# ----------------- open new product ---------------------


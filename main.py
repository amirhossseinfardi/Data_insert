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
new_product = '//*[@id="main_view"]/div/div/div[2]/a'
s.driver.ensure_element_by_xpath(new_product,
                                 state='clickable',
                                 timeout=10).ensure_click()
time.sleep(10)
# ---------------------- product detail ( جزییات محصولات ) ----------------
product_name_xpath = '//*[@id="product_modify_title_control_farsi"]'
product_name = 'امیرحسین'
s.driver.ensure_element_by_xpath(product_name_xpath, timeout=10).send_keys(product_name)

open_category_menu = '//*[@id="page_content_inner"]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[1]'
s.driver.ensure_element_by_xpath(open_category_menu,
                                 timeout=10).ensure_click()
select_category = '//*[@id="page_content_inner"]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/div[11]'
s.driver.ensure_element_by_xpath(select_category,
                                 timeout=10).ensure_click()

# ---------------------- price and availability ( قیمت و موجودی ) ----------------
price_title_xpath = '//*[@id="product_modify_package_title_control"]'
price_title = 'قیمت کل'
s.driver.ensure_element_by_xpath(price_title_xpath, timeout=10).send_keys(price_title)

price_detail_xpath = '//*[@id="product_modify_package_title_per_control"]'
price_detail = 'قیمت جز'
s.driver.ensure_element_by_xpath(price_detail_xpath, timeout=10).send_keys(price_detail)

inquiry = True

if inquiry:
    inquiry_click_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/span'
    s.driver.ensure_element_by_xpath(inquiry_click_xpath,
                                     timeout=10).ensure_click()
    maximum_order_xpath = '//*[@id="pkg_max_order_0"]'
    maximum_order = 20
    s.driver.ensure_element_by_xpath(maximum_order_xpath, timeout=10).send_keys(maximum_order)

inventory_xpath = '//*[@id="product_modify_quantity_control"]'
inventory_value = '1000'
s.driver.ensure_element_by_xpath(inventory_xpath, timeout=10).send_keys(inventory_value)




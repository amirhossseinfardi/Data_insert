#
#
from selenium import webdriver
from requestium import Session, Keys

# initialize chrome
s = Session(webdriver_path=r'C:\chromedriver\chromedriver.exe',
            browser='chrome',
            default_timeout=15)

# go to kaalaak.com
s.driver.get('https://www.kaalaak.com')

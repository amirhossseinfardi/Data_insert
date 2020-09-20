import pandas as pd
from requestium import Session, Keys
import time

# initialize chrome
s = Session(webdriver_path=r'C:\chromedriver\chromedriver.exe',
            browser='chrome',
            default_timeout=15,
            )
s.driver.maximize_window()

url = 'https://www.skf.com/group/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings'

s.driver.get(url)
time.sleep(10)
data_table = pd.read_html(s.driver.page_source,
                          skiprows=1)[0]
print(data_table)

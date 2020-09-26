from requestium import Session, Keys
import time
from insert_function import insertSelectableValue
from insert_function import insertValue
from insert_function import insertSelectImage

def insertData(df_insert_data):
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
    time.sleep(1)
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

    # ------------ end of static content ------------

    # ------------ select category --------------

    open_category_list = '/html/body/div[5]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]'
    # open_category_list1 = '//*[@id="page_heading"]/div/div[1]/div/div[1]/input'
    s.driver.ensure_element_by_xpath(open_category_list,
                                     state='clickable',
                                     timeout=10).ensure_click()

    # select bearing deep groove
    unit_temp = '/html/body/div[5]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[153]'
    s.driver.ensure_element_by_xpath(unit_temp,
                                     timeout=10).ensure_click()
    time.sleep(1)
    s.driver.switch_to_active_element().send_keys(Keys.ESCAPE)

    df_data = df_insert_data
    count = 0

    for index, rows in df_data.iterrows():

        # select main product to copy based on sealing by SKU ID
        Z_series = ['Z', 'ZZ', '2Z']
        RS_series = ['RS']
        ZNR = ['ZNR']
        ZNR_seal = False
        TN_series = ['TN']
        TN_cage = False
        if any(x in rows.trade_name for x in ZNR):
            select_sku = 41030101009
            material = 'فلزی'
            seal = True
            ZNR_seal = True
        elif any(x in rows.trade_name for x in TN_series):
            select_sku = 41030101009
            material = 'فلزی'
            seal = True
            TN_cage = True
        elif any(x in rows.trade_name for x in RS_series):
            select_sku = 41030101009
            material = 'نیتریل'
            seal = True
        elif any(x in rows.trade_name for x in Z_series):
            select_sku = 41030101009
            material = 'فلزی'
            seal = True
        else:
            select_sku = 41030101003
            seal = False
        select_sku_xpath = '//*[@id="product_list_search"]'
        s.driver.ensure_element_by_xpath(select_sku_xpath, timeout=20).clear()
        s.driver.ensure_element_by_xpath(select_sku_xpath, timeout=20).send_keys(select_sku)
        time.sleep(3)

        # copy and duplicate product
        old_product_xpath = '//*[@id="product_list"]/div/div/div[1]/div[1]/i'
        old_product_xpath1 = '/html/body/div[5]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div/ul/li[1]/a'
        s.driver.ensure_element_by_xpath(old_product_xpath,
                                         timeout=10).ensure_click()
        s.driver.ensure_element_by_xpath(old_product_xpath1,
                                         state='clickable',
                                         timeout=10).ensure_click()
        time.sleep(10)
        # -------------- insert part as function---------------

        # --------------------   insert name
        insertSelectableValue(2, rows.trade_name, s)

        # ---------------------- insert ID
        insertValue(5, rows.ID, s)

        # -------------------------- insert ID_TOL
        insertValue(6, rows.ID_Tol, s)

        # -------------------------- insert OD
        insertValue(7, rows.OD, s)

        # --------------------------- insert OD_Tol
        insertValue(8, rows.OD_Tol, s)

        # ---------------------------- width
        insertValue(9, rows.width, s)

        # ---------------------------- dynamic load
        insertValue(12, rows.dynamic, s)

        # ---------------------------- static load
        insertValue(13, rows.static, s)

        # ---------------------------- rpm
        insertValue(14, rows.rpm, s)

        # ----------------------------- seal
        if seal:
            insertSelectableValue(20, material, s)

        # ---------------------- khardar ZNR
        if ZNR_seal:
            insertSelectImage(3, 3, s)

        # ------------------ cage material
        if TN_cage:
            match_text = 'فایبر گلس تقویت شده'
            insertSelectableValue(19, match_text, s)

        # -------------- save and exit
        exit_menu_xpath = '//*[@id="pmf"]/div[3]/a'
        s.driver.ensure_element_by_xpath(exit_menu_xpath,
                                         timeout=10).ensure_click()
        time.sleep(1)
        exit_path = '//*[@id="pmf"]/div[3]/div/button[2]'
        s.driver.ensure_element_by_xpath(exit_path,
                                         timeout=10).ensure_click()
        count = count + 1
        print(count)
        time.sleep(10)

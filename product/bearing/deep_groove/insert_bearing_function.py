#
#
from selenium import webdriver
from requestium import Session, Keys
import time
import pandas as pd


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

    # select categoty

    open_category_list = '/html/body/div[5]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]'
    # open_category_list1 = '//*[@id="page_heading"]/div/div[1]/div/div[1]/input'
    s.driver.ensure_element_by_xpath(open_category_list,
                                     state='clickable',
                                     timeout=10).ensure_click()

    # select bearing deep groove
    unit_temp = '/html/body/div[5]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[151]'
    s.driver.ensure_element_by_xpath(unit_temp,
                                     timeout=10).ensure_click()
    time.sleep(1)
    s.driver.switch_to_active_element().send_keys(Keys.ESCAPE)

    # print('little sleep')
    # time.sleep(4)
    #
    # s.driver.ensure_element_by_xpath(open_category_list1,
    #                                  timeout=10).send_keys(Keys.BACKSPACE)
    # print('sleep again')
    # time.sleep(4)
    # s.driver.ensure_element_by_xpath(unit_temp,
    #                                  timeout=10).ensure_click()
    # print('sleep')
    # time.sleep(4)
    # s.driver.switch_to_active_element().send_keys(Keys.ESCAPE)

    # df_data = pd.read_excel('data.xlsx')
    df_data = df_insert_data
    # print(df_data)
    # time.sleep(60)
    count = 0
    for index, rows in df_data.iterrows():

        # select main product to copy based on sealing
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

        # --------------------   insert name
        text_menu_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/' \
                          'div[3]/div[2]/div/div[2]/div/div/div/div[1]'
        s.driver.ensure_element_by_xpath(text_menu_xpath,
                                         timeout=20).ensure_click()
        # text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]'
        # s.driver.ensure_element_by_xpath(text_xpath,
        #                                  timeout=10).ensure_click()
        match_text = rows.trade_name
        remove_text = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div[1]/input'
        s.driver.ensure_element_by_xpath(remove_text,
                                         timeout=10).send_keys(Keys.BACKSPACE)
        try:
            text_xpath = '//*[text()="{temp}"]'.format(temp=match_text)
            # print(text_xpath)
            s.driver.ensure_element_by_xpath(text_xpath,
                                             timeout=5).ensure_click()
            print('no predefine value')
        except:
            add_text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]' \
                             '/div[2]/div/div[2]/div/div/div/div[2]/div/div'
            # div[1]/input to div[2]/div/div
            text_input = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/div[1]/input'
            s.driver.ensure_element_by_xpath(text_input, timeout=10).send_keys(match_text)
            time.sleep(0.5)
            s.driver.ensure_element_by_xpath(add_text_xpath,
                                             timeout=10).ensure_click()
            print('new value added')

        # ---------------------- insert ID
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[5]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.ID
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # unit_menu_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[5]/div/div[2]/div/div/div[2]/select'
        # unit_value = 'mm'
        # unit_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[5]/div/div[2]' \
        #              '/div/div/div[2]/select/option[contains(text(),"{temp}")]'.format(temp=unit_value)
        # print(unit_xpath)
        # s.driver.ensure_element_by_xpath(unit_menu_xpath,
        #                                  timeout=10).ensure_click()
        # time.sleep(0.5)
        # temp_unit = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[5]/
        # div/div[2]/div/div/div[2]/select/option[2]'
        # s.driver.ensure_element_by_xpath(unit_xpath,
        #                                  timeout=10).ensure_click()

        # -------------------------- insert ID_TOL
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[6]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.ID_Tol
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # -------------------------- insert OD
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[7]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.OD
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # --------------------------- insert OD_Tol
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[8]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.OD_Tol
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # ---------------------------- width
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[9]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.width
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # ---------------------------- dynamic load
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[12]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.dynamic
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # ---------------------------- static load
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[13]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.static
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(value_input))

        # ---------------------------- rpm
        value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                            '/div[14]/div/div[2]/div/div/div[1]/div/input'
        value_input = rows.rpm
        print(type(value_input))
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
        if isinstance(value_input, (int, float)):
            s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(int(value_input)))
        else:
            s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(value_input)

        # ----------------------------- seal
        if seal:
            text_menu_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[20]/div/div[2]/div/div/div/div[1]'
            s.driver.ensure_element_by_xpath(text_menu_xpath,
                                             timeout=20).ensure_click()
            # text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]
            # /div/div[2]/div/div/div/div[2]/div/div[1]'
            # s.driver.ensure_element_by_xpath(text_xpath,
            #                                  timeout=10).ensure_click()
            match_text = material
            remove_text = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[20]/div/div[2]/div/div/div/div[1]/input'
            s.driver.ensure_element_by_xpath(remove_text,
                                             timeout=10).send_keys(Keys.BACKSPACE)
            try:
                text_xpath = '//*[text()="{temp}"]'.format(temp=match_text)
                print(text_xpath)
                s.driver.ensure_element_by_xpath(text_xpath,
                                                 timeout=5).ensure_click()
                print('predefine value')
            except:
                add_text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]' \
                                 '/div[20]/div/div[2]/div/div/div/div[2]/div/div'
                # div[1]/input to div[2]/div/div
                text_input = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[20]/div/div[2]/' \
                             'div/div/div/div[1]/input'
                s.driver.ensure_element_by_xpath(text_input, timeout=10).send_keys(match_text)
                time.sleep(0.5)
                s.driver.ensure_element_by_xpath(add_text_xpath,
                                                 timeout=10).ensure_click()
                print('new material added')

        # ---------------------- khardar ZNR
        if ZNR_seal:
            khardar_image_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[3]/div/' \
                                  'div[2]/div/div/label[3]'
            s.driver.ensure_element_by_xpath(khardar_image_xpath,
                                             timeout=10).ensure_click()

        # ------------------ cage material
        if TN_cage:
            text_menu_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[19]/div/div[2]/div/div/div/div[1]'
            s.driver.ensure_element_by_xpath(text_menu_xpath,
                                             timeout=20).ensure_click()
            # text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]
            # /div/div[2]/div/div/div/div[2]/div/div[1]'
            # s.driver.ensure_element_by_xpath(text_xpath,
            #                                  timeout=10).ensure_click()
            match_text = 'فایبر گلس تقویت شده'
            remove_text = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[19]/div/div[2]/div/div/div/div[1]/input'
            s.driver.ensure_element_by_xpath(remove_text,
                                             timeout=10).send_keys(Keys.BACKSPACE)
            try:
                text_xpath = '//*[text()="{temp}"]'.format(temp=match_text)
                print(text_xpath)
                s.driver.ensure_element_by_xpath(text_xpath,
                                                 timeout=5).ensure_click()
                print('predefine value')
            except:
                add_text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]' \
                                 '/div[19]/div/div[2]/div/div/div/div[2]/div/div'
                # div[1]/input to div[2]/div/div
                text_input = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[19]/div/div[2]/' \
                             'div/div/div/div[1]/input'
                s.driver.ensure_element_by_xpath(text_input, timeout=10).send_keys(match_text)
                time.sleep(0.5)
                s.driver.ensure_element_by_xpath(add_text_xpath,
                                                 timeout=10).ensure_click()
                print('new cage added')
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

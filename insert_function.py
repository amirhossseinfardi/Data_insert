from requestium import Session, Keys
import time


def insertSelectableValue(n, parameter, s):
    filter_place = n
    text_menu_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[{}]' \
                      '/div/div[2]/div/div/div/div[1]'.format(filter_place)

    s.driver.ensure_element_by_xpath(text_menu_xpath,
                                     timeout=20).ensure_click()
    # text_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[2]
    # /div/div[2]/div/div/div/div[2]/div/div[1]'
    # s.driver.ensure_element_by_xpath(text_xpath,
    #                                  timeout=10).ensure_click()
    match_text = parameter
    remove_text = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[{}]' \
                  '/div/div[2]/div/div/div/div[1]/input'.format(filter_place)
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
                         '/div[{}]/div/div[2]/div/div/div/div[2]/div/div'.format(filter_place)

        text_input = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[{}]/div/div[2]/' \
                     'div/div/div/div[1]/input'.format(filter_place)
        s.driver.ensure_element_by_xpath(text_input, timeout=10).send_keys(match_text)
        time.sleep(0.5)
        s.driver.ensure_element_by_xpath(add_text_xpath,
                                         timeout=10).ensure_click()
        print('new value added')


def insertValue(n, parameter, s):
    filter_place = n
    value_input_xpath = '/html/body/div[5]/div/div/div[1]/form/div[2]/div/div[2]/div[3]' \
                        '/div[{}]/div/div[2]/div/div/div[1]/div/input'.format(filter_place)
    value_input = parameter
    s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).clear()
    if isinstance(value_input, (int, float)):
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(str(int(value_input)))
    else:
        s.driver.ensure_element_by_xpath(value_input_xpath, timeout=10).send_keys(value_input)


def insertSelectImage(n, parameter, s):
    filter_place = n
    image_xpath = '//*[@id="page_content_inner"]/div/div[2]/div[3]/div[{temp_filter_place}]/div/' \
                  'div[2]/div/div/label[{image_place}]'.format(image_place=parameter,
                                                               temp_filter_place=filter_place)
    s.driver.ensure_element_by_xpath(image_xpath,
                                     timeout=10).ensure_click()

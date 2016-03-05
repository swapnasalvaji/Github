from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,datetime
'''
g= webdriver.Chrome('/Users/Swapna/Downloads/chromedriver')
g.get("https://www.google.com/")
g.close()
'''
f= webdriver.Firefox()
f.get("https://www.google.com/")
f.find_element_by_name('q').is_displayed()
if f:
    f.find_element_by_name('q').send_keys('weather')
    f.find_element_by_name('btnG').click()
    try:
        f.find_element_by_css_selector('[href=https://www.weather.com]').click()

    except BaseException as e:
        print('exception ',e)


    time.sleep(5)
    f.close()

else:
    f.close()

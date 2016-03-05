from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time , datetime
f=webdriver.Firefox()
f.get("https://www.gmail.com")
f.find_element_by_name('Email').send_keys('swapnas.cute')
f.find_element_by_name('signIn').click()
time.sleep(2)
f.find_element_by_name('Passwd').send_keys('sappudu461461')
#time.sleep(2)
f.find_element_by_id('signIn').click()
time.sleep(5)
f.close()
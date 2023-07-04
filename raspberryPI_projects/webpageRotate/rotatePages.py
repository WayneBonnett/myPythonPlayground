import time
from selenium import webdriver

driver=webdriver.Edge()
#driver.manage().window().maximize()
driver.get('https://google.com')
driver.maximize_window()
# wait a while, and then go to another page
time.sleep(5)
driver.get('https://cnbc.com')
time.sleep(5)
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import random
import time
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)

# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element(By.ID,'session_key')

# send_keys() to simulate key strokes
username.send_keys('mahexh007@gmail.com')

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element(By.ID,'session_password')

# send_keys() to simulate key strokes
password.send_keys('M4h3xh@2001')
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element(By.XPATH,'//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()
sleep(10)





Jobdata = []
lnks = []
for x in range(0,100,10):
    driver.get(f'https://www.google.com/search?q=site:linkedin.com/in/+AND+%22Python+Developer%22+AND+%22Delhi%22&rlz=1C1CHZO_enIN1023IN1023&ei=jPaIY-mEGM6cseMPyZaNmAo&start={x}')
    time.sleep(random.uniform(2.5, 4.9))
    linkedin_urls = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
    lnks.append(linkedin_urls)
    
for x in lnks:
    for i in x:

        # get the profile URL
        driver.get(i)
        sleep(5)
        try:
            connect1 = driver.find_element(By.XPATH,'//li-icon[@type = "connect"]')
            connect1.click()
        except:
            pass
        connect = driver.find_element(By.XPATH,'//div[@class="ml7 mt1 pl3"]')
        connect.click()
        sleep(5)
        send = driver.find_element(By.XPATH,'//button[@aria-label = "Send now"]')
        send.click()
        sleep(2)
        
driver.quit()


# In[ ]:





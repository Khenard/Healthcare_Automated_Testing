from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess
import time, random
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
import ctypes
import pyautogui, sys
import autoit
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Declare as variable the data xlsx file - put it on the same folder as the project
datafile = os.getcwd()+"\data.xlsx" 
# Declare excel data as variable and set the first column to ID
excel_data = pd.read_excel(datafile)
#age = pd.DataFrame(excel_data, columns =['NAME'])
#convert column data to array list and use it to select random values
colname = excel_data['NAME'].tolist()
print(colname)
name_random = random.choice(colname)
    
servers.qaserver()
config.driver.get("https://qado.medisource.com/patients/admitted")
time.sleep(5) 
stb = config.driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys(name_random)









# END TEST
 
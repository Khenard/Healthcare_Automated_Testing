from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes  # An included library with Python install. 


servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/DBBB3F9A-0D1D-495E-87DC-DAB0CE6B3124/93C9DC38-3BC3-4ACE-ABAC-AA5CB5EB2564/overview")
time.sleep(2)   



# Function to get test information and put it as first comment box - OASIS 
sysinfo = config.systeminfo()

commenticon = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[8]/div/div/div/a/i').click()
time.sleep(3)
commentbox = config.driver.find_element_by_xpath('/html/body//textarea[@placeholder="Comments here"]')
commentbox.click()
commentbox.send_keys(sysinfo)
time.sleep(3)
commentsave = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Send")]').click()

#currentpage = config.driver.current_url








# END TEST
 
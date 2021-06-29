from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes
import pyautogui, sys
from _socket import close
from autoit import process


servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/E2B75EF7-0338-48A6-861A-629BADEB0008/BE8D6183-82BC-4C73-ABC2-3677C533C333/overview")
time.sleep(2)   

task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')

taskstatus = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[3]/div/span').text
print(taskstatus)

if taskstatus == "In Progress":
    task.click()
    time.sleep(3)
    editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click() #edit button
    time.sleep(3)
        
elif taskstatus == "Scheduled":
    task.click()
    time.sleep(3)
    
#editbtn = config.driver.get('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click()
integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]').click()


# END TEST
 
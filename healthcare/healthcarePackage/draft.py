from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess
import time
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
    
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/CEB7010B-2FE7-45B1-808C-3C25C0E594F0/857A6F1E-C5A3-415E-92FC-879D983FAA2F/overview")
time.sleep(2)  
 
complete_woundprocess.complete_woundprocess()

# END TEST
 
from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task, test_unit, test_main
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes  # An included library with Python install. 
import pymsgbox



chooseserver = pymsgbox.prompt('Choose server for the Automated Test: \n \n Type: "live" or "qa"', 'Healthcare Automation')
testcase = pymsgbox.prompt('Choose Test Case: \n \n Type: \n "1" for test_main.py \n "2" for test_unit.py', 'Healthcare Automation')
    
if chooseserver == "live":
    testserver = "live"
    if testcase == "1":
        test_main.test_main(testserver)
    elif testcase == "2":
        test_unit.test_unit(testserver)
        
elif chooseserver == "qa":
    testserver = "qa"
    
    if testcase == "1":
        test_main.test_main(testserver)
    elif testcase == "2":
        test_unit.test_unit(testserver)
    

    









# END TEST
 
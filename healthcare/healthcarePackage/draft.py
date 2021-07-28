from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess, function_human_resources, function_medical_resources
import random, os, pyautogui, sys, autoit, ctypes
import time
import pymsgbox
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import random
from selenium.webdriver.common.action_chains import ActionChains



# Hospital
servers.qaserver()
config.driver.get("https://qado.medisource.com/physicians")
time.sleep(3)

"""num = pymsgbox.prompt('How many records to add?', 'Healthcare Automation')
num = int(num)       
# Specify the numbers of hospital to be added
for x in range(num):"""

function_medical_resources.addphysician()












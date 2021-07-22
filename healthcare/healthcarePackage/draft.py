from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess, function_authorization
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

# Useful variables from config.py
todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
name_random = config.randomize_name()
ssn = config.randomize_ssn()
today = date.today()
todaynow = today.strftime("%m/%d/%Y")   

days_range = 30 # Number of days the authorization would last
# Set number of authorized visit(s)
rn = 5
lvn = 2
pt = 2
st = 2
ot = 2
msw = 1
hha = 1

servers.qaserver()
config.driver.get("https://qado.medisource.com/patient")
time.sleep(2)

# Patient Admission
function_admission.preadmission_nonmed_auth(
    todaynow,
    todaytime,
    todaynow,
    str(name_random),
    "Automated",
    "NM",
    "02/07/1997",
    "Male",
    "Single",
    "American", 
    "english",
    ssn,
    "17 Peachtree St, Charleston, MS, 38921",
    "Blue Building",
    "17 Peachtree St",
    "Charleston",
    "MS",
    "38921",
    "8593603818",
    "6626472513",
    "automatedpatient@mailinator.com",
    "Ken Figuracion",
    "8593603818",
    "Catherine Balanag",
    "Wife",
    "8593603818",
    "6626472513",
    "01/01/2018",
    "02/01/2018",
    "Colon and Rectal Surgery",
    "Peanut",
    "RN"
    )

# Authorization Page
function_authorization.new_auth(
    str(name_random),
    days_range,
    rn,
    lvn,
    pt, 
    st,
    ot,
    msw,
    hha
    )

print('Test success!')   
pymsgbox.alert('Test Success!', 'Success')
config.driver.close()
    


# END TEST
 
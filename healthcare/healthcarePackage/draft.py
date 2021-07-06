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
config.driver.get("https://qado.medisource.com/patientcare/85183C5B-5A9B-482B-80A9-63F3670BF711/510A4E92-D238-434A-B342-9B0A6B255847/overview")
time.sleep(2)  

woundtype = "Pressure Ulcer"
#woundlocation = ['Buttock (R)', 'Buttock (L)', 'Sacrum', 'Coccyx', 'Trochanter (R)', 'Trochanter (L)', 'Ischial tuberosity (R)', 'Ischial tuberosity (L)', 'Lateral ankle (R)', 'Lateral ankle (L)', 'Medial ankle (R)', 'Medial ankle (L)', 'Heel (R)', 'Heel (L)', 'Plantar', 'Toes', 'Abdomen', 'Groin']
woundlocation = 'Sacrum'
stages = "2"
grantissue = "3"
nectissue = "3"
granneccoverage = "4"
exuamount = "4"
exutype = "Serous"
edges = "2"
periwoundtissue = "Edematous"
healingstatus = "Early/partial granulation"
woundrelatedpain = "4"


function_woundprocess.addwounddirectly(
        woundtype,
        woundlocation,
        stages, 
        grantissue, 
        nectissue, 
        granneccoverage, 
        exuamount, 
        exutype, 
        edges, 
        periwoundtissue, 
        healingstatus, 
        woundrelatedpain
        )









# END TEST
 
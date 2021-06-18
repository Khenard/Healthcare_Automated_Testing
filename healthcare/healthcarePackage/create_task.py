from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task
import random, time
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


def create_task(task):
    t = task
    time.sleep(3)
    
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
    
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    print(t)
    
    for x in t:
        print(x)
        if (((x == "RN - Skilled Assessment" or x == "RN - OASIS D1 Discharge from Agency") or (x == "RN - OASIS D1 Discharge Non-visit" or x == "RN - OASIS D1 Other Follow-Up")) or (x == "RN - OASIS D1 Transfer (discharged)" or x == "RN - OASIS D1 Transfer (not discharged)")):
            function_create_task.oasis(x)
        else:
            function_create_task.snv(x)
        time.sleep(5)
    
        
    time.sleep(2)
    
    
  

from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task
import random, time
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


def create_task():

    time.sleep(3)
    
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
    
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_create_task.newtask("RN - Wound Visit")
    
    
  

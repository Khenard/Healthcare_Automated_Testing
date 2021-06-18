from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import os
import time
from datetime import date


#Configure web driver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)

def timenow():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print(current_time)
    return current_time

def datenow():
    today = date.today()
    todaynow = today.strftime("%m/%d/%Y")
    print(todaynow)
    return todaynow




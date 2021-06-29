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
config.driver.get("https://qado.medisource.com/patient")
time.sleep(2)   

skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button
primary_insurance = config.driver.find_element_by_css_selector("#primary_insurance_chosen > .chosen-single")
primary_insurance.click()
primary_insurancedd = config.driver.find_element_by_xpath('//*[@id="primary_insurance_chosen"]/div/div/input')
primary_insurancedd.send_keys('other', Keys.ENTER)

#currentpage = config.driver.current_url








# END TEST
 
from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_human_resources
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


# Select discipline and title
sn = 'Skilled Nurse (SN)'
sn_rn = 'Registered Nurse (RN)'
sn_lvn = 'Licensed Vocational Nurse (LVN) / Licensed Practical Nurse (LPN) '

hha = 'Home Health Aide (HHA)'
hha_chha = 'Certified Home Health Aide (CHHA)'

pt = 'Physical Therapist (PT)'
pt_pt = 'Physical Therapist (PT)'
pt_pta = 'Physical Therapist Assistant(PTA)'

ot = 'Occupational Therapist (OT)'
ot_ot = 'Occupational Therapist (OT)'
ot_ota = 'Occupational Therapist Assistant (OTA)'


st = 'Speech Therapist (ST)'
st_st = 'Speech Therapist Assistant (ST)'
st_sta = 'Speech-language pathologist (SLP)'

msw = 'Medical Social Work (MSW)'
msw_msw = 'Medical Social Worker (MSW)'
msw_lcsw = 'Licensed Clinical Social Worker (LCSW)'

# Choose final option
discipline = sn
title = sn_rn

#randomize options
language1 = ['English', 'Chinese', 'Filipino', 'French', 'German', 'Hebrew', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Malaysian', 'Russian', 'Spanish', 'Vietnamese', 'Unknown']
language = random.choice(language1) 
level1 = ['Fluent', 'Intermediate', 'Elementary', 'Unable to talk']
level = random.choice(level1) 

userole = 'Administrator'


servers.qaserver()
config.driver.get("https://qado.medisource.com/personnels/create")
time.sleep(2)

# Tabs
personalinfo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[1]/a')
profcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[2]/a')
healthcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[3]/a')

# Personal Information
function_human_resources.personalinfo(
    'Automated',
    '02/07/1997',
    'Asian',
    'Single',
    discipline,
    title,
    'Direct Hire',
    'Administrator',
    'Medisource, LLC.',
    '8982 Portage Pointe Dr #B, Streetsboro, OH, 44241',
    language,
    level
    )   
function_human_resources.professionalcreds() # Profressional Credentials
function_human_resources.healthcreds() # Health Credentials
function_human_resources.systemaccount(userole) # System Account

#servers.logout() # Logout

p = config.driver.current_window_handle # Get the current window
parent = config.driver.window_handles[0]

# Lets open google.com in the first tab
config.driver.maximize_window()
creds = function_human_resources.gotomailinator(useremail) #Get the return values of username and password from the mailinator
username = creds[0]
userpass = creds[1]
    
time.sleep(3)

config.driver.execute_script("window.open('about:blank','secondtab');")
config.driver.switch_to.window("secondtab")
config.driver.get('https://qado.medisource.com/login')

chld = config.driver.window_handles[1]
time.sleep(3)
    
login.login(username, userpass)
time.sleep(3)
    
    
config.driver.switch_to.window(parent) # Switch to first tab
     
backtoinbox = config.driver.find_element_by_xpath('//*[@id="email_pane"]/div/div[1]/div[2]/a').click()
time.sleep(3)

inbox1 = config.driver.find_element_by_xpath('/html/body/div/main/div[2]/div[3]/div/div[4]/div/div/table/tbody/tr/td[2]').click()
time.sleep(3)

config.driver.switch_to.frame(config.driver.find_element_by_id('html_msg_body'))

verificationcode = config.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[2]/td').text
print(verificationcode)
time.sleep(3)
    
config.driver.switch_to.window(chld) # Switch back to the 2nd tab
     
time.sleep(3)
verifycode = config.driver.find_element_by_xpath('//*[@id="token"]').send_keys(verificationcode)
verifybtn = config.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/form/div[4]/button').click()
    

  
  
function_human_resources.accountsecurity(
    userpass,
    'testtest',
    'Tester2021!'
    )




# Redirects to Mailinator
#function_human_resources.gotomailinator() 













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


servers.liveserver()
config.driver.get("https://app.medisource.com/personnels/create")
time.sleep(2)

# Tabs
personalinfo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[1]/a')
profcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[2]/a')
healthcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[3]/a')

"""# Personal Information 
fname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[1]/td[2]/div/input').send_keys(name_random)
lname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[2]/td[2]/div/input').send_keys('Automated')
gender_m = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//label[1]/input').click()
bdate = config.driver.find_element_by_xpath('//*[@id="birthdate"]').send_keys('02/07/1997')

ethdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a').click()
ethtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/div/div/input').send_keys('Asian', Keys.ENTER)

maritalstatdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/a').click()
maritalstattb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/div/div/input').send_keys('Single', Keys.ENTER)

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


disciplinedd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/a').click()
disciplinetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/div/div/input').send_keys(discipline, Keys.ENTER)

titledd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/a').click()
titletb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/div/div/input').send_keys(title, Keys.ENTER)

hirecategdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/a').click()
hirecategtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/div/div/input').send_keys('Direct Hire', Keys.ENTER)

positiondd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/a').click()
positiontb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/div/div/input').send_keys('Administrator', Keys.ENTER)

ssntb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[13]/td[2]/div/input').send_keys(ssn)
clinicianid = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[14]/td[2]/div/input').send_keys(ssn)
company = config.driver.find_element_by_name('company').send_keys('Medisource, LLC.')
address = config.driver.find_element_by_name('address1').send_keys('8982 Portage Pointe Dr #B, Streetsboro, OH, 44241')

scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")

phone = config.driver.find_element_by_name('phone').send_keys(ssn)
emailtb = config.driver.find_element_by_name('email').send_keys(name_random + '@mailinator.com')
hireddate = config.driver.find_element_by_id('hireddate').send_keys(todaynow)


taskdateconvert = datetime.strptime(todaynow, '%m/%d/%Y') #2. Convert to date string
addeddaystodate = timedelta(days=1000) #3. Add days to the date
datetotal = taskdateconvert + addeddaystodate #4. add total
finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date  
print(finaltaskdate)

time.sleep(2)

terminationdate = config.driver.find_element_by_id('terminationdate').send_keys(finaltaskdate)

for x in range(2):
    print(x)
    

for x in range(1,5):
    for y in range(2,4):
        langdd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/a').click()
        langtb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/div/div/input').send_keys('English', Keys.ENTER)
        dd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/a').click()
        tb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/div/div/input').send_keys('Fluent', Keys.ENTER)
        
scrollup= config.driver.execute_script("window.scrollTo(0,0)")"""
 
 
 
profcreds.click()
time.sleep(3)

for x in range(2,11):
    print(x)
    
    l = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
    l21 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
    l2 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/input').send_keys('No', Keys.ENTER)
     
 

 
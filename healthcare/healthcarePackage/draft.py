from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess, function_human_resources
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


"""useremail = 'Wynona@mailinator.com'
config.driver.maximize_window()
function_human_resources.gotomailinator(useremail)"""








# Useful variables from config.py
todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
name_random = config.randomize_name()
ssn = config.randomize_ssn()
today = date.today()
todaynow = today.strftime("%m/%d/%Y")   

taskdateconvert = datetime.strptime(todaynow, '%m/%d/%Y') #2. Convert to date string
addeddaystodate = timedelta(days=1000) #3. Add days to the date
datetotal = taskdateconvert + addeddaystodate #4. add total
finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date  
print(finaltaskdate)

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


# ----------------------------------------------------------

servers.liveserver()
config.driver.get("https://app.medisource.com/personnels/create")
time.sleep(2)


# Tabs
personalinfo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[1]/a')
profcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[2]/a')
healthcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[3]/a')


# ----------------------------------------------------------
# Personal Information 
# ----------------------------------------------------------
fname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[1]/td[2]/div/input').send_keys(name_random)
lname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[2]/td[2]/div/input').send_keys('Automated')
gender_m = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//label[1]/input').click()
bdate = config.driver.find_element_by_xpath('//*[@id="birthdate"]').send_keys('02/07/1997')

ethdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a').click()
ethtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/div/div/input').send_keys('Asian', Keys.ENTER)

maritalstatdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/a').click()
maritalstattb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/div/div/input').send_keys('Single', Keys.ENTER)


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
time.sleep(2)
phone = config.driver.find_element_by_name('phone').send_keys(ssn)
emailtb = config.driver.find_element_by_name('email').send_keys(name_random + '@mailinator.com')
hireddate = config.driver.find_element_by_id('hireddate').send_keys(todaynow)

terminationdate = config.driver.find_element_by_id('terminationdate').send_keys(finaltaskdate)

for x in range(1,5):
    for y in range(2,4):
        
        #randomize options
        language1 = ['English', 'Chinese', 'Filipino', 'French', 'German', 'Hebrew', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Malaysian', 'Russian', 'Spanish', 'Vietnamese', 'Unknown']
        language = random.choice(language1) 
        langdd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/a').click()
        langtb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/div/div/input').send_keys(language, Keys.ENTER)
        
        level1 = ['Fluent', 'Intermediate', 'Elementary', 'Unable to talk']
        level = random.choice(level1) 
        dd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/a').click()
        tb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/div/div/input').send_keys(level, Keys.ENTER)
        
scrollup= config.driver.execute_script("window.scrollTo(0,0)")

# ----------------------------------------------------------
# Professional Credentials
# ----------------------------------------------------------
time.sleep(3)
profcreds.click()

profid = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr[1]/td[3]/div/input').send_keys(ssn)
proeffdate = config.driver.find_element_by_xpath('//*[@id="efdateu0"]').send_keys(todaynow)
proexpdate = config.driver.find_element_by_xpath('//*[@id="exdate0"]').send_keys(finaltaskdate)
prodatever = config.driver.find_element_by_xpath('//*[@id="verdate0"]').send_keys(todaynow)
proverby = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr[1]/td[7]/div/input').send_keys('Khenard Figuracion')

for x in range(2,11):
    l = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
    l21 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
    no = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/div/ul/li[2]').click()
    
# ----------------------------------------------------------
# Health Credentials
# ----------------------------------------------------------

# Other buttons
savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]')
systemuser_yes = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
systemuser_no = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]')


time.sleep(3)
healthcreds.click()

hc1 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/a').click()
hc2 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/a').click()
hcno = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/div/ul/li[2]').click()
hc3 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/a').click()
hc3 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/a').click()
hcno1 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/div/ul/li[2]').click()

# ----------------------------------------------------------
# Saving
# ----------------------------------------------------------
time.sleep(3)
savebtn.click()
time.sleep(3)
systemuser_yes.click()
time.sleep(5)
discardyes = config.driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/button[1]').click()
# ----------------------------------------------------------
# create user system account
# ----------------------------------------------------------
time.sleep(5)

userole = 'Administrator'

useremail = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[3]/td[2]/div/input').get_attribute('value')
username = useremail.replace('@mailinator.com', '')

usernametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[2]/td[2]/div/input').send_keys(username)
activeuser = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[5]/td[2]/div/ng-form/label[1]/input').click()

# Choose User role
userroledd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[7]/td[2]/div/div/div/a').click()
useroletb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[7]/td[2]/div/div/div/div/div/input').send_keys(userole, Keys.ENTER)

time.sleep(2)     
scroll= config.driver.execute_script("window.scrollTo(0,5000)")

commenttb = config.driver.find_element_by_name('remarks').send_keys('This is entered using automated testing')

time.sleep(2)
saveaccountbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]').click()


"""time.sleep(5)
config.driver.get("https://app.medisource.com/personnels")
time.sleep(2)
searchuser = config.driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys(name_random)
time.sleep(2)"""


# Logout
profileuser = config.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[6]/a').click()
signout = config.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[6]/div/div[2]/div/button[2]').click()

# Go to mailinator.com
config.driver.get("https://www.mailinator.com/")
print(useremail)
mail = config.driver.find_element_by_xpath('//*[@id="addOverlay"]').send_keys(useremail, Keys.ENTER)



 
 
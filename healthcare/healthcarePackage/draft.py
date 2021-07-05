from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes
import pyautogui, sys
from _socket import close
import pyautogui, sys
import autoit

"""servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/E2B75EF7-0338-48A6-861A-629BADEB0008/BE8D6183-82BC-4C73-ABC2-3677C533C333/overview")
time.sleep(2)   

task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')

taskstatus = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[3]/div/span').text
print(taskstatus)

if taskstatus == "In Progress":
    task.click()
    time.sleep(3)
    editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click() #edit button
    time.sleep(3)
        
elif taskstatus == "Scheduled":
    task.click()
    time.sleep(3)
    
#editbtn = config.driver.get('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click()
integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,500)")

time.sleep(3)
woundyes = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/label/input').click()
woundplus =  config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/a').click()
time.sleep(3)

woundtype = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[1]/input')
woundtype.click()
woundtype.send_keys('Pressure Ulcer')
time.sleep(2)

woundloc = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[1]/input')
woundloc.click()
woundloc.send_keys('Buttock (R)')
time.sleep(2)

woundcomment = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[7]/input').send_keys('Added from automated testing.')
time.sleep(2)

savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button[3]').click()
time.sleep(2)

assessnow = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()"""

servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/E2B75EF7-0338-48A6-861A-629BADEB0008/BE8D6183-82BC-4C73-ABC2-3677C533C333/woundcare/update/3FBBD17D-39CE-42E4-9B7E-8906F0E49DD6/1")
time.sleep(3)   

scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")

time.sleep(3)

# --- Click the dropdown
# --- Get all data on dropdown
# --- Select the option

# -- All values declare here
stages = '2'
grantissue = '3'
nectissue = '2'
granneccoverage = '4'
exuamount = '4'
exutype = 'Serous'
edges = '2'
periwoundtissue = 'Edematous'
healingstatus = 'Early/partial granulation'
woundrelatedpain = '4'

# Stages
stages_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//input').click()
stages_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//li[contains(string(), "'+ stages +'")]').click()

time.sleep(2)
"""
# Granulation Tissue
grantissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//input').click()
grantissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//li[contains(string(), "'+ grantissue +'")]').click()

# Necrotic Tissue
nectissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//input').click()
nectissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//li[contains(string(), "'+ nectissue +'")]').click()

# Granulation and Necrosis Coverage
granneccoverage_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//input').click()
granneccoverage_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//li[contains(string(), "'+ granneccoverage +'")]').click()

# Exudate Amount
exuamount_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//input').click()
exuamount_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//li[contains(string(), "'+ exuamount +'")]').click()

# Exudate Type
exutype_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//input').click()
exutype_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//li[contains(string(), "'+ exutype +'")]').click()

# Edge Type
edges_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//input').click()
edges_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//li[contains(string(), "'+ edges +'")]').click()


# Healing Status
healingstatus_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//input').click()
healingstatus_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//li[contains(string(), "'+ healingstatus +'")]').click()

# Wound Related Pain 
woundrelatedpain_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//input').click()
woundrelatedpain_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//li[contains(string(), "'+ woundrelatedpain +'")]').click()


# Periwound Tissue 
periwoundtissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[1]').click()
periwoundtissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]//div[2]').text
time.sleep(2)
finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]//li[contains(string(), "'+ periwoundtissue +'")]').click()
"""
scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")

time.sleep(2)


# Upload Function
# -- 1. find the wound.png file path
# -- 2. Click upload Element
# -- 3. use autoit function for upload -- import autoit

woundimage = os.getcwd()+"\wound.png"

upload = config.driver.find_element(By.XPATH, '//*[@id="myImg"]').click()
time.sleep(2)
autoit.control_set_text("Open","Edit1", woundimage)
autoit.control_send("Open","Edit1","{ENTER}")







# END TEST
 
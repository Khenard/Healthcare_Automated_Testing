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
from autoit import process
import pyautogui, sys


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

stages = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input')
stages.click()
time.sleep(2)  
stages.send_keys('3 = Stage 3: Full thickness tissue loss, subcutaneous fat may be visible but bone, tendon, or muscle is not exposed ')

grantissue = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input')
grantissue.click()
time.sleep(2)  
grantissue.send_keys('3 = Pink, dull, dusky red, hypergranulation')

necrotictissue = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[1]/input')
necrotictissue.click()
time.sleep(2)  
necrotictissue.send_keys('2 = Slough, thin, non-adherent (yellow, tan, gray, green or brown) non-viable tissue')

exuamount = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[1]/input')
exuamount.click()
time.sleep(2)  
exuamount.send_keys('1 = Scant, moist wound tissue, no measurable drainage')

exutype = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]/span/table-inputs/div/div[1]/input')
exutype.click()
time.sleep(2)  
exutype.send_keys('Serosanguineous')

edges = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]/span/table-inputs/div/div[1]/input')
edges.click()
time.sleep(2)  
edges.send_keys('3 = Defined edge, unattached to wound base')

pt = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[1]').click()
time.sleep(2)  
periwoundtissue = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[2]/ul/li[1]').click()

healingstatus = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]/span/table-inputs/div/div[1]/input')
healingstatus.click()
time.sleep(2)  
healingstatus.send_keys('Early/partial granulation')

woundrelatedpain = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]/span/table-inputs/div/div[1]/input')
woundrelatedpain.click()
time.sleep(2)  
woundrelatedpain.send_keys('5')

otherobservation = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[17]/div/textarea').send_keys('sample text goes here...')
time.sleep(2)



def woundcareFunction():
    
    degree = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input')
    degree.click()
    time.sleep(5)
    selectDegree = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[2]/ul/li[2]')
    selectDegree.click()
    time.sleep(5)
    amount = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input')
    amount.click()
    time.sleep(5)
    selectAmount = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[2]/ul/li[6]')
    selectAmount.click()
    time.sleep(5)
    Type = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[1]/input')
    Type.click()
    time.sleep(5)
    selectType = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[2]/ul/li[6]')
    selectType.click()
    time.sleep(5)
    Status = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[1]/input')
    Status.click()
    time.sleep(5)
    selectStatus = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[2]/ul/li[6]')
    selectStatus.click()
    time.sleep(5)
    RelatedPain = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[1]/input')
    RelatedPain.click()
    time.sleep(5)
    selectScore = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[2]/ul/li[7]')
    selectScore.click()
    time.sleep(5)
    
    
def UploadFunction():
    upload = config.driver.find_element(By.XPATH, '//*[@id="myImg"]').click()
    time.sleep(5)
    
def mouseHover():
    
    screenWidth, screenHeight = pyautogui.size()
    time.sleep(5)
    pyautogui.click(410, 274)
    time.sleep(5)
    pyautogui.doubleClick(762, 368)
    time.sleep(5)
    pyautogui.click(540, 392)
    time.sleep(5)
    pyautogui.click(981, 674)
    time.sleep(5)

 

def pressDigitalMeasurement():
    
    digitalclck = config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a')
    digitalclck.click()
    time.sleep(20)
    EditDigitalclck = config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a')
    EditDigitalclck.click()
    time.sleep(5)
    pyautogui.click(1343, 718)
    pyautogui.click(1343, 718)
    pyautogui.click(1343, 718)
    pyautogui.click(1343, 718)
    pyautogui.click(1343, 718)
    time.sleep(5)
    
def WoundMeasurement():
    
    time.sleep(5)
    pyautogui.click(614, 215)
    time.sleep(5)
    pyautogui.click(566, 223)
    time.sleep(5)
    pyautogui.click(504, 247)
    time.sleep(5)
    pyautogui.click(458, 273)
    time.sleep(5)
    pyautogui.click(420, 297)
    time.sleep(5)
    pyautogui.click(393, 334)
    time.sleep(5)
    pyautogui.click(385, 394)
    time.sleep(5)
    pyautogui.click(399, 447)
    time.sleep(5)
    pyautogui.click(424, 487)
    time.sleep(5)
    pyautogui.click(471, 510)
    time.sleep(5)
    pyautogui.click(506, 526)
    time.sleep(5)
    pyautogui.click(555, 535)
    time.sleep(5)
    pyautogui.click(599, 539)
    time.sleep(5)
    pyautogui.click(636, 538)
    time.sleep(5)
    pyautogui.click(680, 526)
    time.sleep(5)
    pyautogui.click(715, 512)
    time.sleep(5)
    pyautogui.click(757, 490)
    time.sleep(5)
    pyautogui.click(810, 452)
    time.sleep(5)
    pyautogui.click(845, 411)
    time.sleep(5)
    pyautogui.click(861, 372)
    time.sleep(5)
    pyautogui.click(855, 327)
    time.sleep(5)
    pyautogui.click(837, 290)
    time.sleep(5)
    pyautogui.click(811, 259)
    time.sleep(5)
    pyautogui.click(768, 234)
    time.sleep(5)
    pyautogui.click(723, 220)
    time.sleep(5)
    pyautogui.click(671, 214)
    time.sleep(5)
    pyautogui.click(614, 215)
    time.sleep(5)
    
def inputGranulation():
    
    X2btn = config.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    percenttb = config.driver.find_element_by_xpath('/html/body/div[12]/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/input[2]')
    percenttb.send_keys("95")
    time.sleep(5)
    pyautogui.click(1339, 124)
    time.sleep(5)
    
def SaveFunction():
    
    save1btn = config.driver.find_element_by_xpath('/html/body/div[12]/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/div[3]/button[2]')
    save1btn.click()
    time.sleep(5)
    config.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    timein = config.driver.find_element_by_xpath('//*[@id="ti"]')
    timein.send_keys("23:00")
    time.sleep(5)
    timein = config.driver.find_element_by_xpath('//*[@id="to"]')
    timein.send_keys("23:30")
    time.sleep(5)
    save2btn = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/td[2]/button')
    save2btn.click()
    time.sleep(5)
    woundtab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[8]')
    woundtab.click()
    time.sleep(5)
    woundHistory = config.driver.find_element_by_xpath('//*[@id="pinid1"]/span/span[1]')
    woundHistory.click()
    time.sleep(5)







# END TEST
 
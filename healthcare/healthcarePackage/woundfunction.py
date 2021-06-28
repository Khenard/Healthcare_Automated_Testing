from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import woundconfig
from importlib.resources import path
import pyautogui, sys
from _socket import close


def loginfunction(un, up):
    
    time.sleep(5)
    usernametb = woundconfig.driver.find_element_by_xpath('//*[@id="loginemail"]').send_keys(un)
    time.sleep(5)
    passwordtb = woundconfig.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(up)
    time.sleep(3)
    loginbtn = woundconfig.driver.find_element_by_xpath('//*[@id="mhLP-ln"]/div[2]/form/div[6]/button')
    loginbtn.click() 
    time.sleep(5)
    
def clicktabsfunction():
    
    time.sleep(3)
    PatientMngr = woundconfig.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[3]')
    PatientMngr.click()
    time.sleep(5)
    patient = woundconfig.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[3]/ul/li[1]/a')
    patient.click()
    time.sleep(5)
    #pageFind = woundconfig.driver.find_element_by_xpath('//*[@id="data-table-command-footer"]/div/div[1]/ul/li[4]')
    #pageFind.click()
    #time.sleep(5)
    patientName = woundconfig.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[11]')
    patientName.click()
    time.sleep(10)
    
def editOasisfunction(comm):
    
    openOasis = woundconfig.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')
    openOasis.click()
    time.sleep(5)
    
   # Xbtn = woundconfig.driver.find_element_by_xpath('//*[@id="closecomments"]')
   #Xbtn.click()
   # time.sleep(5)
    
    #click yung edit button
    X2btn = woundconfig.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    EditOasisbtn = woundconfig.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button')
    EditOasisbtn.click()
    time.sleep(5)
    
    #clicking ng integ tab
    chooseSection = woundconfig.driver.find_element_by_xpath('//*[@id="integumentary"]/div')
    chooseSection.click()
    time.sleep(5)
    
    #click ng wound na checkbox
    checkboxWound = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/label/input')
    checkboxWound.click()
    time.sleep(5)
    
    #click plus sign
    addLabelwound = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/a')
    addLabelwound.click()
    time.sleep(5)
    
    #click yung wound type para labas dropdown
    Woundmenu = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[1]/input')
    Woundmenu.click()
    time.sleep(10)
    
    #namili ng type
    selectWoundType = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[2]/ul/li[9]')
    selectWoundType.click()
    time.sleep(10)
    
    #click mo location dropdwon labas
    location = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[1]/input')
    location.click()
    time.sleep(10)
    
    #namili location
    selectLocation = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[2]/ul/li[3]')
    selectLocation.click()
    time.sleep(10)
    
    #comment 
    commenttb = woundconfig.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[7]/input').send_keys(comm)
    time.sleep(5)
    
    #close kulay green sa taas
    X2btn = woundconfig.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    
    #click save button
    savebtn = woundconfig.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button[3]')
    savebtn.click()
    time.sleep(15)
    
    #assessbtn = woundconfig.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    #assessbtn.click()
    #time.sleep(5)
    
    
def woundcareFunction():  
   
    
    #nirefresh ko lang yung page para makita ko yung woundcare mgmt menu
    woundconfig.driver.refresh();
    time.sleep(20)
    
    
    #click ko yung WOUNDCARE MGMT MENU TAB
    wcareMgmtmenu = woundconfig.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[9]')
    wcareMgmtmenu.click()
    time.sleep(10)

    #click ko yung assessment
    wcareAss = woundconfig.driver.find_element_by_xpath('//*[@id="table-responsive"]/table/tbody[2]/tr/td[2]')
    wcareAss.click()
    time.sleep(10)
    
    #click ko yung EDIT button
    wcareAssEdit = woundconfig.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td[2]/button')
    wcareAssEdit.click()
    time.sleep(10)
    
    #adding ng mga wound parameters
    degree = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input')
    degree.click()
    time.sleep(10)
    selectDegree = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[2]/ul/li[2]')
    selectDegree.click()
    time.sleep(10)
    amount = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input')
    amount.click()
    time.sleep(10)
    selectAmount = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[2]/ul/li[6]')
    selectAmount.click()
    time.sleep(10)
    Type = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[1]/input')
    Type.click()
    time.sleep(10)
    selectType = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[2]/ul/li[6]')
    selectType.click()
    time.sleep(10)
    Status = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[1]/input')
    Status.click()
    time.sleep(10)
    selectStatus = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[2]/ul/li[6]')
    selectStatus.click()
    time.sleep(10)
    RelatedPain = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[1]/input')
    RelatedPain.click()
    time.sleep(10)
    selectScore = woundconfig.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[2]/ul/li[7]')
    selectScore.click()
    time.sleep(10)
    
    ##you should install https://pyautogui.readthedocs.io/en/latest/install.html in order for the module
    #pyautogui.sys to run
    
def UploadFunction():
    upload = woundconfig.driver.find_element(By.XPATH, '//*[@id="myImg"]').click()
    time.sleep(5)
    
  #http://efigureout.com/free-utility-to-locate-mouse-cursor-position/  
def mouseHover():
    
    screenWidth, screenHeight = pyautogui.size()
    time.sleep(5)
    pyautogui.doubleClick(258, 490)
    time.sleep(5)
  

def pressDigitalMeasurement():
    
    
    #Scrolldown
    woundconfig.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    
    digitalclck = woundconfig.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a')
    digitalclck.click()
    time.sleep(20)
    
    #Scrolldown
    #woundconfig.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    EditDigitalclck = woundconfig.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a')
    EditDigitalclck.click()
    time.sleep(10)
    
    
    #pyautogui.click(1343, 718)
    #pyautogui.click(1343, 718)
    #pyautogui.click(1343, 718)
    #pyautogui.click(1343, 718)
    #pyautogui.click(1343, 718)
    #time.sleep(5)
    
def WoundMeasurement():
    
    #dito na yung tracing, used pyautogui
    #for screen resolution 1920 x 1080, pero tawas yung tracing ko :D
    pyautogui.click(911, 309)
    pyautogui.click(789, 326)
    pyautogui.click(711, 349)
    pyautogui.click(638, 383)
    pyautogui.click(574, 437)
    pyautogui.click(554, 480)
    pyautogui.click(555, 532)
    pyautogui.click(566, 576)
    pyautogui.click(589, 626)
    pyautogui.click(649, 669)
    pyautogui.click(779, 707)
    pyautogui.click(923, 711)
    pyautogui.click(1049, 673)
    pyautogui.click(1175, 601)
    pyautogui.click(1230, 528)
    pyautogui.click(1241, 479)
    pyautogui.click(1225, 419)
    pyautogui.click(1180, 370)
    pyautogui.click(1108, 327)
    pyautogui.click(993, 305)
    pyautogui.click(913, 307)
    
    
def inputGranulation():
    
    X2btn = woundconfig.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    percenttb = woundconfig.driver.find_element_by_xpath('/html/body/div[12]/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/input[2]')
    percenttb.send_keys("95")
    time.sleep(5)
    pyautogui.click(1339, 124)
    time.sleep(5)
    
def SaveFunction():
    
    save1btn = woundconfig.driver.find_element_by_xpath('/html/body/div[12]/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/div[3]/button[2]')
    save1btn.click()
    time.sleep(5)
    woundconfig.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    timein = woundconfig.driver.find_element_by_xpath('//*[@id="ti"]')
    timein.send_keys("23:00")
    time.sleep(5)
    timein = woundconfig.driver.find_element_by_xpath('//*[@id="to"]')
    timein.send_keys("23:30")
    time.sleep(5)
    save2btn = woundconfig.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/td[2]/button')
    save2btn.click()
    time.sleep(5)
    woundtab = woundconfig.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[8]')
    woundtab.click()
    time.sleep(5)
   # woundHistory = woundconfig.driver.find_element_by_xpath('//*[@id="pinid1"]/span/span[1]')
   # woundHistory.click()
   # time.sleep(5)
    
    
    
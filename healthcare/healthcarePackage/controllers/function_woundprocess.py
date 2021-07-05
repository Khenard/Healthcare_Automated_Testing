from controllers import config, login, servers, function_mdo
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import pyautogui, sys
import autoit
import os

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

def addwoundoasis(
        woundtype, 
        woundlocation
        ):
        
    #editbtn = config.driver.get('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click()
    integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,500)")
    
    time.sleep(3)
    woundyes = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/label/input').click()
    woundplus =  config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/a').click()
    time.sleep(3)
    
    wound_type = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[1]/input')
    wound_type.click()
    wound_type.send_keys(woundtype)
    time.sleep(2)
    
    woundloc = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[1]/input')
    woundloc.click()
    woundloc.send_keys(woundlocation)
    time.sleep(2)
    
    woundcomment = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[7]/input').send_keys('Added from automated testing.')
    time.sleep(2)
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button[3]').click()
    time.sleep(2)
    
    assessnow = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    
    
def completewoundassessment(
        stages, 
        grantissue, 
        nectissue, 
        granneccoverage, 
        exuamount, 
        exutype, 
        edges, 
        periwoundtissue, 
        healingstatus, 
        woundrelatedpain
        ):
    
    time.sleep(3)
    
    time.sleep(3)   

    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    
    time.sleep(3)
    
    # --- Click the dropdown
    # --- Get all data on dropdown
    # --- Select the option
    
    # Stages
    stages_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//input').click()
    stages_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//li[contains(string(), "'+ stages +'")]').click()
    
    time.sleep(2)
    
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
    
    # Save Assessment
    time.sleep(2)
    savewoundbtn = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/td[2]/button').click()
    

def digitalmeasurement():
    time.sleep(3)
    digitalmesbtn = config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a').click()
    time.sleep(8)
    editdigitalmesbtn =  config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a').click()
    
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
    
    
    
    
    
    
    
from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, patient_dashboard, function_woundprocess
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

def complete_woundprocess(test_server, searchpatient):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)
        
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)
        
    
    task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')
    time.sleep(5)
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
    
    # -- Declare Values 
    
    woundtype = "Pressure Ulcer"
    woundlocation = "Buttock (R)"
    
    stages = "2"
    grantissue = "3"
    nectissue = "3"
    granneccoverage = "4"
    exuamount = "4"
    exutype = "Serous"
    edges = "2"
    periwoundtissue = "Edematous"
    healingstatus = "Early/partial granulation"
    woundrelatedpain = "4"
    
    
    
    function_woundprocess.addwoundoasis(
        woundtype,
        woundlocation
        )
    
    function_woundprocess.dragpin()
    
    function_woundprocess.completewoundassessment(
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
        )
    
    
    function_woundprocess.digitalmeasurement()
    
    function_woundprocess.woundanalytics()



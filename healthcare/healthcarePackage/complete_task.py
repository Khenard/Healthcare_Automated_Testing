from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
    
#lagay ng value and xpath


def snv():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    #check the task if it's in progress on scheduled
    task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')

    taskstatus = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[3]/div/span').text
    print(taskstatus)

    if taskstatus == "In Progress":
        task.click()
        time.sleep(3)
        editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[3]/div[2]/div/button').click() #edit button
        time.sleep(3)
        
    elif taskstatus == "Scheduled":
        task.click()
        time.sleep(3)

        
    vstemp = "97.4"
    vspulse = "85"
    vsres = "28"
    vslasys =  "117"
    vsladyl = "70"
    vso2room = "88"
    vso2o2 = "92"
    vso2lpm = "2"
    vsbs = "128"
    

    function_complete_task.skillednursing(
        todaytime,
        plustime,
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        )
    
    #discard changes
    #discardyes = config.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div/button[1]').click()
    
    time.sleep(2)
    
    patient_dashboard.gettab("task")



def completetask(task):
    
    time.sleep(5)
    
    rnskilledassesment = "RN - Skilled Assessment"
    oasisdcaegency = "RN - OASIS D1 Discharge from Agency"
    oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"
    oasisfollowup = "RN - OASIS D1 Other Follow-Up"
    oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"
    oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"
    
    lvnskilledvisit = "LVN/LPN - Skilled Visit"
    lvnwoundvisit = "LVN/LPN - Wound Visit"
    prnskilledvisit = "PRN - Skilled Visit"
    rneducvisit = "RN - Education Visit"
    rnivvisit = "RN - IV Visit"
    rnjschha = "RN - Joint Supervisory (CHHA)"
    rnjslvn = "RN - Joint Supervisory (LVN)"
    rnskilledvisit = "RN - Skilled Visit"
    rnsupvisit = "RN - Supervisory Visit"
    rnwoundvisit = "RN - Wound Visit"
    
    ptieval = "PT - Initial Eval"
    ptievalsoc = "PT - Initial Eval-SOC"
    ptvisit = "PT - PT Visit"
    ptavisit = "PTA - PTA Visit"
    
    otieval = "OT - Initial Eval"
    otievalsoc = "OT - Initial Eval-SOC"
    otvisit = "OT - OT Visit"
    otavisit = "OTA - OTA Visit"
    
    stieval = "ST - Initial Eval"
    stievalsoc = "ST - Initial Eval-SOC"
    stvisit = "ST - ST Visit"
    
    mswass = "MSW - Assessment"
    mswfollowup = "MSW - Follow-up Visit"
    chhavisit = "CHHA - HHA Visit"

    
    if (((task == rnwoundvisit or task == rnivvisit) or (task == lvnskilledvisit or task == lvnwoundvisit)) or ((task == prnskilledvisit or task == rneducvisit) or (task == rnskilledvisit or task == rnsupvisit))):
        snv()
    elif task == rnjschha or task == rnjslvn:
        rnjschhalvn()
        time.sleep(3)

        
    



    
    


from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

def complete_physician_order(
        ot,
        commnote,
        pyorder
        ):
    ordertime = config.driver.find_element_by_xpath('//*[@id="orderTime"]').send_keys(ot)
    #sentdate = config.driver.find_element_by_xpath('//*[@id="sentDate"]').send_keys(sd)
    #receivedate = config.driver.find_element_by_xpath('//*[@id="receiveDate"]').send_keys(rd)
    #receivetime = config.driver.find_element_by_xpath('//*[@id="receiveTime"]').send_keys(rt)
    commnotes = config.driver.find_element_by_xpath('//*[@id="communicationnote"]').send_keys(commnote)
    physicianorder = config.driver.find_element_by_xpath('//*[@id="physicianordernotes"]').send_keys(commnote)
    
    # Code Explanation: 
    # --- Get all items on the section, store on an array 
    # --- Remove items without checkboxes
    # --- Click the items via for loop
    
    # Subject matter
    items = config.driver.find_element_by_xpath('//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[1]/td[2]').text
    subjectmatter = items.split('\n')
    removeitem = {"Adverse Events", "Other"}
    subjectmatter = [ele for ele in subjectmatter if ele not in removeitem]
    print(subjectmatter)
    for x in subjectmatter:
        finditem = config.driver.find_element_by_xpath('//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[1]/td[2]//label[contains(string(), "'+ x +'")]')
        finditem.click()
    
    # Communication Mode
    items = config.driver.find_element_by_xpath('//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[2]/td[2]').text
    commmode = items.split('\n')
    print(commmode)
    for x in commmode:
        finditem = config.driver.find_element_by_xpath('//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[2]/td[2]//label[contains(string(), "'+ x +'")]')
        finditem.click()
        
    time.sleep(3)
    savebtn = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]').click()
    time.sleep(5)
    

def new_mdo(mdo):
    
    #Click MDO tab
    patient_dashboard.gettab("mdo")
    time.sleep(5)
    
    # Enter the name of order:
    #   -- Recertification Order
    #   -- Discharge Order
    #   -- Discharge (Death at Home)
    #   -- Transfer Order
    #   -- Physician Order
    
    if mdo == "recertification": 
        patient_dashboard.create_mdo("Recertification Order") 
        time.sleep(5)
    elif mdo == "discharge": 
        patient_dashboard.create_mdo("Discharge Order") 
        time.sleep(5)
    elif mdo == "discharge": 
        patient_dashboard.create_mdo("Discharge Order") 
        time.sleep(5)  
    elif mdo == "death": 
        patient_dashboard.create_mdo("Discharge (Death at Home)") 
        time.sleep(5)
    elif mdo == "transfer": 
        patient_dashboard.create_mdo("Transfer Order") 
        time.sleep(5)
    elif mdo == "physician":
        patient_dashboard.create_mdo("Physician Order") 
        time.sleep(5)

    
    



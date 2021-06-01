from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

def complete_physician_order():
    ordertime = config.driver.find_element_by_xpath('//*[@id="orderTime"]')
    sentdate = config.driver.find_element_by_xpath('//*[@id="sentDate"]')
    receivedate = config.driver.find_element_by_xpath('//*[@id="receiveDate"]')
    receivetime = config.driver.find_element_by_xpath('//*[@id="receiveTime"]')
    
    """x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')
    x = config.driver.find_element_by_xpath('')"""


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

    
    



from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_mdo
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

def createmdo(test_server, continuous_test):
    
    todaytime = config.timenow()
    todaydate = config.datenow()
    plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
    
    time.sleep(5)
    
    if continuous_test == "no":
        if test_server == "qa":
            config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #QA
            searchpatient()
        elif test_server == "live":
            config.driver.get("https://app.medisource.com/patientcare/7139B78F-D3A7-4532-B2F4-A1D9AFE0E8AF/D87C5BFF-98B7-4B73-BFD8-461FCADFB118/overview") #LIVE
            searchpatient()
    elif continuous_test == "yes":
        time.sleep(2)
        
    patient_dashboard.gettab("mdo")
    
    
    function_mdo.new_mdo("physician")
    
    function_mdo.complete_physician_order(
        todaytime,
        "SN reported today that patient's skin and conjunctiva is pale. No gross signs and symptoms of bleeding. MD notified. Ordered CBS",
        "MSW to evaluate patient's caregiving situation and compliance with patient's medications and treatment."
        )
    
    patient_dashboard.gettab("mdo")

from controllers import config, login, function_admission, function_oasis, servers, function_snv, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


#QA - UNITEST
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #QA
time.sleep(5)

#Enter the name of patient dashboard tab you want to access

patient_dashboard.gettab("chart")
time.sleep(5)

patient_dashboard.gettab("task")
time.sleep(5)

patient_dashboard.gettab("mdo")
time.sleep(5)


patient_dashboard.gettab("communication")
time.sleep(5)

patient_dashboard.gettab("spx")
time.sleep(5)

patient_dashboard.gettab("task")
time.sleep(5)

patient_dashboard.gettab("adverse")
time.sleep(5)

patient_dashboard.gettab("medication")
time.sleep(5)

patient_dashboard.gettab("misc")
time.sleep(5)

patient_dashboard.gettab("vsmonitor")
time.sleep(5)

patient_dashboard.gettab("ptgmanager")
time.sleep(5)

patient_dashboard.gettab("qasis")
time.sleep(5)







from controllers import config, login, function_admission, function_oasis, servers, function_snv, patient_dashboard, function_mdo
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

#QA - UNITEST
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #QA
time.sleep(5)

function_mdo.new_mdo("physician")

function_mdo.complete_physician_order(
    todaytime,
    "SN reported today that patient's skin and conjunctiva is pale. No gross signs and symptoms of bleeding. MD notified. Ordered CBS",
    "MSW to evaluate patient's caregiving situation and compliance with patient's medications and treatment."
    )

patient_dashboard.gettab("mdo")

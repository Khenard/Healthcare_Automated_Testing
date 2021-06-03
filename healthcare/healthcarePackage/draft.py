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
config.driver.get("https://qado.medisource.com/patientcare/743BD670-8915-460B-8CF5-1145A1066879/6960A273-BF39-4FE4-ADE8-277FCC0B9593/snv/v2view/1451") #QA
time.sleep(5)

editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[3]/div[2]/div/button').click()
time.sleep(3)

neuro = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[3]').click()
time.sleep(5)


scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
items = config.driver.find_element_by_xpath('//*[@id="activities permitted"]').text
activitiespermitted = items.split('\n')
print(activitiespermitted)
removeitem = {"Other:  "}
activitiespermitted = [ele for ele in activitiespermitted if ele not in removeitem]
print(activitiespermitted)
for x in activitiespermitted:
    finditem = config.driver.find_element_by_xpath('//*[@id="activities permitted"]//label[contains(string(), "'+ x +'")]')
    finditem.click()
    
    
    
    
    
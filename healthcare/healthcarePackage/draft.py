from controllers import config, login, function_admission, function_oasis, servers, function_snv, patient_dashboard, function_mdo
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

#QA - UNITEST
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #QA
time.sleep(5)

function_mdo.new_mdo("physician")

function_mdo.complete_physician_order()

smitems = config.driver.find_element_by_xpath('//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[1]/td[2]').text

subjectmatter = smitems.split('\n')
print(subjectmatter)
print(len(subjectmatter))

finditem = config.driver.find_element_by_xpath('//*[@id="parent"]//label[text()="Medication"]').click()


#//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[1]/td[2]/div[1]/div[1]/div/label
#//*[@id="parent"]/div/ng-form/div/fieldset/div[2]/div/div[1]/div/table[2]/tbody/tr[1]/td[2]   /div[1]/div[1]/div/label/input
      
    

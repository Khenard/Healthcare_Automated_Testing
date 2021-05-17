from controllers import config, login, function_admission, function_oasis, servers, function_snv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


#QA
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #QA
time.sleep(3)

# ------------------------------------------------------------------------------------------------
#  CREATE SNV FUNCTIONS
# ------------------------------------------------------------------------------------------------

#open 1st task
current_scheduledtask = config.driver.find_element_by_link_text('RN - Skilled Visit').click()
time.sleep(3)

#editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[3]/div[2]/div/button').click() #edit button
time.sleep(3)

function_snv.timeinout("1200", "1600")

#Tab button
vssensoryintegendo = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[1]')
cardionutrielim = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[2]')
neuromusculo = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[3]')
caremaninterv = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[4]')

time.sleep(5)
    
function_snv.vssensoryintegendo(
    "97.4",
    "85",
    "28",
    "117",
    "70",
    "88",
    "92",
    "2",
    "128"
    )
time.sleep(5)

cardionutrielim.click()        
function_snv.cardionutrielim()

neuromusculo.click()        
function_snv.neuromusculo()

caremaninterv.click()        
function_snv.caremaninterv()


time.sleep(5)





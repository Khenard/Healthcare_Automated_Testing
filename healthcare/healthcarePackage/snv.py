from controllers import config, login, function_admission, function_oasis, servers, function_snv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


def snv(test_server, continuous_test):
    
    # ------------------------------------------------------------------------------------------------
    #  CREATE SNV FUNCTIONS
    # ------------------------------------------------------------------------------------------------
    time.sleep(5)  
    
    #check the task if it's in progress on scheduled 
    taskstatus = config.driver.find_element_by_link_text('Scheduled').click()
    print(taskstatus)
    time.sleep(3)
    
    #open 1st task
    #current_scheduledtask = config.driver.find_element_by_link_text('RN - Skilled Visit').click()
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




    
    
    

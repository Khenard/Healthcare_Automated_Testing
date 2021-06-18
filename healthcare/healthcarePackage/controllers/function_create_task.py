from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


def snv(task):
    
    #sortup = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/thead/tr/th[6]/span/span[2]/i[1]').click()
    sortdown = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/thead/tr/th[6]/span/span[2]/i[2]').click()
    time.sleep(5) 
    
    #1. Get the current date of the OASIS and add days for the task date
    oasisdate = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[6]').text
    #2. Convert to date string
    taskdateconvert = datetime.strptime(oasisdate, '%m/%d/%Y')
    #3. Add days to the date
    addeddaystodate = timedelta(days=6)
    #4. add total
    datetotal = taskdateconvert + addeddaystodate
    #5. convert again to date string for final date
    finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y')
    
    
    #Get the last five days of the episode
    first = timedelta(days=56)
    firsttotal = taskdateconvert + first
    firstlastdate = datetime.strftime(datetotal, '%m/%d/%Y')
    print(firstlastdate)
    
    
    
            
    #Test ouput date
    print(oasisdate)
    print(datetotal)
    print(finaltaskdate)
    
    
    #Get the the add new task button 
    addnewtask_btn = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click()
    time.sleep(3)
    
    #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(finaltaskdate)
            
    taskdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    createtask = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div//li[contains(string(), "'+ task +'")]')
    createtask.click()    
    
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    staff.click()    

    time.sleep(3)
   
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()

    time.sleep(3) 
    #Create button
    
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    
    #go back to task
    #patient_dashboard.gettab("task")
    #time.sleep(5)


def oasis(task):
    
    #sortup = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/thead/tr/th[6]/span/span[2]/i[1]').click()
    sortdown = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/thead/tr/th[6]/span/span[2]/i[2]').click()
   
    time.sleep(5) 
    
    #1. Get the current date of the OASIS and add days for the task date
    oasisdate = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[6]').text
    #2. Convert to date string
    taskdateconvert = datetime.strptime(oasisdate, '%m/%d/%Y')
    #3. Add days to the date
    addeddaystodate = timedelta(days=57)
    #4. add total
    datetotal = taskdateconvert + addeddaystodate
    #5. convert again to date string for final date
    finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y')
            
    #Test ouput date
    print(oasisdate)
    print(datetotal)
    print(finaltaskdate)
    
    #Get the the add new task button 
    addnewtask_btn = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click()
    time.sleep(3)
    
    #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(finaltaskdate)
            
    taskdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
        
    # Enter the EXACT task name you want to create
    time.sleep(3)
    createtask = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div//li[contains(string(), "'+ task +'")]')
    createtask.click()   
    

    time.sleep(3)
    
    visitdate = config.driver.find_element_by_xpath('//*[@id="visitdate"]').send_keys(finaltaskdate)
   
    time.sleep(3) 
    
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
            
    time.sleep(5)     
    
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)


    #Open newly created 
    #current_scheduledtask = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]//a[contains(string(), "'+ task +'")]').click()

  


def completetask(task):
    
    time.sleep(5)
    
    #if task == "RN - Skilled Assessment":
    #    time.sleep(5)
    #elif task == "RN - OASIS D1 Discharge from Agency":
    #    time.sleep(5)
    
 
        
    







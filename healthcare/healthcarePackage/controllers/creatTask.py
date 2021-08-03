from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import os
import time
from controllers import config
from datetime import datetime
from datetime import timedelta
from datetime import date
  

 

def lvnSV():
    # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=1)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
    #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("LVN/LPN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5) 
    
def lvnWV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=2)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("LVN/LPN - Wound Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def prnSV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=3)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("PRN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnEV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=4)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Education Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnIV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=5)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - IV Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnJSHHA():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=6)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Joint Supervisory (CHHA)")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)
    
def rnJSLVN():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=7)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Joint Supervisory (LVN)")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnSV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=9)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnSupV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=10)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Supervisory Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnWV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=11)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Wound Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def ptIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=12)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("PT - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def stIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=13)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("ST - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def otIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=14)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("OT - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)


def mswa():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=15)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("MSW - Assessment")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def mswfv():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=16)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(3)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(3)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("MSW - Follow-up Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(3)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(3) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)




def chha():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=17)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(3)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("CHHA - HHA Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(3)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(3)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5) 
    

 

from controllers import config, login, function_admission, function_oasis, servers
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

# ------------------------------------------------------------------------------------------------
#  SELECT SERVER FOR TEST
# ------------------------------------------------------------------------------------------------

servers.qaserver() #QA server
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview") #Sample patient

#servers.liveserver() #Live server
#config.driver.get("https://app.medisource.com/patientcare/9962299C-1274-4944-9246-FB35680ED6F6/F7180EC0-F8AC-4C07-ADF5-6C33D01C0DEC/overview") #Sample patient

# ------------------------------------------------------------------------------------------------
#  MAIN CREATE TASK FUNCTIONS
# ------------------------------------------------------------------------------------------------

time.sleep(5)

#Get the the add new task button 
addnewtask_btn = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click()

# ------------------------------------------------------------------------------------------------
#  GETTING THE OASIS DATE AND ADD x DAYS FOR THE TASKS DATE
# ------------------------------------------------------------------------------------------------

#1. Get the current date of the OASIS and add days for the task date
oasisdate = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[6]').text
#2. Convert to date string
taskdateconvert = datetime.strptime(oasisdate, '%m/%d/%Y')
#3. Add days to the date
addeddaystodate = timedelta(days=5)
#4. add total
datetotal = taskdateconvert + addeddaystodate
#5. convert again to date string for final date
finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y')

#Test ouput date
print(oasisdate)
print(datetotal)
print(finaltaskdate)

# ------------------------------------------------------------------------------------------------
#  FILL UP TASK MANAGER MODAL
# ------------------------------------------------------------------------------------------------
time.sleep(3)

#task date
taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
taskdate.send_keys(finaltaskdate)

#select task name - RN - Skilled Visit
task = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click()
task_name = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys('RN - Skilled Visit', Keys.ENTER)

#Uncheck the MDO
uncheck_mdo = config.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/ng-form/div[3]/div[2]/div/label/input').click()

#Create button
createbtn = config.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/button[2]').click()










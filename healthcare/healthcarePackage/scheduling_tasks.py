import config
import login, completing_oasis
import random, time
from datetime import date 
from datetime import timedelta
from healthcarePackage import oasis



today = date.today()
todaynow = today.strftime("%m/%d/%Y")

ssn = random.randint(0, 9999999999)

#Open Chrome and navigate to realtime workflow
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

#login function
login.login("superagent@unitest", "Tester2021@")
time.sleep(5)
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview")
time.sleep(5)

#Get Add New Schedule button
addnewtask_btn = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click()

#get the value of OASIS SOC date
oasissocdate_value = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[6]').text
str(oasissocdate_value)
#create task date add oasis value
taskdate = oasissocdate_value + timedelta(days=10)


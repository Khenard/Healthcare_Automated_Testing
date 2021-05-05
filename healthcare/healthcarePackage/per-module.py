import config
import login, completing_oasis
import random, time
from datetime import date

today = date.today()
todaynow = today.strftime("%m/%d/%Y")

ssn = random.randint(0, 9999999999)

#Open Chrome and navigate to realtime workflow
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

#login function
login.login("superagent@unitest", "Tester2021@")
config.driver.get("https://qado.medisource.com/patientcare/98892440-8AF8-41C2-A944-88D485322567/A6796B3C-AB21-4D5A-B4F6-8C45772CC078/2020/oasis/soc/60EA0F34-E4AC-4F0B-9F3B-99A0F76EF30C/98892440-8AF8-41C2-A944-88D485322567/v3/adl")
time.sleep(5)
#click the OASIS edit button
oasisedit = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button").click()
#declare the tabs, save button, and previous next button 
savebtn = config.driver.find_element_by_css_selector("#titleNoteBar > div.col-sm-12.p-0.title__section.m-b-10.oasis_actionBtnTab > div:nth-child(2) > button.btn__success.m-l-10.waves-effect.ng-scope")
previousbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[1]')
nextbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[2]')
 
#OASIS button
democrecord = config.driver.find_element_by_xpath('//*[@id="clinical"]')
diagnosesmedhis = config.driver.find_element_by_xpath('//*[@id="diagnosis"]')
vssensory = config.driver.find_element_by_xpath('//*[@id="sensory"]')
integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]')
cardio = config.driver.find_element_by_xpath('//*[@id="cardio"]')
nutrielim = config.driver.find_element_by_xpath('//*[@id="elimination"]')
neurobehav = config.driver.find_element_by_xpath('//*[@id="neuro"]')
adlmusco = config.driver.find_element_by_xpath('//*[@id="adl"]')
medication = config.driver.find_element_by_xpath('//*[@id="medication"]')
careman = config.driver.find_element_by_xpath('//*[@id="careManagement"]')


# ------------- Care Management -----------------------------------------------------------------------------------
careman.click()
completing_oasis.oasissoc_careman()

savebtn.click()

time.sleep(8)
config.driver.close()



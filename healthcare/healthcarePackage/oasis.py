import config
import login, completing_oasis
import random, time
from datetime import date

today = date.today()
todaynow = today.strftime("%m/%d/%Y")

#Open Chrome and navigate to realtime workflow
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

#login function
login.login("superagent@unitest", "Tester2021!")
config.driver.get("https://qado.medisource.com/patients/admitted")
time.sleep(5)

#search Automated Patient and click the top/first result
search_patient = config.driver.find_element_by_xpath("//*[@id='searchbar__wrapper']/div/input")
search_patient.send_keys("Automated")
time.sleep(5)
patientresult = config.driver.find_element_by_xpath("//*[@id='content']/data/div/div[2]/div/table/tbody/tr[2]").click()
time.sleep(5)

#Open the OASIS 
clickoasis = config.driver.find_element_by_xpath("//*[@id='parent']/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a").click()
time.sleep(5)
#click the OASIS edit button
oasisedit = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button").click()

# ------------------------------------------------------------------------------------------------
#Functions for completing OASIS per tab
time.sleep(5)
#declare the tabs, save button, and previous next button 
#savebtn = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button[3]")
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

#entering Time in and Time out
completing_oasis.oasissoc_timeinout("1200", "1600")

#demographics
completing_oasis.oasissoc_demographics(savebtn, todaynow, "Early")

diagnosesmedhis.click()

completing_oasis.oasissoc_diagnosesmedhis(
    "COVID-19",
    "Pseudomonas (aeruginosa)",
    "Obstructive and reflux uropathy, unspecified"
    )


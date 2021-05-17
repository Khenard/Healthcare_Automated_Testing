from controllers import config, login, servers
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

# TIME IN TIME OUT
def timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

# VS/SENSORY/INTEGUMENTARY/ENDOCRINE
def vssensoryintegendo(
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        ):
    time.sleep(5)
    
    vs_temp = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/div/input').send_keys(vstemp)
    vs_temp_scan = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[1]/td[3]/div[2]/label[2]/input').click() #scan
    
    vs_pulse = config.driver.find_element_by_name("VS0003").send_keys(vspulse)
    vs_pulse_radial = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/div[2]/label[1]/input').click()
    vs_res = config.driver.find_element_by_name("VS0006").send_keys(vsres)
    
    vs_lefta_sys = config.driver.find_element_by_name("VS0009").send_keys(vslasys)
    vs_lefta_dyl = config.driver.find_element_by_name("VS0057").send_keys(vsladyl)
    vs_lefta_sitting = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/div/label[1]/input').click()
    
    vs_o2room = config.driver.find_element_by_name("VS0021").send_keys(vso2room)
    vs_o2o2 = config.driver.find_element_by_name("VS0022").send_keys(vso2o2)
    vs_o2lpm = config.driver.find_element_by_name("VS0023").send_keys(vso2lpm)
    
    vs_bs = config.driver.find_element_by_name("VS0024").send_keys(vsbs)
    vs_bs_rbs = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[10]/td[3]/div[2]/label[2]/input').click()
    
    vs_weight_actual = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[11]/td[3]/div[2]/label[1]/input').click()
    vs_height_actual = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/div/input').click()
    
    m1242_nopain = config.driver.find_element_by_xpath('//*[@id="pain_assessment"]/tbody/tr/td/div[1]/label/input').click()
  
    #All sensory status will be WNL
    ss_eyes_wnl = config.driver.find_element_by_xpath('//*[@id="sensory_assessment"]/tbody/tr[1]/td/div/div/label/input').click()
    ss_ear_wnl = config.driver.find_element_by_name("SENSORY0039").click()
    ss_mouth_wnl = config.driver.find_element_by_name("SENSORY0059").click() 
    ss_nose_wnl = config.driver.find_element_by_name("SENSORY0055").click() 
    ss_throat_wnl = config.driver.find_element_by_name("SENSORY0063").click() 
    ss_speech_wnl = config.driver.find_element_by_name("SENSORY0067").click() 
    ss_touch_wnl = config.driver.find_element_by_name("SENSORY0070").click() 
    
# CADRIOPULMONARY/NUTRITION/ELIMINATION
def cardionutrielim(): 
    time.sleep(5)
    shortofbreath = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[1]/tbody/tr/td/table[2]/tbody/tr/td[1]/div/label/input').click()
    resps_wnl = config.driver.find_element_by_xpath('//*[@id="respiratory"]/tr/td[2]/table/tbody/tr/td[2]/div/label/input').click()
    cardio_wnl = config.driver.find_element_by_xpath('//*[@id="cardiovascular_temp"]/tr/td[2]/table/tbody/tr/td[2]/div/label/input').click()
    uppergistat_wnl = config.driver.find_element_by_xpath('//*[@id="upper_gastrointestinal"]/tr/td[2]/div/label/input').click()
    lowergistat_wnl = config.driver.find_element_by_xpath('//*[@id="lower_gastrointestinal"]/tbody/tr/th[2]/div/div/label/input').click()
    genitostat_wnl = config.driver.find_element_by_xpath('//*[@id="genitourinary_status_temp"]/tbody/tr/th[2]/div/div/label/input').click()
    abnelim_no = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[3]/tbody/tr[2]/td/table[3]/tbody/tr[1]/td[2]/label[1]/input').click()
    spx_no = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[3]/tbody/tr[2]/td/table[4]/tbody/tr/td[2]/label/input').click()

# NEUROLOGIC/MUSCULOSKELETAL
def neuromusculo():
    time.sleep(5)
    neurostat_wnl = config.driver.find_element_by_xpath('//*[@id="neurological_status_temp"]/tbody/tr/th[2]/div/div/label/input').click()
    thought_wnl = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr/td/table[4]/tbody/tr/th[2]/div[1]/div/label/input').click()
    musculo_wnl = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr/td/table[5]/tbody/tr/th[2]/div[1]/div/label/input').click()

# CARE MANAGMENT/INTERVENTIONS
def caremaninterv():
    time.sleep(5)
    config.driver.close()


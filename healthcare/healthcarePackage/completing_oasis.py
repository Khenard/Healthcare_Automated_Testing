import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def oasissoc_timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

def oasissoc_demographics(
        todaynow, 
        episodetiming
        ):
    m0090 = config.driver.find_element_by_id("m0090_info_completed_dt").send_keys(todaynow)
    time.sleep(3)
    m0102_checkbox = config.driver.find_element_by_name("M0102_PHYSN_ORDRD_SOCROC_DT_NA").click()
    time.sleep(3)
    m0104 = config.driver.find_element_by_name("M0104_PHYSN_RFRL_DT").send_keys(todaynow)
    
    etiming = ""
    if episodetiming == "Early":
        etiming = config.driver.find_element_by_name("6807")
    elif episodetiming == "Later":
        etiming = config.driver.find_element_by_name("6808")
    elif episodetiming == "Unknown":
        etiming = config.driver.find_element_by_name("6809")
    elif episodetiming == "NA":
        etiming = config.driver.find_element_by_name("6810")
    etiming.click()
    
    
    
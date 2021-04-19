import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def oasissoc_timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

def oasissoc_demographics(todaynow):
    m0090 = config.driver.find_element_by_id("m0090_info_completed_dt").send_keys(todaynow)
    m0102_checkbox = config.drver.find_element_by_name("M0102_PHYSN_ORDRD_SOCROC_DT_NA").click()
    m0104 = config.driver.find_element_by_name("M0104_PHYSN_RFRL_DT").send_keys(todaynow)
    
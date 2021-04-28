import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from _ast import Div


def oasissoc_timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

def oasissoc_demographics(savebtn, todaynow, episodetiming):
    m0090 = config.driver.find_element_by_id("m0090_info_completed_dt").send_keys(todaynow)
    time.sleep(3)
    m0102_checkbox = config.driver.find_element_by_name("M0102_PHYSN_ORDRD_SOCROC_DT_NA").click()
    time.sleep(3)
    m0104 = config.driver.find_element_by_id("m0104_physn_rfrl_dt").send_keys(todaynow)
    
    #For Episode Timing
    etiming = ""
    if episodetiming == "Early":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[1]/label/input")
    elif episodetiming == "Later":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[2]/label/input")
    elif episodetiming == "Unknown":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[1]/label/input")
    elif episodetiming == "NA":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[2]/label/input")
    etiming.click()
    
    #Asian 
    m0140 = config.driver.find_element_by_xpath("//*[@id='M0140_ETHNIC_ASIAN']/input").click()
    
    #Medicare Traditional 
    m0150 = config.driver.find_element_by_xpath("//*[@id='M0150_CPAY_MCARE_FFS']/input").click()
    #Private Insurance
    #m0150 = config.driver.find_element_by_xpath("//*[@id='M0150_CPAY_PRIV_INS']/input").click()
     
    #Skilled Nursing Facility
    m1000 = config.driver.find_element_by_name("M1000_DC_SNF_14_DA").click()
     
    #Unknown
    m1005 = config.driver.find_element_by_name("M1005_INP_DSCHG_UNKNOWN").click()
    
    #savebtn.click()
    
def oasissoc_diagnosesmedhis(
        pdx,
        sdx1,
        sdx2,
        sdx3,
        sdx4,
        sdx5
        ):
    time.sleep(5)
    
    #Primary Diagnosis
    pd = config.driver.find_element_by_xpath("//*[@id='tooltip_a']/table/tbody/tr/td[2]/icd-opt/div/div[1]/input")
    pd.send_keys(pdx)
    time.sleep(1)
    config.driver.switch_to_active_element()
    pd.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    pd.send_keys(Keys.ENTER)
    pdr = config.driver.find_element_by_xpath("//*[@id='icdSeverityIdCode$index']/label[4]/input").click()
    
    #Secondary Diagnosis
    #1st Secondary Diagnosis
    sd1 = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd1.send_keys(sdx1)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd1.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd1.send_keys(Keys.ENTER)
    sd1r = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
    
    #2nd Secondary Diagnosis
    sd2 = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd2.send_keys(sdx2)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd2.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd2.send_keys(Keys.ENTER)
    sd2r = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #3rd Secondary Diagnosis
    sd3 = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd3.send_keys(sdx3)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd3.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd3.send_keys(Keys.ENTER)
    sd3r = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #4th Secondary Diagnosis
    sd4 = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd4.send_keys(sdx4)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd4.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd4.send_keys(Keys.ENTER)
    sd4r = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #5th Secondary Diagnosis
    sd5 = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd5.send_keys(sdx5)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd5.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd5.send_keys(Keys.ENTER)
    sd5r = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3



    time.sleep(5)
    #config.driver.close()
    
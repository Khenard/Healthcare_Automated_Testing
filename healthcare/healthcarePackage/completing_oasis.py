import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


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
        sdxb,
        sdxc
        ):
    time.sleep(5)
    #primary diagnosis
    pd = config.driver.find_element_by_xpath("//*[@id='diagnosisForm']/div/fieldset/table[1]/tbody/tr[3]/td/table/tbody[2]/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/icd-opt/div/div[1]/input").send_keys(pdx, Keys.ENTER)
    pdr = config.driver.find_element_by_xpath("//*[@id='diagnosisForm']/div/fieldset/table[1]/tbody/tr[3]/td/table/tbody[2]/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/icd-opt/div/div[2]/ul").click()
    
    
    pdrating = config.driver.find_element_by_xpath('//*[@id="icdSeverityIdCode$index"]/label[4]/input').click()
    #secondary diagnosis
    sdb = config.driver.find_element_by_xpath("//*[@id='diagnosisForm']/div/fieldset/table[1]/tbody/tr[3]/td/table/tbody[2]/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/icd-opt/div/div[1]/input").send_keys(sdxb, Keys.ENTER)
    sdbrating = config.driver.find_element_by_xpath("//*[@id='icdSeverityIdCode$index']/label[2]/input").click()
    sdc = config.driver.find_element_by_xpath("//*[@id='diagnosisForm']/div/fieldset/table[1]/tbody/tr[3]/td/table/tbody[2]/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/icd-opt/div/div[1]/input").send_keys(sdxc, Keys.ENTER)
    sdcrating = config.driver.find_element_by_xpath("//*[@id='icdSeverityIdCode$index']/label[3]/input").click()
 
 
    # sdb = config.driver.find_element_by_xpath("")send_keys(pdx, Keys.ENTER)
    # sdbrating = config.driver.find_element_by_xpath("").click()
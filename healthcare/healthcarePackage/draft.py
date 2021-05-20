from controllers import config, login, function_admission, function_oasis, servers, function_snv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


#QA
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/88AB9D4E-3CDD-43F7-B222-7D6862CC892E/DA97206A-824E-4BE8-8BF7-5014493F0CD7/2020/oasis/soc/52491A5D-B6EB-40E8-A50C-4B085B467070/88AB9D4E-3CDD-43F7-B222-7D6862CC892E/v3/adl") #QA
time.sleep(3)

time.sleep(5)  

#click the OASIS edit button
oasisedit = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button").click()
     
    
scrolldown = config.driver.execute_script("window.scrollTo(0,3500)")
    
GG0100A = config.driver.find_element_by_xpath('//*[@id="GG0100A_chosen"]').click()
GG0100A3 = config.driver.find_element_by_xpath('//*[@id="GG0100A_chosen"]/div/ul/li[1]').click()
GG0100B = config.driver.find_element_by_xpath('//*[@id="GG0100B_chosen"]').click()
GG0100B3 = config.driver.find_element_by_xpath('//*[@id="GG0100B_chosen"]/div/ul/li[1]').click()
GG0100C = config.driver.find_element_by_xpath('//*[@id="GG0100C_chosen"]').click()
GG0100C3 = config.driver.find_element_by_xpath('//*[@id="GG0100C_chosen"]/div/ul/li[1]').click()
GG0100D = config.driver.find_element_by_xpath('//*[@id="GG0100D_chosen"]').click()
GG0100D3 = config.driver.find_element_by_xpath('//*[@id="GG0100D_chosen"]/div/ul/li[1]').click()
gg0110_z = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[18]/tbody/tr[2]/td/table/tbody/tr[4]/td[3]/label/input').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,4000)")

GG0130A1 = config.driver.find_element_by_xpath('//*[@id="GG0130A1"]/div/mhc-gg0130').click()
GG0130A16 = config.driver.find_element_by_xpath('//*[@id="GG0130A1"]//div/ul/li[1]').click()
GG0130A2 = config.driver.find_element_by_xpath('//*[@id="GG0130A2"]/div/mhc-gg0130').click()
GG0130A26 = config.driver.find_element_by_xpath('//*[@id="GG0130A2"]//div/ul/li[1]').click()

GG0130B1 = config.driver.find_element_by_xpath('//*[@id="GG0130B1"]/div/mhc-gg0130').click()
GG0130B16 = config.driver.find_element_by_xpath('//*[@id="GG0130B1"]//div/ul/li[1]').click()
GG0130B2 = config.driver.find_element_by_xpath('//*[@id="GG0130B2"]/div/mhc-gg0130').click()
GG0130B26 = config.driver.find_element_by_xpath('//*[@id="GG0130B2"]//div/ul/li[1]').click()

GG0130C1 = config.driver.find_element_by_xpath('//*[@id="GG0130C1"]/div/mhc-gg0130').click()
GG0130C16 = config.driver.find_element_by_xpath('//*[@id="GG0130C1"]//div/ul/li[1]').click()
GG0130C2 = config.driver.find_element_by_xpath('//*[@id="GG0130C2"]/div/mhc-gg0130').click()
GG0130C26 = config.driver.find_element_by_xpath('//*[@id="GG0130C2"]//div/ul/li[1]').click()

GG0130E1 = config.driver.find_element_by_xpath('//*[@id="GG0130E1"]/div/mhc-gg0130').click()
GG0130E16 = config.driver.find_element_by_xpath('//*[@id="GG0130E1"]//div/ul/li[1]').click()
GG0130E2 = config.driver.find_element_by_xpath('//*[@id="GG0130E2"]/div/mhc-gg0130').click()
GG0130E26 = config.driver.find_element_by_xpath('//*[@id="GG0130E2"]//div/ul/li[1]').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,4300)")

GG0130F1 = config.driver.find_element_by_xpath('//*[@id="GG0130F1"]/div/mhc-gg0130').click()
GG0130F16 = config.driver.find_element_by_xpath('//*[@id="GG0130F1"]//div/ul/li[1]').click()
GG0130F2 = config.driver.find_element_by_xpath('//*[@id="GG0130F2"]/div/mhc-gg0130').click()
GG0130F26 = config.driver.find_element_by_xpath('//*[@id="GG0130F2"]//div/ul/li[1]').click()

GG0130G1 = config.driver.find_element_by_xpath('//*[@id="GG0130G1"]/div/mhc-gg0130').click()
GG0130G16 = config.driver.find_element_by_xpath('//*[@id="GG0130G1"]//div/ul/li[1]').click()
GG0130G2 = config.driver.find_element_by_xpath('//*[@id="GG0130G2"]/div/mhc-gg0130').click()
GG0130G26 = config.driver.find_element_by_xpath('//*[@id="GG0130G2"]//div/ul/li[1]').click()

GG0130H1 = config.driver.find_element_by_xpath('//*[@id="GG0130H1"]/div/mhc-gg0130').click()
GG0130H16 = config.driver.find_element_by_xpath('//*[@id="GG0130H1"]//div/ul/li[1]').click()
GG0130H2 = config.driver.find_element_by_xpath('//*[@id="GG0130H2"]/div/mhc-gg0130').click()
GG0130H26 = config.driver.find_element_by_xpath('//*[@id="GG0130H2"]//div/ul/li[1]').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,5200)")

GG0170A1 = config.driver.find_element_by_xpath('//*[@id="GG0170A1"]').click()
GG0170A16 = config.driver.find_element_by_xpath('//*[@id="GG0170A1"]//div/ul/li[1]').click()
GG0170A2 = config.driver.find_element_by_xpath('//*[@id="GG0170A2"]').click()
GG0170A26 = config.driver.find_element_by_xpath('//*[@id="GG0170A2"]//div/ul/li[1]').click()

GG0170B1 = config.driver.find_element_by_xpath('//*[@id="GG0170B1"]').click()
GG0170B16 = config.driver.find_element_by_xpath('//*[@id="GG0170B1"]//div/ul/li[1]').click()
GG0170B2 = config.driver.find_element_by_xpath('//*[@id="GG0170B2"]').click()
GG0170B26 = config.driver.find_element_by_xpath('//*[@id="GG0170B2"]//div/ul/li[1]').click()

GG0170C1 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_SOCROC_PERF"]/div/mhc-gg0170c/div').click()
GG0170C16 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_SOCROC_PERF"]//div/ul/li[1]').click()
GG0170C2 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_DSCHG_GOAL"]/div/mhc-gg0170c/div').click()
GG0170C26 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_DSCHG_GOAL"]//div/ul/li[1]').click()

GG0170D1 = config.driver.find_element_by_xpath('//*[@id="GG0170D1"]/div/mhc-gg0170c/div').click()
GG0170D16 = config.driver.find_element_by_xpath('//*[@id="GG0170D1"]//div/ul/li[1]').click()
GG0170D2 = config.driver.find_element_by_xpath('//*[@id="GG0170D2"]/div/mhc-gg0170c/div').click()
GG0170D26 = config.driver.find_element_by_xpath('//*[@id="GG0170D2"]//div/ul/li[1]').click()

GG0170E1 = config.driver.find_element_by_xpath('//*[@id="GG0170E1"]').click()
GG0170E16 = config.driver.find_element_by_xpath('//*[@id="GG0170E1"]//div/ul/li[1]').click()
GG0170E2 = config.driver.find_element_by_xpath('//*[@id="GG0170E2"]').click()
GG0170E26 = config.driver.find_element_by_xpath('//*[@id="GG0170E2"]//div/ul/li[1]').click()

GG0170F1 = config.driver.find_element_by_xpath('//*[@id="GG0170F1"]').click()
GG0170F16 = config.driver.find_element_by_xpath('//*[@id="GG0170F1"]//div/ul/li[1]').click()
GG0170F2 = config.driver.find_element_by_xpath('//*[@id="GG0170F2"]').click()
GG0170F26 = config.driver.find_element_by_xpath('//*[@id="GG0170F2"]//div/ul/li[1]').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,5500)")

GG0170G1 = config.driver.find_element_by_xpath('//*[@id="GG0170G1"]').click()
GG0170G16 = config.driver.find_element_by_xpath('//*[@id="GG0170G1"]//div/ul/li[1]').click()
GG0170G2 = config.driver.find_element_by_xpath('//*[@id="GG0170G2"]').click()
GG0170G26 = config.driver.find_element_by_xpath('//*[@id="GG0170G2"]//div/ul/li[1]').click()

GG0170I1 = config.driver.find_element_by_xpath('//*[@id="GG0170I1"]').click()
GG0170I16 = config.driver.find_element_by_xpath('//*[@id="GG0170I1"]//div/ul/li[1]').click()
GG0170I2 = config.driver.find_element_by_xpath('//*[@id="GG0170I2"]').click()
GG0170I26 = config.driver.find_element_by_xpath('//*[@id="GG0170I2"]//div/ul/li[1]').click()

GG0170J1 = config.driver.find_element_by_xpath('//*[@id="GG0170J1"]').click()
GG0170J16 = config.driver.find_element_by_xpath('//*[@id="GG0170J1"]//div/ul/li[1]').click()
GG0170J2 = config.driver.find_element_by_xpath('//*[@id="GG0170J2"]').click()
GG0170J26 = config.driver.find_element_by_xpath('//*[@id="GG0170J2"]//div/ul/li[1]').click()

GG0170K1 = config.driver.find_element_by_xpath('//*[@id="GG0170K1"]').click()
GG0170K16 = config.driver.find_element_by_xpath('//*[@id="GG0170K1"]//div/ul/li[1]').click()
GG0170K2 = config.driver.find_element_by_xpath('//*[@id="GG0170K2"]').click()
GG0170K26 = config.driver.find_element_by_xpath('//*[@id="GG0170K2"]//div/ul/li[1]').click()

GG0170L1 = config.driver.find_element_by_xpath('//*[@id="GG0170L1"]').click()
GG0170L16 = config.driver.find_element_by_xpath('//*[@id="GG0170L1"]//div/ul/li[1]').click()
GG0170L2 = config.driver.find_element_by_xpath('//*[@id="GG0170L2"]').click()
GG0170L26 = config.driver.find_element_by_xpath('//*[@id="GG0170L2"]//div/ul/li[1]').click()

scrolldown = config.driver.execute_script("window.scrollTo(0,6000)")

GG0170M1 = config.driver.find_element_by_xpath('//*[@id="GG0170M1"]').click()
GG0170M16 = config.driver.find_element_by_xpath('//*[@id="GG0170M1"]//div/ul/li[1]').click()
GG0170M2 = config.driver.find_element_by_xpath('//*[@id="GG0170M2"]').click()
GG0170M26 = config.driver.find_element_by_xpath('//*[@id="GG0170M2"]//div/ul/li[1]').click()

GG0170N1 = config.driver.find_element_by_xpath('//*[@id="GG0170N1"]').click()
GG0170N16 = config.driver.find_element_by_xpath('//*[@id="GG0170N1"]//div/ul/li[1]').click()
GG0170N2 = config.driver.find_element_by_xpath('//*[@id="GG0170N2"]').click()
GG0170N26 = config.driver.find_element_by_xpath('//*[@id="GG0170N2"]//div/ul/li[1]').click()

GG0170O1 = config.driver.find_element_by_xpath('//*[@id="GG0170O1"]').click()
GG0170O16 = config.driver.find_element_by_xpath('//*[@id="GG0170O1"]//div/ul/li[1]').click()
GG0170O2 = config.driver.find_element_by_xpath('//*[@id="GG0170O2"]').click()
GG0170O26 = config.driver.find_element_by_xpath('//*[@id="GG0170O2"]//div/ul/li[1]').click()

GG0170P1 = config.driver.find_element_by_xpath('//*[@id="GG0170P1"]').click()
GG0170P16 = config.driver.find_element_by_xpath('//*[@id="GG0170P1"]//div/ul/li[1]').click()
GG0170P2 = config.driver.find_element_by_xpath('//*[@id="GG0170P2"]').click()
GG0170P26 = config.driver.find_element_by_xpath('//*[@id="GG0170P2"]//div/ul/li[1]').click()

GG0170Q1 = config.driver.find_element_by_xpath('//*[@id="GG0170Q1_chosen"]').click()
GG0170Q11 = config.driver.find_element_by_xpath('//*[@id="GG0170Q1_chosen"]/div/ul/li[1]').click()








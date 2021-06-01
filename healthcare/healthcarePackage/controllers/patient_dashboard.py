from controllers import config, login, servers
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def gettab(pdtab):

    tab = ""
    
    if pdtab == "chart":
        tab = config.driver.find_element_by_xpath('//*[@id="togglesidelist"]')
           
    elif pdtab == "task":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[2]/a')
        
    elif pdtab == "mdo":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[3]/a')
    
    elif pdtab == "communication":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[4]/a')
           
    elif pdtab == "spx":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[5]/a')
        
    elif pdtab == "adverse":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[6]/a')

    elif pdtab == "medication":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[7]/a')
        
    elif pdtab == "misc":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[8]/a')
        
    elif pdtab == "vsmonitor":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[9]/a')
        
    elif pdtab == "qasis":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[10]/a')   
                 
    elif pdtab == "ptgmanager":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[11]/a')
        
    tab.click()
    
        
        
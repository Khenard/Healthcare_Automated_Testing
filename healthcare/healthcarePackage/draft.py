from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess, function_human_resources, function_medical_resources
import random, os, pyautogui, sys, autoit, ctypes
import time
import pymsgbox
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import random
from selenium.webdriver.common.action_chains import ActionChains


name_random = config.randomize_name()
ssn = config.randomize_ssn()

randomtype = str(name_random) + " " + str(ssn)

# Hospital
servers.qaserver()
config.driver.get("https://qado.medisource.com/hospital")
time.sleep(3)
newhospitalbtn =  config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a').click()

time.sleep(2)

addtype = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/button').click()

time.sleep(3)
typetitle = config.driver.find_element_by_xpath('//*[@id="title"]').send_keys(randomtype)
time.sleep(3)
savetypebtn = config.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/form/div/div[3]/div/button[2]').click()

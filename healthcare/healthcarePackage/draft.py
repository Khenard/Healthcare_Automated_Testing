from controllers import config, login, function_admission, function_oasis, servers, function_snv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta


#QA
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/51BD74B9-836C-4BB3-AD5C-5D4270654FDB/1741C467-22FA-4B59-A2E2-B67ADB1EB500/2020/oasis/soc/14E7E7A6-B914-4096-BF1A-3F5F2631D7D0/51BD74B9-836C-4BB3-AD5C-5D4270654FDB/v3/clinical") #QA
time.sleep(3)

servers.webpagetest()
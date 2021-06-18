from controllers import config, login, function_admission, function_oasis, servers, function_snv, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait




servers.liveserver()
config.driver.get("https://app.medisource.com/patientcare/3B46FBCD-038C-4EF4-8976-09C659819D90/DCA59BDD-F004-4CED-8F73-60F215D333A4/overview")
   

# END TEST

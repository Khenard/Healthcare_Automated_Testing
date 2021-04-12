from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

#Configure web driver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)


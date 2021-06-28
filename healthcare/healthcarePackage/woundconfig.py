from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions


chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

file_path = os.path.abspath('./data/wound-images-week_7.png')

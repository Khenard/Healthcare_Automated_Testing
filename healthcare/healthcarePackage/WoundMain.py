from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import woundfunction
import woundconfig
import mswfunction
#import Upload


woundconfig.driver.get("https://qado.medisource.com/login")
woundconfig.driver.maximize_window()
woundfunction.loginfunction('superagent@geeksnest', 'Tester2021@')


woundfunction.clicktabsfunction()
#woundfunction.editOasisfunction('Lorem Ipsum')
#woundfunction.woundcareFunction()
#woundfunction.UploadFunction()
#woundfunction.mouseHover()
#woundfunction.pressDigitalMeasurement()
#woundfunction.WoundMeasurement()
#woundfunction.inputGranulation()
#woundfunction.SaveFunction()



#after adding ng wound proceed sa addding ng entry sa MSW
mswfunction.clickTaskMenu()
mswfunction.mswform('samplehse', 'sampleec', 'sampless', 'samplehs')

woundconfig.driver.close()
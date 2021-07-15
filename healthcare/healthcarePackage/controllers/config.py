from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import os
import time
from datetime import date
import platform, getpass
import cv2 as cv
import pyautogui
import numpy as np



#Configure web driver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)

def timenow():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return current_time

def datenow():
    today = date.today()
    todaynow = today.strftime("%m/%d/%Y")
    return todaynow

def systeminfo():
    my_system = platform.uname()
    username = getpass.getuser()
    
    todaytime = timenow()
    todaydate = datenow()
    
    sysinfo = str("Testing Information: \n Tester: " + username + " \n Time: " + todaytime + "\n Date: " + todaydate + " \n \n System: " + my_system.system + "\n Node Name: " + my_system.node + "\n Release: " + my_system.release + "\n Version: " + my_system.version + "\n Machine: " + my_system.machine + "\n Processor: " + my_system.processor)
    return sysinfo

def take_screenshot():
    ss = driver.get_screenshot_as_file("./screenshots/screenshot.png") 
    return ss

def take_video():
    
    #(width,height)
    screen_size=pyautogui.size()
    
    #initialize the object
    video = cv.VideoWriter('Recording.avi', cv.VideoWriter_fourcc(*'MJPG'), 20, screen_size)
    
    print("Recording.....")
    while True:
        #click screen shot
        screen_shot_img = pyautogui.screenshot()
    
        #convert into array
        frame = np.array(screen_shot_img)
    
        #change from BGR to RGB
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
        #write frame
        video.write(frame)
    
        #display the live recording 
        cv.imshow("Recording Frame(Minimize it)", frame)    
        if cv.waitKey(1) == ord("q"):
            break
    
    cv.destroyAllWindows()
    video.release()

    

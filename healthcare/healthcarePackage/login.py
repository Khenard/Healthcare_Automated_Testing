import config, time
def login(un, up):
    #Set Variables
    user_name = un
    password = up
    #get the LOGIN button element by xpath
    submitbtn = config.driver.find_element_by_xpath("//*[@id='mhLP-ln']/div[2]/form/div[6]/button")
    
    #Get element and applied set variables
    element = config.driver.find_element_by_id("loginemail")
    element.send_keys(user_name)
    element = config.driver.find_element_by_id("loginpassword")
    element.send_keys(password)
    time.sleep(1)
    submitbtn.click()
    time.sleep(1)



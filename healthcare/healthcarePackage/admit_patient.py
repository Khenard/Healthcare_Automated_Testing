import config, time
def admission():
    #Navigate to Add patient page
    config.driver.get("https://qado.medisource.com/patient")
    
    time.sleep(15)
    #get id and xpath and assign variables
    skip_eligibility = config.driver.find_element_by_xpath("/html/body/div[12]/div/div/div/form/div/div[3]/div/a")
    
    #functions
    skip_eligibility.click()
    time.sleep(5)

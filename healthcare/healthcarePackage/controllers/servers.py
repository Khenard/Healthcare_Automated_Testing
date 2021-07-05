from controllers import config, login
import time

# ------------------------------------------------------------------------------------------------
#  QA SERVER
# ------------------------------------------------------------------------------------------------
def qaserver():
    config.driver.maximize_window()
    config.driver.get("https://qado.medisource.com/login")
    
    login.login("superagent@unitest", "Tester2021@")
    time.sleep(5)
    
# ------------------------------------------------------------------------------------------------
#  LIVE SERVER
# ------------------------------------------------------------------------------------------------
def liveserver():
    config.driver.maximize_window()
    config.driver.get("https://app.medisource.com/login")
    
    login.login("superagent@geekers", "Tester2021@")
    time.sleep(5)
    
def webpagetest():
    # Use Navigation Timing  API to calculate the timings that matter the most
    # https://www.lambdatest.com/blog/how-to-measure-page-load-times-with-selenium/
    navigationStart = config.driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = config.driver.execute_script("return window.performance.timing.responseStart")
    domComplete = config.driver.execute_script("return window.performance.timing.domComplete")
    
    # Calculate the performance 
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
     
    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)    

    

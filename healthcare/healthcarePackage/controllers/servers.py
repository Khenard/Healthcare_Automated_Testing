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
    
    login.login("superagent@geekers", "Tester2021!")
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
     
    """
    navigationStart – This attribute returns the time spent after the user agent completes unloading the previous page/document. If there was no document prior to loading the new page, navigationStart returns the same value as fetchStart.
    responseStart – This attribute returns the time as soon as the user-agent receives the first byte from the server or from the local sources/application cache.
    domComplete – This attribute returns the time just before the current document/page readiness is set to ‘complete’. 
    document.readyState status as ‘complete’ indicates that the parsing of the page/document is complete & all the resources required for the page are downloaded. 
    """
    
    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)    

    

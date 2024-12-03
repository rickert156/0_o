import time

def login(driver):
    url_login = 'https://account.ycombinator.com/?continue=https://www.workatastartup.com/'
    
    driver.get(url_login) 
    time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from tools.login_y import login as y_comb_log
from tools.scrollingY import scrollingSearchPage
from tools.scrapyLinks import scrapyLinks
from tools.parserCompanies import CollectInfo


profile_chrome = 'ProfileChrome'

chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={profile_chrome}')
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(options=chrome_options)




if __name__ == '__main__':
    #y_comb_log(driver)
    #scrollingSearchPage(driver)

    CollectInfo(driver, 'https://www.workatastartup.com/companies/ply-health')

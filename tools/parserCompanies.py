from tools.colors import RED, GREEN, RESET
from selenium.webdriver.common.by import By
import csv, os, time
from bs4 import BeautifulSoup

def CompanyName(driver):
    try:company_name = driver.find_element(By.CLASS_NAME, 'company-name').text
    except:company_name = 'N/A'
    return company_name
    

def TitleCompany(driver):
    try:title_company = driver.find_element(By.CLASS_NAME, 'mt-3.text-gray-700').text
    except:title_company = 'N/A'
    return title_company

def AboutCompany(driver):
    try:about_company = driver.find_element(By.CSS_SELECTOR, 'div[class*="prose col-span-11"]').text
    except:about_company = 'N/A'
    return about_company

def EmployeesComapny(driver):
    pass

def CollectInfo(driver, url):
    driver.get(url);time.sleep(3)

    company_name = CompanyName(driver)
    title_company = TitleCompany(driver)
    about_company = AboutCompany(driver)

    print(f'{RED}Company Name:{RESET}\t{GREEN}{company_name}{RESET}')
    print(f'{RED}Company Title:{RESET}\t{GREEN}{title_company}{RESET}')
    print(f'{RED}About Company:{RESET}\t{GREEN}{about_company}{RESET}')

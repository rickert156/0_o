from tools.colors import RED, GREEN, YELLOW, RESET
from selenium.webdriver.common.by import By
import csv, os, time

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

def FounderComapny(driver):
    try:founder_company = driver.find_element(By.CSS_SELECTOR, 'div[class*="flex flex-col"]').text.split('Founders')[1].strip()
    except:founder_company = 'N/A'
    return founder_company

def SocialLink(driver):
    try:
        LIST_NAME = []
        SOCIAL_LINK = []
        for name in driver.find_elements(By.CLASS_NAME, 'mb-1.font-medium'):
            name = name.text
            LIST_NAME+=[name]

        for link in driver.find_elements(By.TAG_NAME, 'a'):
            link = link.get_attribute('href')
            if 'https://www.linkedin.com/in/' in link:
                SOCIAL_LINK+=[link]
    except:name = 'N/A'
    return LIST_NAME, SOCIAL_LINK

def TechCompany(driver):
    try:tech_company = driver.find_element(By.CSS_SELECTOR, 'div[class*="prose col-span-11 mx-5"]').text
    except:tech_company = 'N/A'
    return tech_company

def InfoCompany(driver):
    try:info_company = driver.find_element(By.CSS_SELECTOR, '"flex flex-wrap gap-1"')
    except:info_company = 'N/A'
    return info_company

def JobPosts(driver):
    try:
        LIST_JOB_NAME = []
        LIST_JOB_INFO = []
        for job_name in driver.find_elements(By.CLASS_NAME, 'job-name'):
            job_name = job_name.text
            LIST_JOB_NAME+=[job_name]
    
        for job_info in driver.find_elements(By.CSS_SELECTOR, 'div[class*="mr-2 text-sm"]'):
            job_info = job_info.text
            LIST_JOB_INFO+=[job_info]

    except:
        LIST_JOB_NAME = 'N/A'
        LIST_JOB_INFO = 'N/A'
    return LIST_JOB_NAME, LIST_JOB_INFO

def CollectInfo(driver, url):
    driver.get(url);time.sleep(3)

    company_name = CompanyName(driver)
    title_company = TitleCompany(driver)
    about_company = AboutCompany(driver)
    founder_company = FounderComapny(driver)
    #tech_company = TechCompany(driver)
    social_names, link = SocialLink(driver)
    jobs_name, jobs_info = JobPosts(driver)
    
    border = '-'*40

    print(f'{RED}Company Name:{RESET}\t{GREEN}{company_name}{RESET}')
    print(border)
    print(f'{RED}Company Title:{RESET}\t{GREEN}{title_company}{RESET}')
    print(border)
    print(f'{RED}About Company:{RESET}\t{GREEN}{about_company}{RESET}')
    print(border)
    print(f'{RED}Founders Company:{RESET}\n{GREEN}{founder_company}{RESET}')
    try:
        print(border)
        number_persone = 0
        for social in social_names:
            linkedin = link[number_persone]
            person_count = number_persone+1
            print(f'{RED}Founder[{person_count}] {RESET}{GREEN}{social}:{RESET}\t{YELLOW}{linkedin}{RESET}')
            number_persone+=1
        print(border)
    except Exception as err:print(f'Error: {err}')
    try:
        number_post = 0
        for job_name in jobs_name:
            job_info = jobs_info[number_post]
            job_info = job_info.replace('\n', ' | ')
            job_count = number_post+1
            if 'Interview Process' in job_name:job_name = job_name.split('Interview Process')[0].strip()
            print(f'{RED}Job Post [{job_count}]{RESET}\t{GREEN}{job_name}\n{job_info}{RESET}')
            number_post+=1
        print(border)
    except Exception as err:print(f'Error: {err}')

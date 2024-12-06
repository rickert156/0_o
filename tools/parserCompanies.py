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

def SiteCompany(driver):
    try:
        domain_block = driver.find_element(By.CLASS_NAME, 'text-blue-600.ellipsis')
        site = domain_block.find_element(By.TAG_NAME, 'a').text
    except:site = 'N/A'
    return site

def AboutCompany(driver):
    try:about_company = driver.find_element(By.CSS_SELECTOR, 'div[class*="prose col-span-11"]').text
    except:about_company = 'N/A'
    return about_company

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

def InfoCompany(driver):
    try:info_company = driver.find_element(By.CSS_SELECTOR, '"flex flex-wrap gap-1"')
    except:info_company = 'N/A'
    return info_company

def JobPosts(driver):
    try:
        LIST_JOB_NAME = []
        LIST_JOB_INFO = []
        LIST_JOB_LINK = []

        for job_name in driver.find_elements(By.CLASS_NAME, 'job-name'):
            job_name = job_name.text
            LIST_JOB_NAME+=[job_name]
    
        for job_info in driver.find_elements(By.CSS_SELECTOR, 'div[class*="mr-2 text-sm"]'):
            job_info = job_info.text
            LIST_JOB_INFO+=[job_info]
        for job_link in driver.find_elements(By.TAG_NAME, 'a'):
            href = job_link.get_attribute('href')
            if href:
                if 'https://www.workatastartup.com/jobs/' in href:
                    LIST_JOB_LINK+=[href]

    except:
        LIST_JOB_NAME = 'N/A'
        LIST_JOB_INFO = 'N/A'
        LIST_JOB_LINK = 'N/A'
    return LIST_JOB_NAME, LIST_JOB_INFO, LIST_JOB_LINK

def CollectInfo(driver, url):
    driver.get(url);time.sleep(3)

    company_name = CompanyName(driver)
    site = SiteCompany(driver)
    title_company = TitleCompany(driver)
    about_company = AboutCompany(driver)
    social_names, link = SocialLink(driver)
    jobs_name, jobs_info, jobs_link = JobPosts(driver)

    border = '-'*40
    print(url)
    print(f'{RED}Company Name:{RESET}\t{GREEN}{company_name}{RESET} |  {YELLOW}{site}{RESET}')
    print(f'{RED}Company Title:{RESET}\t{GREEN}{title_company}{RESET}')
    print(border)
    print(f'{RED}About Company:{RESET}\t{GREEN}{about_company}{RESET}')
    try:
        print(border)
        number_persone = 0
        social_link = ''
        for social in social_names:
            linkedin = link[number_persone]
            social_link = f'{social_link}{linkedin}\n'
            person_count = number_persone+1
            print(f'{RED}Founder[{person_count}] {RESET}{GREEN}{social}{RESET}')
            number_persone+=1
        social_link = social_link.strip()
        print(f'{social_link}\n{border}')
    except Exception as err:print(f'Error: {err}')
    try:
        number_post = 0
        job = ''
        for job_name in jobs_name:
            job_info = jobs_info[number_post]
            job_link = jobs_link[number_post]
            
            job_info = job_info.replace('\n', ' | ')
            
            job_experience = job_info.split('|')[-1].strip()
            job_location = job_info.split('|')[0].strip()
            job_rests = job_info.split('|')[1:-1]
            job_rest = ''
            for job in job_rests:
                job_rest = f'{job_rest}{job} '
            
            job_count = number_post+1
            if 'Interview Process' in job_name:job_name = job_name.split('Interview Process')[0].strip()
            print(f'{RED}Job Post [{job_count}]{RESET}\t{GREEN}{job_name}: {job_link}\n{job_info}{RESET}\n')
            
            with open('testing.csv', 'a+') as file:
                write = csv.writer(file)
                write.writerow([job_name, company_name, site, job_location, job_experience, job_rest, job_info, job_link, title_company, about_company, social_link])
            
            number_post+=1
        print(border)
    except Exception as err:print(f'Error: {err}')


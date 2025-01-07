from tools.colors import RED, GREEN, YELLOW, RESET
from selenium.webdriver.common.by import By
import csv, os, time

from tools.recordResult import COMPANY_DATA_PATH 
from tools.email_report import send_email
from sql.createDB import recordDataSQLPost, recordDataSQLFounders, createTable

from tools.slack import Slack_Founders_Info, Slack_Job_Post_Info

def CompanyName(driver):
    try:company_name = driver.find_element(By.CLASS_NAME, 'company-name').text
    except:company_name = 'N/A'
    return company_name
    

def SiteCompany(driver):
    try:
        domain_block = driver.find_element(By.CLASS_NAME, 'text-blue-600.ellipsis')
        site = domain_block.find_element(By.TAG_NAME, 'a').text
    except:site = 'N/A'
    return site

def CategoryAndNumberOfEmployeesCompany(driver):
    try:
        employees = 'N/A'
        category = ''
        categories = []
        for info in driver.find_elements(By.CLASS_NAME, 'detail-label'):
            if ',' not in info.text:
                if 'people' in info.text:
                    employees = info.text
                else:
                    categories+=[info.text]

        for c in categories:
            category = f'{category}{c}'

    except:pass
    return employees, category


def AboutCompany(driver):
    try:about_company = driver.find_element(By.CSS_SELECTOR, 'div[class*="prose col-span-11"]').text
    except:about_company = 'N/A'
    return about_company

#Вот это переписать нормально!!!
def FoundersCompany(driver):
    try:
        block_founders = driver.find_element(By.CLASS_NAME, 'border-t.border-gray-200.pb-2.pt-4')
    except:block_founders = 'N/A'
    return block_founders


#До сюда


def InfoCompany(driver):
    try:info_company = driver.find_element(By.CSS_SELECTOR, '"flex flex-wrap gap-1"')
    except:info_company = 'N/A'
    return info_company

def JobPosts(driver):
    try:
        LIST_JOB_NAME = []
        LIST_JOB_INFO = []
        LIST_JOB_LINK = set()

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
                    LIST_JOB_LINK.add(href)

    except:
        LIST_JOB_NAME = 'N/A'
        LIST_JOB_INFO = 'N/A'
        LIST_JOB_LINK = 'N/A'
    return LIST_JOB_NAME, LIST_JOB_INFO, LIST_JOB_LINK

def AboutJob(driver, job_link):
    driver.get(job_link)
    try:
        about_job = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[5]').text
        if "'" in about_job:about_job = about_job.replace("'", "")
        
    except:about_job = 'N/A'
    return about_job

def CollectInfo_Y_Combinator(driver, url):
    createTable()
    
    driver.get(url);time.sleep(3)

    company_name = CompanyName(driver)
    site = SiteCompany(driver)
    employees, category = CategoryAndNumberOfEmployeesCompany(driver)
    about_company = AboutCompany(driver)

    #Переписать(выше)!
    founders = FoundersCompany(driver) 
    #!!!

    jobs_name, jobs_info, jobs_link = JobPosts(driver)

    border = '-'*40
    print(url)
    print(f'{RED}Company Name:{RESET}\t{GREEN}{company_name}{RESET} |  {YELLOW}{site}{RESET}')
    print(border)
    print(f'{RED}About Company:{RESET}\t{GREEN}{about_company}{RESET}')
    
    try:
        print(border)
        
        number_founder = 0
        for founder in founders.find_elements(By.CLASS_NAME, 'mb-4'):
            number_founder+=1
            
            full_name = founder.text.split('\n')[0]
            about_persone = founder.text.split('\n')[1]
            
            first_name = full_name.split(' ')[0]
            last_name = full_name.split(' ')[-1]
            
            try:
                linkedin = founder.find_element(By.TAG_NAME, 'a')
                linkedin = linkedin.get_attribute('href')
            except:linkedin = 'N/A'

            data_check_post = time.strftime("%d/%m/%Y %H:%m")

            print(f'{RED}[{number_founder}]{RESET} {GREEN}{full_name}\nFirst Name: {first_name} | Last Name: {last_name}{RESET} {linkedin}\n{GREEN}{about_persone}{RESET}')

            recordDataSQLFounders(first_name, last_name, about_persone, linkedin, company_name, data_check_post)
            
            #Уведомление в Slack
            #Slack_Founders_Info(company_name=company_name, first_name=first_name, last_name=last_name, linkedin=linkedin, about_persone=about_persone)

        print(f'{border}')



    except Exception as err:print(f'Error: {err}')
    try:
        jobs_new_list = []
        for link in jobs_link:
            jobs_new_list+=[link]

        number_post = 0
        job = ''
        for job_name in jobs_name:
            job_info = jobs_info[number_post]
            job_link = jobs_new_list[number_post]
            
            job_info = job_info.replace('\n', ' | ')
            
            job_experience = job_info.split('|')[-1].strip()
            job_location = job_info.split('|')[0].strip()
            job_type = job_info.split('|')[1]

            job_count = number_post+1
            if 'Interview Process' in job_name:job_name = job_name.split('Interview Process')[0].strip()
            print(f'{RED}Job Post [{job_count}]{RESET}\t{GREEN}{job_name}: {job_link}\n{job_info}{RESET}')

            about_job = AboutJob(driver, job_link)
            
            print(f'\n{RED}About Job:{RESET}\t{GREEN}{about_job}{RESET}\n')
            
            data_check_post = time.strftime("%d/%m/%Y %H:%m")
            

            with open(COMPANY_DATA_PATH, 'a+') as file:
                write = csv.writer(file)
                write.writerow([job_name, company_name, site, job_location, job_experience, job_type, employees, category, about_job, job_link, about_company, 'Y-Combinator', data_check_post])
            
            if "'" in about_company:about_company = about_company.replace("'", "")
            
            recordDataSQLPost(job_name, company_name, site, job_location, job_experience, job_type, employees, category, about_job, job_link, about_company, 'Y-Combinator', data_check_post)
            
            #Уведомление в Slack
            #Slack_Job_Post_Info(company_name=company_name, job_name=job_name, about_job=about_job, category_company=category, link_job=job_link)
            
            
            send_email(job_name, company_name, job_link, 'Y-Combinator')
            number_post+=1
        print(border)
    except Exception as err:print(f'Error block Jobs: {err}')
    print(f'{RED}Employees:{RESET}\t{GREEN}{employees}{RESET}')
    print(f'{RED}Category:{RESET}\t{GREEN}{category}{RESET}')
    

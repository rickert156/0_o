from sql.createDB import recordDataSQL, createTable
from tools.recordResult import COMPANY_DATA_PATH
import csv

def move_data_to_sql():
    createTable()
    with open(COMPANY_DATA_PATH, 'r', encoding='utf-8') as file:
        number_post = 0
        for row in csv.DictReader(file):
            number_post+=1
            job_title = row['Job Title']
            company = row ['Company']
            site = row['Site']
            location = row['Location']
            experience = row['Experience']
            add_info = row['Additional information']
            employees = row['Employees']
            category = row['Category']
            link_post = row['Link Post']
            title_company = row['Title Company']
            about_company = row['About Company']
            link_founders =row['Link Founders']
            platform = row['Platform']
            print(f'{number_post} {job_title}')
            if "'" in title_company:title_company = title_company.replace("'", " ")
            if "'" in about_company:about_company = about_company.replace("'", " ")
            recordDataSQL(job_title, company, site, location, experience, add_info, employees, category, link_post, title_company, about_company, link_founders, platform)

move_data_to_sql()

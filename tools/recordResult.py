import csv, os

BASE_COMPANIES_DIR = 'Companies'
BASE_COMPANIES_FILE = 'all_companies.csv'
PATH_COMPANIES_FILE = f'{BASE_COMPANIES_DIR}/{BASE_COMPANIES_FILE}'

COMPANY_DATA_FILE = 'all_data.csv'
COMPANY_DATA_PATH = f'{BASE_COMPANIES_DIR}/{COMPANY_DATA_FILE}'

def checkDir():
    global BASE_COMPANIES_DIR, BASE_COMPANIES_FILE, PATH_COMPANIES_FILE, COMPANY_DATA_PATH, COMPANY_DATA_FILE
    if not os.path.exists(PATH_COMPANIES_FILE):
        os.makedirs(BASE_COMPANIES_DIR)
        with open(PATH_COMPANIES_FILE, 'a') as file:
            file.write('')
    
    if not os.path.exists(COMPANY_DATA_PATH):
        with open(COMPANY_DATA_PATH, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Job Title', 'Company', 'Site', 'Location', 'Experience', 'Additional information', 'Employees', 'Category', 'Information', 'Link Post', 'Title Company', 'About Company', 'Link Founders', 'Platform'])



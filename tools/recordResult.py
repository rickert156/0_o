import csv, os

BASE_COMPANIES_DIR = 'Companies'
BASE_COMPANIES_FILE = 'all_companies.csv'
PATH_COMPANIES_FILE = f'{BASE_COMPANIES_DIR}/{BASE_COMPANIES_FILE}'

def checkDir():
    global BASE_COMPANIES_DIR, BASE_COMPANIES_FILE, PATH_COMPANIES_FILE
    if not os.path.exists(PATH_COMPANIES_FILE):
        os.makedirs(BASE_COMPANIES_DIR)
        with open(PATH_COMPANIES_FILE, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Link', 'Source'])


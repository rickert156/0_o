from selenium.webdriver.common.by import By
from tools.colors import RED, GREEN, RESET
from tools.recordResult import checkDir, PATH_COMPANIES_FILE
from tools.statusScrapy import statusParser
from tools.parserCompanies import CollectInfo
import os, csv

LIST_LINK_IN_DOC = []

def readFileLink():
    global PATH_COMPANIES_FILE, LIST_LINK_IN_DOC

    with open(PATH_COMPANIES_FILE, 'r') as file:
        for row in csv.DictReader(file):
            email = row['Link']
            LIST_LINK_IN_DOC+=[email]

def scrapyLinks(driver):
    global LIST_LINK_IN_DOC, PATH_COMPANIES_FILE
    SET_LINK = set()

    checkDir()

    for links in driver.find_elements(By.TAG_NAME, 'a'):
        link = links.get_attribute('href')
        if link and '/companies/' in link:
            if '/website' in link:link = link.split('/website')[0]
            SET_LINK.add(link)

    number_link = 0
    for link in SET_LINK:
        readFileLink()
        number_link+=1
        if link not in LIST_LINK_IN_DOC:
            with open(PATH_COMPANIES_FILE, 'a+') as file:
                write = csv.writer(file)
                write.writerow([link, 'Y-Combinator'])
                print(f'{GREEN}[{number_link}]{RESET} {RED}{link}{RESET}')
                CollectInfo(driver, link)
                print('\n')



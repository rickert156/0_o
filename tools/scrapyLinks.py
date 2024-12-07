from selenium.webdriver.common.by import By
from tools.colors import RED, GREEN, RESET
from tools.recordResult import checkDir, PATH_COMPANIES_FILE
from tools.parserCompanies import CollectInfo
import os, csv

LIST_LINK_IN_DOC = []

def readFileLink():
    global PATH_COMPANIES_FILE, LIST_LINK_IN_DOC

    with open(PATH_COMPANIES_FILE, 'r') as file:
        for row in file.readlines():
            link = row.strip()
            LIST_LINK_IN_DOC+=[link]

def scrapyLinks(driver):
    global LIST_LINK_IN_DOC, PATH_COMPANIES_FILE
    SET_LINK = set()

    checkDir()

    for links in driver.find_elements(By.TAG_NAME, 'a'):
        link = links.get_attribute('href')
        if link and '/companies/' in link and '/website' not in link:
            SET_LINK.add(link)

    number_link = 0
    

    

    for link in SET_LINK:
        number_link+=1
        if link not in LIST_LINK_IN_DOC:
            readFileLink()
            with open(PATH_COMPANIES_FILE, 'a+') as file:
                file.write(f'{link}\n')
                print(f'{GREEN}[{number_link}]{RESET} {RED}{link}{RESET}')
                CollectInfo(driver, link)
                print('\n')



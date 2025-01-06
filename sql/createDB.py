import sqlite3
from sql.commands import create_table_job_post, create_table_founders

SQL_BASE = 'job_posts.db'

def createTable():
    global SQL_BASE

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()

    try:
        cursor.execute(create_table_job_post)
        cursor.execute(create_table_founders)
    except Exception as err:print(f'Error: {err}')


def recordDataSQLPost(job_title, company, site, location, experience, job_type, employees, category_company, about_job, link_post, about_company, platform, data_check_post):
    global SQL_BASE

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()
    
    record_sql_post = f'''
    INSERT INTO job_posts (job_title, company, site, location, experience, job_type, employees, category_company, about_job, link_post, about_company, platform, data_check_post)
    VALUES ('{job_title}', '{company}', '{site}', '{location}', '{experience}', '{job_type}', '{employees}', '{category_company}', '{about_job}', '{link_post}', '{about_company}', '{platform}', '{data_check_post}');
    '''
    try:cursor.execute(record_sql_post)
    except sqlite3.DatabaseError as err:print(f'Error: {err}')
    else:
        print('Record Post')
        conn.commit()
    
    cursor.close()
    conn.close()

def recordDataSQLFounders(first_name, last_name, about_persone, linkedin, data_check_post):
    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()

    record_sql_founders = f'''
    INSERT INTO founders (first_name, last_name, about_persone, linkedin, data_check_post)
    VALUES ('{first_name}', '{last_name}', '{about_persone}', '{linkedin}', '{data_check_post}')
    '''
    try:cursor.execute(record_sql_founders)
    except sqlite3.DatabaseError as err:print(f'Error: {err}')
    else:
        print('Record Founders')
        conn.commit()
    cursor.close()
    conn.close()

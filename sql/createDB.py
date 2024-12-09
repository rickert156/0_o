import sqlite3
from sql.commands import create_table_post

SQL_BASE = 'job_posts.db'

def createTable():
    global SQL_BASE

    conn = sqlite3.connect(SQL_BASE)
    cursor = conn.cursor()

    try:cursor.execute(create_table_post)
    except Exception as err:print(f'Error: {err}')


def recordDataSQL(job_title, company, site, location, experience, job_type, employees, category_company, about_job, link_post, about_company, platform, data_check_post):
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
        print('Record Data')
        conn.commit()
    
    cursor.close()
    conn.close()

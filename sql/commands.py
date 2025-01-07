create_table_job_post = """
CREATE TABLE IF NOT EXISTS job_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    site TEXT,
    location TEXT,
    experience TEXT,
    job_type TEXT,
    employees TEXT,
    category_company TEXT,
    about_job TEXT,
    link_post TEXT,
    about_company TEXT,
    platform TEXT,
    data_check_post TEXT
)
"""

create_table_founders = """
CREATE TABLE IF NOT EXISTS founders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    about_persone TEXT,
    linkedin TEXT,
    company_name TEXT,
    data_check_post TEXT
)
"""

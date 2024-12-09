create_table_post = """
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



create_table_post = """
CREATE TABLE IF NOT EXISTS job_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    site TEXT,
    location TEXT,
    experience TEXT,
    additional_information TEXT,
    employees TEXT,
    category_company TEXT,
    information TEXT,
    link_post TEXT,
    title_company TEXT,
    about_company TEXT,
    link_founders TEXT,
    platform TEXT
)
"""



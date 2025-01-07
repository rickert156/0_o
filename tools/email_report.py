import smtplib, random, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tools.colors import RED, GREEN, RESET, YELLOW
from config import send_to


def email_user_login_file():
    dir_account = 'email'
    file_email = 'email.csv'
    path_file_email = f'{dir_account}/{file_email}'

    return path_file_email

def random_number(path:str=email_user_login_file()):
    with open(path, 'r') as file:
        number_string, number_last_line = 0, 0
        for row in file.readlines():
            number_string+=1
            number_last_line = number_string-1

    random_number = random.randint(1, number_last_line)
    return random_number

def select_email_user(path:str=email_user_login_file()) -> str:
    
    select_user = int(random_number())

    with open(path, 'r') as file:
        number_login = 0
        for row in csv.DictReader(file):
            number_login+=1
            if number_login == select_user:
                login = row['login']
                password = row['password']
            
                return login, password
    

def send_email(job_title, company_name, link_post, platform):
    email_text = f"""
    Hi, new Job Post!

    Platform search: {platform}

    Job Title: {job_title}
    Company Name: {company_name}
    Link Job Post: {link_post}
    """

    sender, password = select_email_user()

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = send_to
    msg['Subject'] = f'New Job Post: {company_name}'
    msg.attach(MIMEText(email_text, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
        server.login(sender, password)
        server.sendmail(sender, send_to, msg.as_string())
        server.quit()
        print(f'{YELLOW}[+] Letter sent {RESET}\n')
    except Exception as err:
        print(f'{RED}[x] Error: {err}{RESET}\n')
        send_email(job_title, company_name, link_post, platform)



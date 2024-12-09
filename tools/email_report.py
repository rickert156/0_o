import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tools.colors import RED, GREEN, RESET, YELLOW
from email_login import sender, password, send_to

def send_email(job_title, company_name, link_post, platform):
    email_text = f"""
    Hi, new Job Post!

    Platform search: {platform}

    Job Title: {job_title}
    Company Name: {company_name}
    Link Job Post: {link_post}
    """

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

#send_email('Company Title', 'Company Name', 'https://google.com', 'Y-Combinater')


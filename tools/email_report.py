import smtplib
from tools.colors import RED, GREEN, RESET
from email import sender, password

def sead_email(job_title, company_name, link_post, platform):
    email_text = f"""

    Hi, new Job Post!

    Platform search: {platform}

    Job Title: {job_title}
    Company Name: {company_name}
    Link Job Post: {link_post}
    """

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email_to
    msg['Subject'] = 'New Job Post!'
    msg.attach(MIMEText(email_text, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
        server.login(sender, password)
        server.sendemail(sender, email_to, msg.as_string())
        server.quit()
        print(f'{GREEN}[+] Send letter... {RESET}')
    except Exception as err:
        print(f'{RED}[x] Error: {err}{RESET}')

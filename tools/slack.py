import requests
from config import slack_hook

tire = '-'*60

def Slack_Founders_Info(company_name:str=None, first_name:str=None, last_name:str=None, linkedin:str=None, about_persone:str=None):
    
    message = f'Company Name:\t{company_name}\nFounder:\tName: {first_name} {last_name}\nAbout Founder: {about_persone}\n\n{linkedin}\n\n'

    data = {
            'Content-type':'application/json',
            'text':message
            }

    notification = requests.post(slack_hook, json=data)
    status_slack = notification.status_code
    if status_slack == 200:print('Founder: Message sent to Slack')
    else:print(f'Founder: Status Slack: {status_slack}')
    
def Slack_Job_Post_Info(company_name:str=None, job_name:str=None, about_job:str=None, category_company:str=None, link_job:str=None):
    

    message = f'Job Post:\t{link_job}\nJob Title:\t{job_name}\nCompany Name:\t{company_name}\nCategory Company:\t{category_company}\n\n'

    data = {
            'Content-type':'application/json',
            'text':message
            }
 
    notification = requests.post(slack_hook, json=data)
    status_slack = notification.status_code
    if status_slack == 200:print('Job Post: Message sent to Slack')
    else:print(f'Job Post: Status Slack: {status_slack}')
    

def DividePost():
    message = '-'*40
    data = {
            'Content-type':'application/json',
            'text':message
            }
    notification = requests.post(slack_hook, json=data)


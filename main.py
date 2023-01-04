import datetime as dt
import smtplib
import random
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv('projects\\Birthday Wisher  start\\.env')

my_email=os.getenv('MY_EMAIL')
password=os.getenv('MY_EMAIL_PASS')

random_num=random.randint(1,3)

with open(file=f'.\\projects\\Birthday Wisher  start\\letter_templates\\letter_{random_num}.txt') as file:
    letter_content = file.read()


data=pd.read_csv('.\\projects\\Birthday Wisher  start\\birthdays.csv')
info=data.to_dict(orient='records')

now=dt.datetime.now()

for i in info:
    if now.year==i['year'] and now.month==i['month'] and now.day==i['day']:  
        letter_content = letter_content.replace('[NAME]',i['name'])        
        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i['email'],
                msg=f'Subject:Birthday Card\n\n{letter_content}'
            )










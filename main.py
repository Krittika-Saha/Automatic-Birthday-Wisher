##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pds
import datetime as dt
from smtplib import SMTP
from random import randint
file = open('file.txt', 'r')
email = file.readlines()[0].strip('\n')
password = open('file.txt', 'r').readlines()[1]
file.close()
data = pds.read_csv('birthdays.csv').to_dict(orient='records')
print(data)
with SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=email, password=password)
  for i in data:
    if dt.datetime.now().day == data[i]['day']:
        with open(f'letter_templates/letter_{randint(1, 3)}.txt') as file:
          letter_content = file.read().replace('[NAME]', data[i]['name'])
          connection.sendmail(from_addr=email, to_addrs=data[i]['email'], msg=f"""Subject:Happy Birthday, {data[i]['name']}!\n\n
  {letter_content}""")


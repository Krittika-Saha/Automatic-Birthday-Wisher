import smtplib
import datetime as dt
from random import choice

quote_list = []
with open('file.txt', 'r') as file:
  email = file.readlines()[0].strip('\n')
  password = open('file.txt', 'r').readlines()[1]


for i in range(101):
  quote_list.append(open('quotes.txt', 'r', encoding='utf8').readlines()[i].strip('\n'))
with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=email, password=password)
  if dt.datetime.now().weekday() == 1:
    connection.sendmail(from_addr=email, to_addrs='', msg=f"""
Subject:Inspiration Quotes\n\n
Helloooo! This is the Monday Morning inspiration quote article\n
Your quote for today is:\n   {choice(quote_list)}\n""")

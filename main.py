import smtplib

with open('file.txt', 'r') as file:
  email = file.readlines()[0].strip('\n')
  password = open('file.txt', 'r').readlines()[1]

with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=email, password=password)
  connection.sendmail(from_addr=email, to_addrs='krittika.saha.dev@gmail.com', msg='Subject:Hello\n\nThis is the content of my email')





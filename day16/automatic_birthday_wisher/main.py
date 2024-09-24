import smtplib
import random
import  datetime as dt
import pandas as pd


#---------------ACCOUNT DETAILS SETUP -----------------#
my_account = 'code0aryan@gmail.com'
passwd = 'ufvavjgsaduqhofi'

#-------------CHOOSING LETTER FORMAT------------#
letter_formats = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt']
letter_format = random.choice(letter_formats)

#-----------GETTING DATES------------#
now = dt.datetime.now()
birthday_data = pd.read_csv('birthdays.csv')
current_month = now.month
current_day = now.day


#---------FUNCTIONALITY--------#
for index,row in birthday_data.iterrows():
    if row.month == current_month and row.day == current_day:
        name = row['name']
        receiving_addr = row['email']

        with open(letter_format,'r') as file:
            letter = file.read()
            letter = letter.replace('[NAME]',name)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_account,password=passwd)
            connection.sendmail(
                from_addr=my_account,
                to_addrs=receiving_addr,
                msg = f'Subject: WISHING YOU A VERY HAPPY BIRTHDAY!! \n\n {letter}!'
            )



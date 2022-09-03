import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "example@mail.com"
GMAIL_PASSWORD = "password to MY_EMAIL"

birthdays_data = pandas.read_csv('birthdays.csv').to_dict(orient='records')
now = dt.datetime.now()

for birthday in birthdays_data:

    if int(now.month) == int(birthday['month']) and int(now.day) == int(birthday['day']):
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as f:
            letter = f.read()
            letter_to_send = letter.replace('[NAME]', birthday['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday['email'],
                                msg=f"Subject:Happy Birthday\n\n{letter_to_send}")

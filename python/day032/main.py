import random
import smtplib
import datetime as dt

MY_EMAIL = "example@mail.com"
TO_EMAIL = "example2@mail.com"
GMAIL_PASSWORD = "password to MY_EMAIL"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:

    with open("quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=f"{quote}")



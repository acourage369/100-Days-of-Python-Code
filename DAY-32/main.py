# Automated Birthday Wisher
# cadzewoda@yahoo.com
# acourage009@gmail.com

import smtplib
import datetime as dt

import random

my_email = "acourage009@gmail.com"
my_password = "xpuwtllspiwerqml"
recipient_mail = "cadzewoda@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_mail,
            msg=f"Subject:Monday Motivations\n\n{quote}"
        )


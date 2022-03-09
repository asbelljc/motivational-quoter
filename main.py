from dotenv import load_dotenv
import os
import smtplib
import datetime as dt
import random

load_dotenv()

SMTP = os.getenv('SMTP')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


weekday = dt.datetime.now().weekday()

if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, to_addrs=EMAIL, msg=f'Subject:MONDAY MOTIVATION\n\n{quote}'
        )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import os
import random
import smtplib

import pandas as pd

file = "quotes.txt"
sender_email = "xxx.gmail.com"
receiver_email = "yyy.gmail.com"
password = "123456"

current_date = dt.datetime.now()
month = current_date.month
day = current_date.day

def pick_random_temp():
    template_dir = "letter_templates"
    letters = os.listdir(template_dir)
    random_letter = random.choice(letters)
    return os.path.join(template_dir, random_letter)

def get_letter():
    file = pick_random_temp()
    with open(file) as f:
        content = f.read()
        new_content = content.replace("[NAME]", line.get("name"))
        return new_content

def send_mail(to, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg=f"Subject:Happy birthday!\n\n{message}"
        )

data = pd.read_csv("birthdays.csv")
parsed_data = data.to_dict(orient="records")
for line in parsed_data:
    if line.get("month") == month and line.get("day")==day:
        letter = get_letter()
        send_mail(line.get("email"), letter)


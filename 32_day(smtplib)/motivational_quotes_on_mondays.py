import datetime as dt
import random
import smtplib


file = "quotes.txt"
sender_email = "xxx.gmail.com"
receiver_email = "yyy.gmail.com"
password = "123456"

def pick_rand_quote():
    global file
    try:
        with open(file=file, mode="r", encoding="utf-8") as file:
            quotes = file.readlines()
        return random.choice(quotes)
    except FileNotFoundError:
        print("File Not Found")


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=f"Subject:Motivation\n\n{message}"
        )



current_day = dt.datetime.now()
current_day_of_week = current_day.weekday()
print(current_day_of_week)
if current_day_of_week == 0:
    quote = pick_rand_quote()
    print(quote)
    send_email(quote)



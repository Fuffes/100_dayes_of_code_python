# import smtplib
#
# my_email = ""
# password = ""
#
#
# try:
#     # Connect to Gmail's SMTP server (corrected hostname)
#     with smtplib.SMTP("smtp.gmail.com", 587)  as connection:
#         connection.starttls()  # Encrypt the connection
#         connection.login(user=my_email, password=password)
#
#         # Send the email
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="kuxad@mailto.plus",
#             msg="Subject: Hello\n\nThis is the email body."
#         )
#     print("Email sent successfully!")
#
# except smtplib.SMTPException as e:
#     print(f"SMTP Error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")


# import datetime as dt
#
# data = dt.datetime.now()
# year = data.year
# month = data.month
# day_of_week = data.weekday()
# print(data.year)
#
# date_of_birth = dt.datetime(year=2000, month=12, day=26, hour=4)


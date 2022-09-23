# import smtplib
#
# my_email = "kumrev2003@gmail.com"
# password = "revathi2019"
# # connection = smtplib.SMTP("smtp.gmail.com",port=587)
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # the below line makes our connection secure and send the message encrypted
#     connection.starttls()
#     connection.login(user="kumrev2003@gmail.com", password="revathi2019")
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="saipai20000@gmail.com",
#                         msg="subject:hello\n\nthis is the body of the mail")
#     # connection.close()

# import datetime as dt
#
# now=dt.datetime.now()
# year=now.year
# day_of_week=now.weekday()
# print(day_of_week)
#
# day_of_birth=dt.datetime(day=26,month=9,year=2003)
# print(day_of_birth)

# --------------------automatic monday motivational mail-------------------#
import random
import smtplib
import datetime as dt

with open("quotes.txt") as file:
    data = file.readlines()


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="kumrev2003@gmail.com", password="revathi2019")
        connection.sendmail(from_addr="kumrev2003@gmail.com",
                            to_addrs="saipai20000@gmail.com",
                            msg=f"subject:Motivation\n\n{random.choice(data)}")


now = dt.datetime.now()
week_of_day = now.weekday()
print(week_of_day)
if week_of_day == 4:
    send_mail()

# import smtplib
#
# MY_EMAIL = "vicmanuelr@gmail.com"
# password = "jktkofxgfysnngyu"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL,  password=password)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="victorponce.r@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year == 2022:
#     print("Wear a face mask")
#
# date_of_birth = dt.datetime(year=1986, month=5, day=14)

import smtplib
import random as rn
import datetime as dt

MY_EMAIL = "vicmanuelr@gmail.com"
MY_PASSWORD = "jktkofxgfysnngyu"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open("./data/quotes.txt") as f:
        quotes_list = f.readlines()
        random_quote = rn.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as msg:
        msg.starttls()
        msg.login(user=MY_EMAIL, password=MY_PASSWORD)
        msg.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="flor.arguijoj@gmail.com",
            msg=f"Subject:Monday Motivation!\n\n{random_quote}",
        )

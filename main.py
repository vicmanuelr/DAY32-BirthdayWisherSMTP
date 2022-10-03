import pandas as pd
import datetime as dt
import random as rn
import smtplib

# ----------------------------------- Extra Hard Starting Project ----------------------------------------#
today = dt.datetime.now()
data = pd.read_csv("./data/birthdays.csv")
birthday_list = data.to_dict(orient="records")


def is_birthday(date_of_birth, today_date):
    birthday = dt.datetime(year=date_of_birth["year"], month=date_of_birth["month"], day=date_of_birth["day"])
    if birthday.day == today_date.day and birthday.month == today_date.month:
        return True


def random_letter(celebrant):
    for person in celebrant:
        name = person[0]
        email = person[1]
        random_letter_number = rn.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter_number}.txt") as lt:
            letter = lt.read()
        final_letter = letter.replace("[NAME]", name)
        send_email(final_letter, email)


def send_email(message, email_address):
    MY_EMAIL = "vicmanuelr@gmail.com"
    MY_PASSWORD = "jktkofxgfysnngyu"
    with smtplib.SMTP("smtp.gmail.com", port=587) as msg:
        msg.starttls()
        msg.login(user=MY_EMAIL, password=MY_PASSWORD)
        msg.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=f"Subject:Happy Birthday!\n\n{message}",
        )


def birthday_wisher(list_data, today_date):
    birthdays = [(entry["name"], entry["email"]) for entry in list_data if is_birthday(entry, today_date)]
    if len(birthdays) > 0:
        random_letter(birthdays)


birthday_wisher(birthday_list, today)

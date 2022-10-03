import pandas as pd
import datetime as dt

# ----------------------------------- Extra Hard Starting Project ----------------------------------------#
# TODO 2. Check if today matches a birthday in the data_list.csv
today = dt.datetime.now()
data_list = pd.read_csv("./data/birthdays.csv")
data_list = data_list.to_dict(orient="records")


def is_birthday(test_data):
    birthday = dt.datetime(year=test_data["year"], month=test_data["month"], day=test_data["day"])
    if birthday.day == today.day and birthday.month == today.month:
        return True


def search_data(list_data):
    for entry in list_data:
        if is_birthday(entry):
            # generate_letter(random_letter)
            print(entry["name"])


search_data(data_list)

# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from data_list.csv

# TODO 4. Send the letter generated in step 3 to that person's email address.

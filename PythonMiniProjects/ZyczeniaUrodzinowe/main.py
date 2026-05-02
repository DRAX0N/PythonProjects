import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
day = now.day
month = now.month

my_email = "darmowe.gry.na.steama@gmail.com"
password = "1!QWaszx"

with open("birthdays.csv", "r", encoding="utf8") as data:
    table = pandas.read_csv(data)

day_list = table.day
month_list = table.month

list_of_lists = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for n in range(len(table)):
    if day == day_list[n] and month == month_list[n]:
        name = table.name[n]
        mail = table.email[n]

        list = random.choice(list_of_lists)

        with open(f"listy/{list}") as text:
            new_letter = text.read().replace("[NAME]", name.strip())

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="darmowe.gry.na.steama@gmail.com", password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=mail,
                msg=f"Subject:Happy birthday\n\n{new_letter}"
            )


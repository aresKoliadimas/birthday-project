##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
let_list = ["letter_1", "letter_2", "letter_3"]
rand_letter = random.choice(let_list)
df = pandas.read_csv("birthdays.csv")

with open(f"letter_templates/{rand_letter}.txt", "r") as letter:
    letter_to_send = letter.read()

for i in range(len(df)):
    if now.month == df['month'][i] and now.day == df['day'][i]:
        ready_letter = letter_to_send.replace("[NAME]", df['name'][i])

# with smtplib.SMTP("smtp@gmail.com") as connection:
#     connection.starttls()
#     connection.login(user="ariskoliadimas@gmail.com", password="abcd123")
#     connection.sendmail(
#         from_addr="ariskoliadimas@gmail.com",
#         to_addrs="test@gmail.com",
#         msg=f"Subject:Happy Birthday\n\n{ready_letter}"
#     )

print(f"Subject:Happy Birthday\n\n{ready_letter}")

import datetime
from datetime import date
import requests
import simplejson as json

response = requests.get("https://api.covidtracking.com/v1/states/daily.json")

json_test = response.json()

print("Enter the state for which the COVID data should be retrieved (e.g. TX): ")
user_state = input()
print("Enter the date for which the COVID data should be retrieved (e.g. 20201219): ")
user_date = input()
status = False

count = 0
for i in json_test:
    i = count
    count = count + 1
    state = (json_test[i]['state'])
    dates = (json_test[i]['date'])
    death = (json_test[i]['death'])
    positive = (json_test[i]['positive'])
    positiveIncrease = (json_test[i]['positiveIncrease'])
    deathIncrease = (json_test[i]['deathIncrease'])

    if state == user_state and str(dates) == user_date:
        status = True
        cv_state = state
        cv_date = dates
        cv_death = death
        cv_positive = positive
        cv_positiveIncrease = positiveIncrease
        cv_deathIncrease = deathIncrease
        print(" ")
        print("=======================")
        print("State: " + str(cv_state))
        print("Date: " + str(cv_date))
        print("Positive Cases: " + str(cv_positive))
        print("Death(s): " + str(cv_death))
        print("=======================")
        print(" ")
if(status==False):
    print("No Records")
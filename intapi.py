import requests
import json
import maya
import datetime
import arrow

print("Podaj loasgashgasgsagsaggin")
user = input()
link = "https://api.github.com/users/" + user
response = requests.get(link)

x = response.json()

print(x["login"])
print(x["name"])
print(x["avatar_url"])
dt = maya.parse(x["created_at"]).datetime()
print(dt.date())

print('')
dt = maya.parse(x["created_at"]).datetime()
a = arrow.get(datetime.date.today())
print(a)
b = arrow.get(dt.date())
print(b)

delta = (a-b)

print(delta.days)

# do poprawienia przypadek godzinowy

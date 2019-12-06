import requests
import json

link = "https://api.github.com/users/AceLewis/repos"
username = 'kkaz2611'
token = '852a807853a522d05542a30ff40c468ad02f2299'
request = requests.get(link, auth = (username, token))
json = request.json()
for i in range(0,len(json)):
    print("Project Number:",i+1)
    print("Project Name:",json[i]['name'])
    print("Project URL:",json[i]['svn_url'])
    print("Project description:", json[i]['description'])
    x = json[i]['languages_url']
    # print(x)
    request2 = requests.get(x, auth=(username,token))
    json2 = request2.json()
    suma = 0
    for j in json2.values():
        suma += int(j)
    for k, v in json2.items():
        zmienna = int(v)
        zmienna /= suma
        zmienna *= 100
        print(k, v, "   procentowy udzial: " + "{0:.2f}".format(round(zmienna,2)))
    print('')
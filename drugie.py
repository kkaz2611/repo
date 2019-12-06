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

    x = json[i]['commits_url']
    x = x.replace('{/sha}', '')
    print('')

    request3 = requests.get(x, auth=(username, token))
    json3 = request3.json()

    wielkosctablicy = len(json3)

    if wielkosctablicy > 3:
        wielkosctablicy = 3

    for l in range(0, wielkosctablicy):
        print("Commit number:", l+1)
        print("Commit author:", json3[l]['commit']['author']['name'])
        print("Commit author's email:", json3[l]['commit']['author']['email'])
        print("Commit date:", json3[l]['commit']['author']['date'])
        print("Commit message: ", json3[l]['commit']['message'])
        print("")

    print("\n \n ##########################################################")


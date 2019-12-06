import subprocess
import json
result = subprocess.check_output(['bash', 'skrypt.sh'])
#print(result)
pom2 = []
x = result.split('\n')
for i in x:
    pom = i.split('-')
    pom2.append(pom)

# print(pom2)

# for i in range(0, len(pom2)):
#     print(pom2[i])
# print(len(pom2))

pom = {}
b = []
for i in range(0,len(pom2)-1):
    pom['name'] = pom2[i][0]
    pom['path'] = pom2[i][1]
    b.append(dict(pom))
    #print(pom, "\n\n")

y = json.dumps(b, indent = 4)
print(y)
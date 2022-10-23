import json

file = open('saved-data.json', 'r')

jsonfile = json.load(file)


print(sum(i.count(255) for i in jsonfile))
print(sum(i.count(0) for i in jsonfile))
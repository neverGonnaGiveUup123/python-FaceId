import json,math

file = open('sid-saved-data.json', 'r')

jsonfile = json.load(file)


whiteValues = sum(i.count(255) for i in jsonfile)
blackValues = sum(i.count(0) for i in jsonfile)

print(whiteValues)
print(blackValues)

print(whiteValues / 10000)
print(blackValues / 10000)

if math.isclose(whiteValues / 10000, 2.8,abs_tol=0.2):
    print("Hello Siddharth"), print(whiteValues)
else:
    print("Your not Siddharth"), print(whiteValues)
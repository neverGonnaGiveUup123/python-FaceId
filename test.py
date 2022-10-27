import json,math


file = open('sid-saved-data.json', 'r')

jsonfile = json.load(file)

lightAverage = jsonfile[-1]

print(lightAverage)

whiteValues = 0
blackValues = 0


for i in jsonfile[:-2]:
    for j in i:
        for x in j:
            if x == 255:
                whiteValues += 1
            elif x == 0:
                blackValues += 1

print(whiteValues)
print(blackValues)

print(whiteValues / 10000)
print(blackValues / 10000)

if len(str(whiteValues)):
    pass
    #Will add stuff in future

if math.isclose(whiteValues / 10000, 2.8,abs_tol=0.2):
    print("Hello Siddharth"), print(whiteValues)
else:
    print("Your not Siddharth"), print(whiteValues)


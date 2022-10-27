import cv2 as cv
import numpy as np
import json

camera = cv.VideoCapture(0)


lightAverage = 0

DATA = [None,None,None,None,None]


haarcas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

if not camera.isOpened():
    print("Failed to open selected camera.")
    exit()

e = 0
counter = 0
checkCounter = False

while True:
    check, frame = camera.read()

    if not check:
        print("Camera has a skill issue.")
        break

    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    lightValue = np.mean(grey)

    detectedFace = haarcas.detectMultiScale(grey,scaleFactor = 1.05, minNeighbors=6,minSize=[30,30])

    for x,y,w,h in detectedFace:
        if w*h <= 50000:
            cv.putText(grey,"Closer",(240,100),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        elif w*h >= 50000 and counter < 20:
            grey = cv.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),2)
            thresh = grey[x:x+w, y:y+h]
            babaaaaaaaaaaaa,threshBinary = cv.threshold(thresh,lightValue,255,cv.THRESH_BINARY)
            print(counter) 

            DATA[counter] = threshBinary.tolist()
            
            lightAverage += lightValue
            counter +=1

            if counter >= 5:
                lightAverage = lightAverage / 5
                DATA.append(lightAverage)
                with open("sid-saved-data.json","w") as file:
                    json.dump(DATA,file)
                print(lightAverage)
                quit()

            cv.imshow("EEE",threshBinary)
            # print(threshBinary)
            
        else:
            quit()


    cv.imshow("HHH",grey)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()

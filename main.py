import cv2 as cv
import numpy as np
import json

camera = cv.VideoCapture(0)

haarcas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

if not camera.isOpened():
    print("Failed to open selected camera.")
    exit()

e = 0

while True:
    check, frame = camera.read()

    if not check:
        print("Camera has a skill issue.")
        break

    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    detectedFace = haarcas.detectMultiScale(grey,scaleFactor = 1.05, minNeighbors=6,minSize=[30,30])

    for x,y,w,h in detectedFace:
        if w*h <= 50000:
            cv.putText(grey,"Closer",(240,100),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        elif w*h >= 50000:
            grey = cv.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),2)
            thresh = grey[x:x+w, y:y+h]
            babaaaaaaaaaaaa,threshBinary = cv.threshold(thresh,100,255,cv.THRESH_BINARY)

            if e == 0:
                with open("saved-data.json","w") as file:
                    json.dump(threshBinary.tolist(),file)
                e = 1

            cv.imshow("EEE",threshBinary)
            print(threshBinary)
            
        else:
            print("Error")


    cv.imshow("HHH",grey)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()

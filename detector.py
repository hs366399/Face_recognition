import cv2
import os
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('Harcascade FIles\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

rec = cv2.createLBPHFaceRecognizer()
rec.load("recognizer\\training_Data.yml")
id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 1, 1, 0, 2)

def getProfile(id):
    conn = sqlite3.connect("FaceDB.db")
    cmd = "SELECT * FROM Person WHERE IDs = '" + str(id) + "'"
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile
    
while (cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        profile = getProfile(id)
        if profile is not None:
            cv2.cv.PutText(cv2.cv.fromarray(img), str(profile[1]), (x, y+h+30), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(img), str(profile[0]), (x, y+h+60), font, 255)
            
    cv2.imshow('My_Video', img)
    if cv2.waitKey(1) is ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

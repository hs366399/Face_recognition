import cv2
import sqlite3
import os,sys
import numpy as np

def insertData(Id, Name):
    conn = sqlite3.connect("FaceDB.db")
    cmd = "SELECT * FROM Person WHERE IDs = '" + str(Id) + "'"
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist is 1:
        cmd = "UPDATE Person SET Name = '" + str(Name) + "' WHERE IDs = '" + str(Id) + "'"
    else:
        cmd = "INSERT INTO Person(IDs, Name) VALUES('" + str(Id) + "', '" + str(Name) + "')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

def face_register():

    face_cascade = cv2.CascadeClassifier('Harcascade FIles\\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    
    user_id = raw_input("Enter your ID : ")
    name = raw_input("Enter your Name : ")
    insertData(user_id, str(name))
    
    sample_id = 0
    if not os.path.exists("Image_dataSet\\" + user_id):
        os.makedirs("Image_dataSet\\" + user_id)
    
        while (cap.isOpened()):
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.imwrite("Image_dataSet\\" + user_id + "\\" + user_id + "." + str(sample_id) + ".jpg", gray[y:y+h, x:x+w])
                sample_id+=1
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
            
            cv2.imshow('My_Video', img)
            cv2.waitKey(1)
            if sample_id is 200:
                cap.release()
                cv2.destroyAllWindows()
                act_path = str("Image_dataSet\\" + user_id)
    else:
        cap.release()
        cv2.destroyAllWindows()
        act_

face_register()

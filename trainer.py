import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
path = str(os.getcwd()) + "\\Image_dataSet"

def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for dir in os.listdir(path):
        for imagePath in os.listdir(path + "\\" + dir + "\\"):
            faceImg = Image.open(path + "\\" + dir + "\\" + imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            IDs.append(int(imagePath.split(".")[0]))
            faces.append(faceNp)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
    return IDs, faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save("recognizer\\training_Data.yml")
cv2.destroyAllWindows()


    


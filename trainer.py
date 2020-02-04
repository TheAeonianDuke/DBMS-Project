import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create() #Use OpenCv's Face Recognizer
path='dataSet' #Get images from dataset

def getImagesWithID(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    IDs=[]

    for imagepath in imagepaths:
        faceImg=Image.open(imagepath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Training From New User's Input...",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

IDs,faces=getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.save('recognizer_trainningData.yml')
cv2.destroyAllWindows()
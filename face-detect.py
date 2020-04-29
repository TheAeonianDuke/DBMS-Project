import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer_trainningData.yml")
font=cv2.FONT_HERSHEY_SIMPLEX

def connect_db():
	facedb=sqlite3.connect("dbms_db.db")
	c=facedb.cursor()
	return facedb


facedb=connect_db()



def getProfile(facedb,id):  
    cmd="SELECT * FROM users WHERE user_id="+str(id)
    cursor=facedb.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    # facedb.close()
    return profile

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(facedb,id)
        if(profile!=None):
            cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),font,0.5,(0,255,0));
            cv2.putText(img,"Age : "+str(profile[2]),(x,y+h+45),font,0.5,(0,255,0));
            cv2.putText(img,"Gender : "+str(profile[3]),(x,y+h+70),font,0.5,(0,255,0));
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
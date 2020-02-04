import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Use Default haar cascade from OpenCV
cam=cv2.VideoCapture(0) # Capture from first camera in system

# def insertOrUpdate(Id,Name,Age,Gen):
#     conn=sqlite3.connect("FaceBase.db")
#     cmd="SELECT * FROM People WHERE ID="+str(Id)
#     cursor=conn.execute(cmd)
#     isRecordExist=0
#     for row in cursor:
#         isRecordExist=1
#     if(isRecordExist==1):
#         cmd="UPDATE People SET Name="+str(Name)+"WHERE ID="+str(Id)
#         cmd2="UPDATE People SET Age="+str(Age)+"WHERE ID="+str(Id)
#         cmd3="UPDATE People SET Gender="+str(Gen)+"WHERE ID="+str(Id)
#     else:
#         cmd="INSERT INTO users_db(ID,Name,Age,Gender) Values("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gen)+","+")"
#         cmd2=""
#         cmd3=""
#         cmd4=""
#     conn.execute(cmd)
#     conn.execute(cmd2)
#     conn.execute(cmd3)
#     conn.execute(cmd4)
#     conn.commit()
#     conn.close()

Id=input('Enter User Id')
name=input('Enter User Name')
age=input('Enter User Age')
gen=input('Enter User Gender')


# insertOrUpdate(Id,name,age,gen)

sampleNum=0 #Number of sample images of face
while(True):
    ret,img=cam.read() #Read from cam
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image to gray
    faces=faceDetect.detectMultiScale(gray,1.3,5) #Detect objects of different sizes 

    # Save images and create boxes 
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);

    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()

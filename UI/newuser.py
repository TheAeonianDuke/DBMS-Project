# TODO : Add back navigation button // DONE!
#        Take user to login after registration 
#        Handle empty user inputs // DONE!
#        Handle empty button clicks
#        UI, normalization in doc, indexing in docs, ER diagram
#        Relational Algebra
#        



import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox

# import Opencv module
import cv2
import os
import numpy as np
from PIL import Image

from newuserui import *
import numpy as np
import sqlite3
import splashscreen
import login

class MainWindow(QWidget):
    # class constructor
    def __init__(self,oldwindow):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(oldwindow)
        self.thiswindow = oldwindow
        self.ui.control_bt.hide()
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.submit.clicked.connect(self.insertOrUpdate)
        self.ui.backbtn.clicked.connect(self.backBtn)
        self.scan=0

    def backBtn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = splashscreen.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.thiswindow.close()
        self.window.show()


    def loginBtn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login.MainWindowLogin(self.window)
        self.thiswindow.close()
        self.window.show()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = splashscreen.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.window.show()

    def viewCam(self):
        sampleNum=0
        
        while(self.scan<1):
            ret,img=self.cam.read() #Read from cam
            # print(img)
            ret = cv2.resize(ret, (860,640))
            img = cv2.resize(img, (860,640))
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image to gray
            height, width, channel = img.shape
            step = channel * width
            faces=self.faceDetect.detectMultiScale(gray,1.3,5) #Detect objects of different sizes 
            qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
            # Save images and create boxes 
            
            for(x,y,w,h) in faces:
                sampleNum=sampleNum+1;
                cv2.imwrite("dataSet/User."+str(self.idval)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.waitKey(100);
            # print(self.scan)
            self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
            # cv2.imshow("Face",img);
            cv2.waitKey(1);
            if(sampleNum>20):
                print("DONE! ID :", self.idval)
                self.scan+=1
                self.ui.control_bt.setText("T r a i n i n g   N o w . . .")
                IDs,faces=self.getImagesWithID()
                self.recognizer.train(faces,IDs)
                self.recognizer.save('recognizer_trainningData.yml')
                self.timer.stop()
                self.cam.release()
                self.ui.control_bt.setText("D o n e !  G o   t o   l o g i n")
                self.ui.control_bt.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(39, 235, 56);")
                self.ui.control_bt.clicked.connect(self.loginBtn)
                break
                


    def controlTimer(self):
        if not self.timer.isActive():
            
            self.faceDetect=cv2.CascadeClassifier('../haarcascade_frontalface_default.xml') #Use Default haar cascade from OpenCV
            self.cam=cv2.VideoCapture(0) # Capture from first camera in system
            self.timer.start(20)
            self.ui.control_bt.setText("D e t e c t i n g  F a c e . . .")
        
        # else:
        #     self.timer.stop()
        #     self.cam.release()
        #     self.ui.control_bt.setText("S t a r t  C a m e r a")



    def insertOrUpdate(self):
        Name = self.ui.nameinput.text()
        Age = self.ui.ageinput.text()
        Gen = self.ui.genderinput.text()
        Phone = self.ui.phoneinput.text()

        if(str(Name)!="" and str(Age)!="" and str(Gen)!="" and str(Phone)!="" and str(Age).isnumeric() and str(Phone).isnumeric() and (str(Gen).lower() == 'male' or str(Gen).lower()=='female')):

            params = (str(Name), str(Age), str(Gen), str(Phone))
            
            conn=sqlite3.connect("dbms_db.db")
            cmd2=""
            cmd3=""
            cmd4=""
            cursor = conn.execute("INSERT INTO users(user_id,first_name,age,gender,phone)  Values (NULL, ?, ?, ?, ?)", params)
            conn.execute(cmd2)
            conn.execute(cmd3)
            conn.execute(cmd4)
            conn.commit()
            conn.close()

            self.ui.control_bt.show()
            self.idval = (cursor.lastrowid)
            conn=sqlite3.connect("dbms_db.db")
            params2 = (str(self.idval), str("None"))
            cursor1 = conn.execute("INSERT INTO loyalty(user_id,category) Values(?,?)",params2)
            conn.commit()
            conn.close()
            self.timer = QTimer()
            self.timer.timeout.connect(self.viewCam)

        elif ((str(Gen).lower() != 'male' or str(Gen).lower() !='female') and str(Gen)!="" and str(Phone)!="" ):

            QMessageBox.about(self, "Error!", "Enter Either Male or Female!")
            print("Enter Either Male or Female!")


        else:

            QMessageBox.about(self, "Error!", "Please enter all fields or check field values!")
            print("Enter All Values!")



    def getImagesWithID(self):
        self.recognizer=cv2.face.LBPHFaceRecognizer_create() #Use OpenCv's Face Recognizer
        path='dataSet' #Get images from dataset
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
        cv2.destroyAllWindows()
        return np.array(IDs),faces
        


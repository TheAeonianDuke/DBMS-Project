# TODO : Add back navigation button
#        Take user to personal homepage after login
#        Handle empty button clicks
#        Handle face not detected case 
#        Fix "Waiting" text

import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2
import os
import numpy as np
from PIL import Image

from loginui import *
import numpy as np
import sqlite3
import splashscreen

class MainWindowLogin(QWidget):
    # class constructor
    def __init__(self,oldwindow):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(oldwindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        # self.ui.control_bt.hide()
        self.ui.control_bt.clicked.connect(self.controlTimer)
        # self.ui.submit.clicked.connect(self.insertOrUpdate)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = splashscreen.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def viewCam(self):
        sampleNum=0
        self.scan=0
        while(self.scan!=1):
            ret,img=self.cam.read() #Read from cam

            ret = cv2.resize(ret, (860,640))
            img = cv2.resize(img, (860,640))

            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image to gray
            height, width, channel = img.shape
            step = channel * width
            faces=self.faceDetect.detectMultiScale(gray,1.3,5) #Detect objects of different sizes 
            qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
            # Save images and create boxes 
            self.profiler=None
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf=self.rec.predict(gray[y:y+h,x:x+w])
                profile=self.getProfile(id)
                self.profiler = profile
                if(profile!=None):
                    cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),self.font,0.5,(0,255,0));
                    cv2.putText(img,"Age : "+str(profile[3]),(x,y+h+45),self.font,0.5,(0,255,0));
                    cv2.putText(img,"Gender : "+str(profile[4]),(x,y+h+70),self.font,0.5,(0,255,0));

            self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
            # cv2.imshow("Face",img);
            cv2.waitKey(1)
            self.ui.verify_btn.clicked.connect(self.verifyUser)
            # if(==ord('q')):
            #     self.timer.stop()
            #     self.cam.release()
            #     break;
            
            
                

    def verifyUser(self):
        self.ui.namelabel.setText(str(self.profiler[1]))
        self.ui.agelabel.setText(str(self.profiler[3]))
        self.ui.genderlabel.setText(str(self.profiler[4]))
        self.ui.phonelabel.setText(str(self.profiler[5]))
        self.timer.stop()
        self.cam.release()
        self.scan=1

    def controlTimer(self):
        if not self.timer.isActive():
            
            self.faceDetect=cv2.CascadeClassifier('../haarcascade_frontalface_default.xml') #Use Default haar cascade from OpenCV
            self.cam=cv2.VideoCapture(0);
            self.rec=cv2.face.LBPHFaceRecognizer_create()
            self.rec.read("recognizer_trainningData.yml")
            self.font=cv2.FONT_HERSHEY_SIMPLEX
            self.timer.start(20)
            self.ui.control_bt.setText("R e c o g n i z i n g  F a c e . . .")
        
        # else:
        #     self.timer.stop()
        #     self.cam.release()
        #     self.ui.control_bt.setText("S t a r t  C a m e r a")
        #     
        #     
    def getProfile(self,id):  
        facedb=sqlite3.connect("../dbms_db.db")
        c=facedb.cursor()
        cmd="SELECT * FROM users WHERE user_id="+str(id)
        cursor=facedb.execute(cmd)
        profile=None
        for row in cursor:
            profile=row
        # facedb.close()
        return profile

        

# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/12  22:07
import cv2
import numpy as np

#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

##################################
frameWidth = 640
frameHeight = 480
minArea = 500
color = (255,255,0)
count =0
nPlateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
##################################
# how to import a webcam
cap = cv2.VideoCapture(0)  # 0 mean webcam object
cap.set(3, 640)  # the width ID is 3
cap.set(4, 480)  # the height ID is 4
cap.set(10, 100)  # the brightness ID is 10
while True:
    success, img = cap.read()
    imgRoi = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = imgRoi[y:y+h,x:x+w]
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("saveNumberPlate"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,'Scan Saved',(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow('Result',img)
        cv2.waitKey(500)
        count +=1

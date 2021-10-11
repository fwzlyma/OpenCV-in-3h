# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/12  12:56
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

myColors = [[1,66,253,20,229,255],
            [24,82,170,34,255,255],
            [95,85,52,155,255,255]] #橙、黄、蓝
myColorValues = [[2,135,255], ## BGR
                 [2,242,253],
                 [245,66,57]]
myPoints = [] # [x, y, color]



def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #cv2.CHAIN_APPROX_NONE存储所有轮廓点
    x,y,width,height = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        # give a threshold so as to not detect any noise
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,width,height = cv2.boundingRect(approx) #矩形框
    return x+width//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow('Result',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





















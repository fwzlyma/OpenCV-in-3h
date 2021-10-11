# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/11  20:03
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) #添加RGB
#print(img.shape)

# 1. line
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3) #cv2.line(img, start_axis, end_axis, color, thickness)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 1)
#img[0:200, 100:200] = 255, 0, 0 # first means height, second means width
# cv2.imshow('Image', img)
# cv2.waitKey(0)

# 2. rectangle 矩形
cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED) #cv2.rectangle(img, start_point, end_point, color, thickness/cv2.FILLED)
# cv2.imshow('Image', img)
# cv2.waitKey(0)

# 3. circle 圆形
cv2.circle(img,(int(img.shape[1]/2),int(img.shape[0]/2)),30,(255,255,0),5) #cv2.circle(img, circle_centerpoint, radius[x,y], color, thickness/cv2.FILLED)
# cv2.imshow('Image', img)
# cv2.waitKey(0)

# 4. put text on img
cv2.putText(img,'OPENCV',(0,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3) #cv2.putText(img, string, point[x,y], cv2.FONT_**, scale--text img size ,color, thickness)
cv2.imshow('Image', img)
cv2.waitKey(0)















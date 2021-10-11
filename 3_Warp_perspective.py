# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/11  20:48
import cv2
import numpy as np

img = cv2.imread('cards.jpg')
print(img.shape) # shape -> (height, width)
width,height = 250,350
pts1 = np.float32([[110,219],[290,186],[152,484],[353,440]]) # here is the card's four points [x,y] ,依次 【左上，右上，左下，右下】
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2) # here means pts1 ->img transform into pst2 ->size of img 's matrix
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
print(imgOutput.shape)
cv2.imshow('Image',img)
cv2.imshow('Output',imgOutput)

cv2.waitKey(0)












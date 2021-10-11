# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/30  14:06
import cv2
import numpy as np

# img = cv2.imread("rwen.jpg")
img = cv2.imread("ruiwen.jpg")
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgBlur2 = cv2.GaussianBlur(imgBlur, (7, 7), 0)
imgBlur3 = cv2.GaussianBlur(imgBlur2, (7, 7), 0)

cv2.imwrite("rwfinal.jpg",imgBlur3)
# cv2.imwrite("ruiwen.jpg",img)
# cv2.imshow("view",img)
# cv2.imshow("view2",imgBlur3)
# cv2.waitKey(0)

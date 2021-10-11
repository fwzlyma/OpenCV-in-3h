# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/11  14:18
import cv2
import numpy as np
print('Package Imported')

#how to import a image
#img = cv2.imread("../task_summer/example.jpg") #imread means I am read.
#cv2.imshow("Output", img) #Now the image did appear but it went out immediately!
#cv2.waitKey(0) #1000 mean 1 second


# how to import a video
# cap = cv2.VideoCapture("test_video.mp4")
# while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#ctrl + /快速注释或删除


#how to import a webcam
# cap = cv2.VideoCapture(0) #0 mean webcam object
# cap.set(3, 640)  # the width ID is 3
# cap.set(4, 480)  # the height ID is 4
# cap.set(10, 100)  # the brightness ID is 10
# while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


# 1. 灰度图
img1 = cv2.imread('lambo.png')
img = cv2.resize(img1, (400, 400))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvtColor cvt means convert
#cv2.imshow('Gray Image', imgGray)
# cv2.waitKey(0)

# 2. blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
#cv2.imshow('Blur Image', imgBlur)
#cv2.waitKey(0)

# 3. canny edge detector
imgCanny = cv2.Canny(img, 100, 100)
#cv2.imshow('Canny Image',imgCanny)
#cv2.waitKey(0)

# 4. dilate 膨胀
kernel = np.ones((5, 5), np.uint8)  #统一类型 np.uint8
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#cv2.imshow('Dialation Image',imgDialation)
# cv2.waitKey(0)

# 4.2 erode 腐蚀
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) #iteration 迭代次数
#cv2.imshow('Eroded Image', imgEroded)
#cv2.waitKey(0)

# 5. resize and crop
img_benz = cv2.imread('lambo.png')
# print(img_benz.shape)
img_benz_resize = cv2.resize(img_benz, (600, 400))

img_benz_cropped = img_benz[0:300, 300:600] #height,width
# cv2.imshow('Image', img_benz)
# cv2.imshow('Image Resize', img_benz_resize)
cv2.imshow('Image Cropped', img_benz_cropped)
cv2.waitKey(0)

















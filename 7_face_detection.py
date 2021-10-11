# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/12  12:27
import cv2
import numpy as np


def useCam():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # how to import a webcam
    cap = cv2.VideoCapture(0)  # 0 mean webcam object
    cap.set(3, 640)  # the width ID is 3
    cap.set(4, 480)  # the height ID is 4
    cap.set(10, 100)  # the brightness ID is 10
    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def useImg():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('lena.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    useImg()

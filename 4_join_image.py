# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/7/11  21:39
import cv2
import numpy as np



# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
'''
issue 1: cannot resize the stack img
issue 2: stack the img may out of the frame
issue 3: the type of img must be the same , RGB with Gray img cannot stack
'''
# cv2.imshow('Horizontal',imgHor)
# cv2.imshow('Vertical',imgVer)
#
# cv2.waitKey(0)

'''
solution of the issues, here is the function of it.
Don't need to know how it works, 
but to learn how to use it.
'''


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver



# imgStack2 = stackImages(0.5, ([img, img, img], [img, img, img]))
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgStack3 = stackImages(0.5, ([img, imgGray, img]))

# cv2.imshow('Stack 2 of Image', imgStack2)
# cv2.imshow('Stack different RGB of Image', imgStack3)


if __name__ == '__main__':
    img1 = cv2.imread(r'D:\dailyFiles\picProcess\e4front_1.png')
    img2 = cv2.imread(r'D:\dailyFiles\picProcess\e4front_2.png')
    # img1 = cv2.imread(r'D:\dailyFiles\picProcess\img1.png')
    # img2 = cv2.imread(r'D:\dailyFiles\picProcess\img2.png')
    # img3 = cv2.imread(r'D:\dailyFiles\picProcess\img3.png')
    # img4 = cv2.imread(r'D:\dailyFiles\picProcess\img4.png')
    # img5 = cv2.imread(r'D:\dailyFiles\picProcess\img5.png')
    # img6 = cv2.imread(r'D:\dailyFiles\picProcess\img6.png')


    # imgStack = stackImages(0.5, ([img4], [img5], [img6]))
    imgStack = stackImages(0.5, ([img1,img2]))
    cv2.imwrite(r"D:\dailyFiles\picProcess\e4front.png", imgStack)
    cv2.imshow('Stack of Image', imgStack)
    cv2.waitKey(0)
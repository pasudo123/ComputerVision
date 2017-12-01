import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

"""
- 블러링 ##
영상의 자세한 부분을 제거하거나 줄인다.
카메라의 초점을 흐리게 하거나 배경을 약화
마스크의 크기가 클수록 효과는 좋아짐.
영상 내에 존재하는 잡음을 줄이는데 효과적

- 샤프닝 ##
블러링의 반대 개념
영상의 자세한 부분을 강조
영상의 부분적인 대비를 증가시킴
영상의 경계 부분에 대한 대비 효과 증가
"""
def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # high-pass filter
    kernel = np.array([[-1, -1, -1],\
                       [-1,  9, -1],\
                       [-1, -1, -1]])

    result = cv2.filter2D(img, -1, kernel)
    result1 = cv2.blur(img, (3, 3))
    result2 = cv2.blur(img, (10, 10))
    result3 = cv2.GaussianBlur(img, (3, 3), 0)

    cv2.imshow('image', img)
    cv2.imshow('result filter2D', result)
    # cv2.imshow('result blur(3,3)', result1)
    # cv2.imshow('result blur(10, 10)', result2)
    # cv2.imshow('result GaussianBlur(3, 3)', result3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
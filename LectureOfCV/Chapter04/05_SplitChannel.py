import cv2
import os
from pprint import pprint
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    # # 채널 분리.
    b, g, r = cv2.split(img)

    # numpy 이용 채널 분리.
    # b = img[:, :, 0]
    # g = img[:, :, 1]
    # r = img[:, :, 2];

    ################
    # pprint(b)
    # print("----")
    # pprint(g)
    # print("----")
    # pprint(r)
    # print("----")
    ################

    # numpy 이용 채널 분리.
    # b = img[:, :, 0]
    # g = img[:, :, 1]
    # r = img[:, :, 2];

    # 채널 합성
    mergeImg = cv2.merge((b, g, r))

    # 분리된 채널로 이미지 띄우기
    cv2.imshow('B Image', b)
    cv2.imshow('G Image', g)
    cv2.imshow('R Image', r)
    cv2.imshow('Merge Image', mergeImg)

    # pprint(mergeImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
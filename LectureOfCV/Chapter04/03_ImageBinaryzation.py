import cv2
import os
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)    # 영상 그레이화
    
    # 이지화 이전
    cv2.imshow('Lena Image', img)
    
    # 영상 이치화 과정
    ysize = img.shape[0]    # 영상의 행 (높이)
    xsize = img.shape[1]    # 영상이 열 (가로)

    # threshold 를 주어 해당 값보다 작으면 0, 크면 255 이다. (흑 백)
    for y in range(ysize):
        for x in range(xsize):
            if img.item(y, x) < 128:
                img.itemset((y, x), 0)
            else:
                img.itemset((y, x), 255)
    
    # 이치화 이후
    cv2.imshow('Binary Image', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
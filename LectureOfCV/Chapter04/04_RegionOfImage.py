import cv2
import os
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    # 해당 img 를 높이 : 250 ~ 400, 너비 : 200 ~ 350 사이
    subimg = img[250:400, 200:350]
    cv2.imshow('SubImage', subimg)

    # img 의 해당 위치에 subimg 삽입
    img[0:150, 0:150] = subimg
    cv2.imshow('Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
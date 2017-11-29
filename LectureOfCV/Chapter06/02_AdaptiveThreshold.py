import cv2
import os
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

"""
적응이치화

하나의 임계치만으로 이치화를 하기때문에,
조명 등에 의한 점진적인 밝기의 변화에 만족할만한 결과를 얻기 힘듦
"""
def showImage():
    filename = askopenfilename() # filename = "VIN0.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    ret, result = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    result1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
    result2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

    cv2.imshow('image', img)
    cv2.imshow('OTSU', result)
    cv2.imshow('MEAN_C', result1)
    cv2.imshow('GAUSSIAN_C', result2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
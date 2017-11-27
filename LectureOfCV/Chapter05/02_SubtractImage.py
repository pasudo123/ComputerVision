import cv2
import os
from pprint import pprint
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    file1 = os.path.join(os.getcwd(), "ic_ref.raw.jpg")
    file2 = os.path.join(os.getcwd(), "ic_test.raw.jpg")

    img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Image_1', img1)

    img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Image_2', img2)

    # 뺄셈연산 적용 > 결함 발견
    result = cv2.subtract(img1, img2)
    cv2.imshow('Subtract result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
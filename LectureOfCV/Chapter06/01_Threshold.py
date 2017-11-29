import cv2
import os
import matplotlib.pyplot as plt

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

"""
자동이치화 (Otsu Algorithm)
임계치를 '자동' 으로 결정하는 알고리즘

높은 유사성을 갖는 픽셀들을 낮은 분산 값을 가진다는 점을 이용
즉, 배경부와 물체부의 두 그룹이 가능한 낮은 분산값을 가지도록 임계치 t 를 결정
"""
def showImage():
    filename = os.path.join(os.getcwd(), "CH06", "coin.raw.jpg")
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # cv2.threshold(img, th, maxValue, flag)
    # img : Grayscale 이미지
    # th  : 임계값
    # maxValue : 임계값보다 클 때 적용되는 값
    # flag

    ret, result1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)              # 0 < th < maxValue
    ret, result2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)          # maxValue < th < 0
    ret, result3 = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)               # value < th < th
    ret, result4 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)              # 0 < th < value
    ret, result5 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)          # value < th < 0
    ret, result6 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)    # Otsu

    cv2.imshow('BINARY', result1)
    cv2.imshow('BINARY_INV', result2)
    cv2.imshow('TRUNC', result3)
    cv2.imshow('TOZERO', result4)
    cv2.imshow('TOZERO_INV', result5)
    cv2.imshow('OTSU', result6)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
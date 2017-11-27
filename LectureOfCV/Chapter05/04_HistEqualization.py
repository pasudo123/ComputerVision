import cv2
import os
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)


def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 영상 그레이화
    
    # 일반 이미지.
    cv2.imshow('Lena Image', img)

    equImg = cv2.equalizeHist(img)

    # 픽셀들이 여러 밝기 영역으로 넓게 퍼지며 분포하게 된다.
    # 누적 히스토그램으로붵 정규화 합 히스토그램을 구함

    # 평활화 이후
    cv2.imshow("Lena Eualization Image", equImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
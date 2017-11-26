import cv2
import numpy as np
import os

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")

    # img = cv2.imread(filename, cv2.IMREAD_COLOR)      # 컬러이미지
    # img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 흑백이미지
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)    # 알파채널 포함 그대로 읽음
    
    cv2.imshow('Lena Image', img) # 해당 윈도우 폼 타이틀
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # cv2 버전 확인 & 현재 작업 디렉토리 반환
    print("openCV Version : ", cv2.__version__)
    print("변환 전 경로 : ", os.getcwd())

    imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
    os.chdir(imagepath)
    
    print("변환 후 경로 : ", os.getcwd())
    showImage()
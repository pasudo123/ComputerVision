import cv2
import os
import numpy as np

"""
    - imshow()
    이미지를 읽은 후, numpy 의 ndarray 형식으로 리턴.
    해당 픽셀의 값 [B, G, R] (= BLUE, GREEN, RED)

    img.shape : 이미지의 높이, 너비, 채널수 
    img.size  : 이미지의 크기(바이트)
    img.dtype : 이미지 픽셀의 데이터 타입
    """

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    print("Image shape : ", img.shape)
    print("Image size  : ", img.size)
    print("Image dtype : ", img.dtype)

    cv2.namedWindow('Lena Image', cv2.WINDOW_NORMAL)  # 크기 조정 가능
    # cv2.namedWindow('Lena Image', cv2.WINDOW_AUTOSIZE)  # 크기 조정 불가

    cv2.imshow('Lena Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
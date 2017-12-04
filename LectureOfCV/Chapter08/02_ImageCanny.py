import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    """
    Canny Edge Detector : 가장자리 검출 알고리즘
    이미지를 그레이 이미지 변환 후 가장자리 검출 알고리즘을 이용하여, 
    이미지를 이진화 하는 방법에 대해 정리
    
    (1) 낮은 에러율 : 실제 에지만을 탐지하는 능력 ( 에지를 못찾는 경우 최소화 ) 
    (2) 낮은 오차율 : 실제 에지와 탐지된 에지의 픽셀 거리 차이를 최소화 ( 실제 에지와 가까워야 함 )
    (3) 최소한의 응답성 : 각 에지에 대해서는 한 번만 검출
    """    
    result = cv2.Canny(img, 50, 150)

    print(cv2.CV_64F)

    cv2.imshow('Image', img)
    cv2.imshow('Canny', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
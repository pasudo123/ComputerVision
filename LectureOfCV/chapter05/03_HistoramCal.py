import cv2
import os
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

"""
- 수평축 : 영상의 밝기 값
- 수직축 : 수평축의 밝기 값에 대응되는 크기를 가진 픽셀의 빈도 수
"""
def showHistogram():
    filename = os.path.join(os.getcwd(), "lena.jpg")

    grayImg = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # 히스토그램 계산
    hist = cv2.calcHist([grayImg], [0], None, [256], [0, 256])

    # 히스토그램 그리기
    plt.plot(hist, color='black')

    colorImg = cv2.imread(filename, cv2.IMREAD_COLOR)

    for i, c in enumerate(('blue', 'green', 'red')):
        # 히스토그램 계산
        # (Image, Channel, Mask, Histsize, Range)
        hist = cv2.calcHist([colorImg], [i], None, [256], [0, 256])
        plt.plot(hist, color=c)

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showHistogram()
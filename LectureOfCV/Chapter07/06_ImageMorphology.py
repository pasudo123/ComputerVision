import cv2
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from tkinter.filedialog import askopenfilename


# 모폴로지 처리 : 영상의 밝은영역 혹은 어두운영역을 축소, 확대하는 기법

# 처리대상이 좁아지는 침식연산이 존재
# 처리대상이 넓어지는 팽창연산이 존재

"""
- 침식연산
영상 내에서 구조요소의 모든 요소가 영역 내에 존재하면 현재의 그 지점의 값을 1로 설정

- 팽창연산
영상 내에서 구조요소의 값 중 하나라도 영역 내에 존재하면 현재 그 지점의 값을 1로 설정
"""

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    kernel = np.ones((3, 3), np.uint8)

    """
    kernel = array([[1, 1, 1]\
                    [1, 1, 1]\
                    [1, 1, 1]], dtype=uint8)
    """
    result1 = cv2.erode(img, kernel, iterations=1)
    result2 = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('Image', img)
    cv2.imshow('erosionImage', result1)
    cv2.imshow('dilateImage', result2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
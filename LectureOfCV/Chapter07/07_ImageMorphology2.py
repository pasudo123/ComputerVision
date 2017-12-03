import cv2
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from tkinter.filedialog import askopenfilename

# 대상 영역에서 세부영역이 '제거되는' 열림연산 존재
# 대상 영역에서 세부영역이 '채워지는' 닫힘연산 존재

"""
열림연산과 닫힘연산은 침식과 팽창을 결합한 형태이다.

- 열림연산은 밝은영역에 나타난 미세한 조각을 제거할 수 있다.
침식 연산 수행(erode) >> 밝은 영역 전체 축소 >> 팽창 연산 수행 >> 전체적인 넓이로 복구

- 닫힘연산은 밝은영역에 생긴 미세한 틈을 메운다
팽창 연산 수행(dilate) >> 밝은 영역을 넓힘 >> 침식 연산 수행 >> 전체적인 넓이로 복구

reference : https://docs.opencv.org/2.4/doc/tutorials/imgproc/opening_closing_hats/opening_closing_hats.html
"""

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    kernel = np.ones((3, 3), np.uint8)

    result1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    result2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # 해당 개체의 윤곽선을 찾는데, 유용 : 팽창과 부식의 차로 구한다.
    # dst = morph_{grad}( src, element ) = dilate( src, element ) - erode( src, element )
    result3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow('Image', img)
    cv2.imshow('openingImage', result1)
    cv2.imshow('closingImage', result2)
    cv2.imshow('gradientImage', result3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
import cv2
import os
from pprint import pprint
import numpy as np

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)

def showImage():
    filename = os.path.join(os.getcwd(), "lena.jpg")
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    # numpy.arange([start, ] stop, [step, ] dtype=None)
    # uint : Unsigned integer (0 to 255)
    # 255 ~ -1 (-1 미포함), step 은 -1 로 감소 내림차순
    lut = np.arange(255, -1, -1, dtype='uint8') # Create Lookup Table
    
    # 결과값을 가진 테이블, 연산속도 감소
    result = cv2.LUT(img, lut)

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
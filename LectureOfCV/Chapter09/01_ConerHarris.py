import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    """
    cv2.cornerHarris(src, blockSize, ksize, k)
    src : input image(float32)
    blocksize : 이웃픽셀의 범위
    ksize : Sobel 인수 값
    k : 보통 0.04
    """
    result = cv2.cornerHarris(gray, 2, 3, 0.04)
    result = cv2.dilate(result, None)

    img[result > 0.01 * result.max()] = [0, 0, 255]

    cv2.imshow('Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
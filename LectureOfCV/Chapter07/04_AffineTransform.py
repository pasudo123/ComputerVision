import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def geometricTransform():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    pts1 = np.float32([[50, 50], [50, 100], [100, 75]])
    pts2 = np.float32([[10, 100], [10, 150], [100, 100]])

    # M = cv2.getAffineTransform(pts1, pts2)
    # 변환 전 3개의 죄표(pts1), 변환 후 3개의 좌표(pts2)
    M = cv2.getAffineTransform(pts1, pts2)
    result = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('image', img)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    geometricTransform()
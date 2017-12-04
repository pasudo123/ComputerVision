import cv2
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from tkinter.filedialog import askopenfilename

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    kernel = np.ones((3, 3), np.uint8)

    k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    k2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    k3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    print("MORPH_RECT\n", k1)
    print()
    print("MORPH_ELLIPSE\n", k2)
    print()
    print("MORPH_CROSS\n", k3)

    result2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k2)

    cv2.imshow('Image', result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def geometricTransform():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    M = cv2.getRotationMatrix2D((width/2, height/2), -45, 1)
    result = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('image', img)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    geometricTransform()
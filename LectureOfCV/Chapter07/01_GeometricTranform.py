import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def geometricTransform():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    rimg1 = cv2.resize(img, None, None, fx=0.5, fy=1.0, interpolation=cv2.INTER_AREA)
    rimg2 = cv2.resize(img, None, None, fx=1.0, fy=0.5, interpolation=cv2.INTER_AREA)
    rimg3 = cv2.resize(img, None, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('image', img)
    cv2.imshow('fx=0.5, fy=1.0', rimg1)
    cv2.imshow('fx=1.0, fy=0.5', rimg2)
    cv2.imshow('fx=0.5, fy=0.5', rimg3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    geometricTransform()
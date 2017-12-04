import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 50, 150)
    cv2.imshow('canny', canny)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 5, param1=100, param2=50, maxRadius=100)

    if circles is not None:
        print(circles)
        circles = np.uint16(np.around(circles[0, :]))

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 0, 255), 1)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
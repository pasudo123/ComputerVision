import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result1, result2 = None, None

    sift = cv2
    keypoint = sift.detect(gray, None)

    result1 = cv2.drawKeypoints(gray, keypoint, result1)
    result2 = cv2.drawKeypoints(gray, keypoint, result2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('SIFT1', result1)
    cv2.imshow("SIFT2", result2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showImage()
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def showImage():
    filename1 = askopenfilename()
    img1 = cv2.imread(filename1, cv2.IMREAD_COLOR)
    filename2 = askopenfilename()
    img2 = cv2.imread(filename2, cv2.IMREAD_COLOR)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x:x.distance)

    result = None
    result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], result, flags = 0)

    cv2.imshow("labeled Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

"""
M = [[1, 0, t_x],\
     [0, 1, t_y]]
    
    t_x, t_y 만큼이동
"""

def geometricTransform():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape[0:2]

    M = np.array([[1, 0, 100],\
                  [0, 1,  50]], np.float32)

    result = cv2.warpAffine(img, M, (width, height))

    cv2.imshow('image', img)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    geometricTransform()
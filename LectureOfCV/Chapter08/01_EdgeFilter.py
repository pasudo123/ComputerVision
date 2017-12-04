import cv2
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    result1 = cv2.Laplacian(img, cv2.CV_64F)
    result2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.subplot(2, 2, 2), plt.imshow(result1, cmap='gray')
    plt.subplot(2, 2, 3), plt.imshow(result2, cmap='gray')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showImage()
import cv2
import os
import matplotlib.pyplot as plt

imagepath = "C:\\Users\\PASUDO\\PycharmProjects\\Main\\ComputerVision\\Image"
os.chdir(imagepath)


def showHistogram():
    filename = os.path.join(os.getcwd(), "lena.jpg")

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 2D 히스토그램 계산
    # 물체의 모양은 무시한 채, 단순히 컬러 분포만을 검출하는 방법 
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    
    # OpenCV 출력
    cv2.imshow('2DHist', hist)

    # MatplotLib 출력
    plt.imshow(hist, interpolation='nearest')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showHistogram()
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hello/lena.jpg', cv2.IMREAD_GRAYSCALE)       # or 0
#img = cv2.imread('hello/sudoku.jpg', 0)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cannyedges = cv2.Canny(img, 100, 200)
images = [img, lap, sobelX, sobelY, sobelCombined, cannyedges]
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
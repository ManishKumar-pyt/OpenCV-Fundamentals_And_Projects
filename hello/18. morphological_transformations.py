import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hello/j.png')
# mask = cv2.threshold(video, 200, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2), np.uint8)

dilation = cv2.dilate(img, kernal, iterations=2)
erosion = cv2.erode(img, kernal, iterations=2)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)
bh = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernal)

images = [img, dilation, erosion, opening, closing, mg, th, bh]
titles = ['image', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hello/gradient1.jpg')

ret, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)
ret, th4 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO_INV)
ret, th5 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)

titles = ['Original image', 'BINARY','BINARY_INV', 'TOZERO', 'TOZERO_INV', 'TRUNC']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

#cv2.imshow('image', img)
#cv2.imshow('th1', th1)
#cv2.imshow('th2', th2)
#cv2.imshow('th3', th3)
#cv2.imshow('th4', th4)
#cv2.imshow('th5', th5)

plt.show()
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
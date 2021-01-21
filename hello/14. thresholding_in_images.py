import cv2
import numpy as np

img = cv2.imread('hello/gradient1.jpg')

ret, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)
ret, th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
ret, th5 = cv2.threshold(img, 250, 255, cv2.THRESH_MASK)

cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
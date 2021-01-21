import cv2
import numpy as np

img = cv2.imread('hello/Resources/chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)    # harris corner method takes float32 type
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = (0, 255, 255)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
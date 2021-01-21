import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hello/lena.jpg')

layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[4]
#cv2.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]

for i in range(4, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])  # acchi quality image - smooth, blurred image
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img= np.zeros((250, 500, 3), np.uint8)
cv.namedWindow('Image')

cv.createTrackbar('B', 'Image', 0, 255, nothing)
cv.createTrackbar('G', 'Image', 0, 255, nothing)
cv.createTrackbar('R', 'Image', 0, 255, nothing)
switch= '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'Image', 0, 1, nothing)

while(1):
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    b= cv.getTrackbarPos('B', 'Image')
    g= cv.getTrackbarPos('G', 'Image')
    r= cv.getTrackbarPos('R', 'Image')
    s= cv.getTrackbarPos(switch, 'Image')

    if s==0:
        img[:]=0
    else:
        img[:]= [b, g, r]

cv.destroyAllWindows()
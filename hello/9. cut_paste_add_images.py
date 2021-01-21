import cv2
import numpy as np

img= cv2.imread('hello/messi.jpg')
img2= cv2.imread('hello/opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)

#b,g,r= cv2.split(img)
#img= cv2.merge((b,g,r))

ball= img[339:395, 346:403]
img[342:398, 410:467]= ball
img[345:401, 473:530]= ball

img= cv2.resize(img, (510,510))
img2= cv2.resize(img2, (510,510))

dst= cv2.addWeighted(img, .7, img2, .3, 0)

cv2.imshow('image', dst)
if cv2.waitKey(0) and 0xFF == ord('q'):
    cv2.destroyAllWindows()
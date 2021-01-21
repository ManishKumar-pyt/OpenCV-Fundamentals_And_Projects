import cv2
import numpy as np

img = cv2.imread('hello/Resources/messi5.jpg',)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('hello/Resources/template.jpg', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

# when there are more than one templates in image we can proceed like this: (can do even for one template in img)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
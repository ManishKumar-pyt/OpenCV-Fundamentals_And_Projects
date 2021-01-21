import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hello/Resources/lena.jpg')
# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv2.rectangle(img, (0, 100), (100, 200), (127), -1)

# b, g, r = cv2.split(img)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

# cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
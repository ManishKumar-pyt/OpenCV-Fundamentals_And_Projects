import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('hello/opencv-logo.png')
#img = cv2.imread('hello/medianblur.jpg')
#img = cv2.imread('hello/filterimage.jpg')
img = cv2.imread('hello/lena.jpg')                    #sharp corners in bilateralfilter

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
mblur = cv2.medianBlur(img, 7)
bfilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D convolution', 'blur', 'Gaussian Blur', 'MedianBlur', 'bilateralfilter']
images = [img, dst, blur, gblur, mblur, bfilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
if cv2.waitkey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
def nothing(x):
    print(x)

cv2.namedWindow('trackers')
cv2.createTrackbar('LH', 'trackers', 0, 255, nothing)
cv2.createTrackbar('LS', 'trackers', 0, 255, nothing)
cv2.createTrackbar('LV', 'trackers', 0, 255, nothing)
cv2.createTrackbar('UH', 'trackers', 0, 255, nothing)
cv2.createTrackbar('US', 'trackers', 0, 255, nothing)
cv2.createTrackbar('UV', 'trackers', 0, 255, nothing)

while(1):
    img = cv2.imread('hello/Smarties.jpg')
   # ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'trackers')
    l_s = cv2.getTrackbarPos('LS', 'trackers')
    l_v = cv2.getTrackbarPos('LV', 'trackers')
    u_h = cv2.getTrackbarPos('UH', 'trackers')
    u_s = cv2.getTrackbarPos('US', 'trackers')
    u_v = cv2.getTrackbarPos('UV', 'trackers')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(img, l_b, u_b)

    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
cv2.destroyAllWindows()

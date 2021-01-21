import cv2

img = cv2.imread('hello/fruits.jpg', 0)

print(img)

cv2.imshow("Output", img)
k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('hello/fruits_copy.png', img)
    cv2.destroyAllWindows()
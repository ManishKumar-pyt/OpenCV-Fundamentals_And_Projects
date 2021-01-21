import cv2 as cv

def nothing(x):
    print(x)

#img = cv.imread('hello/messi.jpg', 0)

cv.namedWindow('image')

cv.createTrackbar('th1', 'image', 100, 255, nothing)
cv.createTrackbar('th2', 'image', 100, 255, nothing)

while(1):
    img = cv.imread('hello/lena.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    t1 = cv.getTrackbarPos('th1', 'image')
    t2 = cv.getTrackbarPos('th2', 'image')

    img = cv.Canny(img, t1, t2)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    cv.imshow('image', img)

cv.destroyAllWindows()
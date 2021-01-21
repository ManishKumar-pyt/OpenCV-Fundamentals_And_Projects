import cv2

cap= cv2.VideoCapture(0)
print(cap.get(3), cap.get(4))

cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(3), cap.get(4))

while(cap.isOpened()):
    ret, video=cap.read()
    if ret==True:

        gray= cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
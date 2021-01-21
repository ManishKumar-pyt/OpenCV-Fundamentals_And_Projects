import cv2
import datetime

cap= cv2.VideoCapture(0)
print(cap.get(3), cap.get(4))

while(cap.isOpened()):
    ret, video=cap.read()
    if ret==True:
        font= cv2.FONT_HERSHEY_SIMPLEX
        text= "WIDTH:"+str(cap.get(3))+" HEIGHT:"+str(cap.get(4))

        datet= str(datetime.datetime.now())

        video= cv2.putText(video, text, (0,55), font, 1, (0,255,255), 2, cv2.LINE_AA)

        video= cv2.putText(video, datet, (240, 445), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Video", video)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
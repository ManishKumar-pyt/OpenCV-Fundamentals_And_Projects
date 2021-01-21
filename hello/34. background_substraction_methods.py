import cv2
import numpy as np

cap = cv2.VideoCapture('hello/Resources/vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG()   # by default detectshadows is true, change if needed
                                            # more methods are available for this check video
while cap.isOpened():
    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('FG MASK', fgmask)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
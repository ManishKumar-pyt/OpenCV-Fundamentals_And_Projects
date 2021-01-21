import cv2
import numpy as np

def mouse_event(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,255,255), -1)
        cv2.imshow('image', img)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 3)
            cv2.imshow('image', img)

points=[]
img= np.zeros((510,510,3),np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_event)

if cv2.waitKey(0) and 0xFF==ord('q'):
    cv2.destroyAllWindows()
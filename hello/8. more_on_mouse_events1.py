import cv2
import numpy as np

def mouse_click(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]

        mycolor= np.zeros((510,510,3),np.uint8)
        mycolor[:]=[blue,green, red]
        font= cv2.FONT_HERSHEY_SIMPLEX
        strBGR= str(blue)+', '+str(green)+', '+str(red)
        mycolor= cv2.putText(mycolor, strBGR, (10,255), font, 2, (0,0,0), 2)
        cv2.imshow('mycolor',mycolor)

img= cv2.imread('hello/fruits.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
if cv2.waitKey(0) and 0xFF==ord('a'):
    cv2.destroyAllWindows()
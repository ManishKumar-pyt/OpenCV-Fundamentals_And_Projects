import numpy as np
import cv2

#img = cv2.imread('hello/lena.jpg', 1)
img= np.zeros([600,600,3], np.uint8)

img= cv2.rectangle(img, (0,0), (510,510), (0,0,255), -1)
img= cv2.line(img, (0,0), (510,255), (0,255,255), 10,)
img= cv2.arrowedLine(img, (0,0), (255,510), (255,255,0), 2)
img= cv2.rectangle(img, (255,255), (510,510), (0,255,0), 5)
img= cv2.circle(img, (255,255), 150, (150,0,255), 10)

font= cv2.FONT_HERSHEY_SCRIPT_COMPLEX
img= cv2.putText(img, "Sample", (150,255), font, 3, (255,0,0), 5, cv2.LINE_8)
#img= cv2.ellipse(img, (300,300), )

cv2.imshow('image', img)
if cv2.waitKey(0) and 0xFF == ord('q'):
    cv2.destroyAllWindows()
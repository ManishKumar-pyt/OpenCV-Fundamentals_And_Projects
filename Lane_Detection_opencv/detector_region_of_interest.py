import cv2
import numpy as np
from matplotlib import pylab as plt

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    mask_show = cv2.cvtColor(mask, cv2.COLOR_RGB2BGR)
    #cv2.imshow('image', mask_show)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype= np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 6)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0)
    return img

image = cv2.imread('lanes.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [(0, 540), (570, 270), (1000, 704)]

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 300)

cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

lines = cv2.HoughLinesP(cropped_image, rho= 20, theta= np.pi/60, threshold= 300, lines= np.array([]), minLineLength = 25, maxLineGap = 200)

image_with_lines = draw_the_lines(image, lines)

plt.imshow(image_with_lines)
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
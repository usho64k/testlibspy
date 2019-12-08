import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('C:/Python27/images/sample1.png')
img2 = cv2.imread('C:/Python27/images/inomin.png')
print img
print img2

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print img_rgb

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print gray_img

cv2.imwrite('images/img.png',gray_img)
cv2.imwrite('images/gbr.png',img_rgb)

_,threshold_img = cv2.threshold(gray_img,80,255,cv2.THRESH_BINARY)
threshold_img = cv2.cvtColor(threshold_img,cv2.COLOR_GRAY2RGB)
cv2.imwrite('images/thresh.png',threshold_img)

piet = cv2.imread('C:/Python27/images/gbr.png')
piet_hsv = cv2.cvtColor(piet,cv2.COLOR_BGR2HSV)
blue_min = np.array([100,100,100],np.uint8)
blue_max = np.array([142,255,255],np.uint8)
thre_bl_img = cv2.inRange(piet_hsv,blue_min,blue_max)
thre_bl_img = cv2.cvtColor(thre_bl_img,cv2.COLOR_GRAY2RGB)
cv2.imwrite('images/thresh4.png',thre_bl_img)


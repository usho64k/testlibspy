import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import

shikichi = 138

#Reading Image
img = cv2.imread('images/curcle.png');

#GrayScale Translate
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cv2.imwrite('images/1.png',gray_img)
#Output Black/White
_,th = cv2.threshold(gray_img,shikichi,255,cv2.THRESH_BINARY);
cv2.imwrite('images/2.png',th)
#Search the separator
contours, hieraruchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);
#ArrayType Translate
contours = np.array(contours);

count = 0;
for i in contours:
	#draw circle each the parts
	countB = 0;
	cv2.circle(img,(contours[count][countB][0][0],contours[count][countB][0][1]),1,(255,0,0),-1);
	count +=1;

#Output Number of Circles and Picture
print "there are " +str(count)+" circles.";

cv2.imwrite("images/Circles.png",img);
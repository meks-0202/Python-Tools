import cv2 as cv
import numpy as np
from google.colab.patches import cv2_imshow # This is needed only for google colab

img = cv.imread('/content/cats.jpg')
#cv.imshow('Cats', img)# This is used for local computer 
cv2_imshow(img)#This is used only in google colab
cv.waitKey(0)

#Grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
cv2_imshow(gray)
cv.waitKey(0)

#Canny edges
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)
cv2_imshow(canny)
cv.waitKey(0)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
cv.waitKey(0)

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank)
cv2_imshow(blank)
cv.waitKey(0)

cv.drawContours(blank, contours, -1, (255,255,0), 1)
#cv.imshow('Contours Drawn', blank)
cv2_imshow(blank)
cv.waitKey(0)

#thresholding
 ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
 #cv.imshow('Thresh', thresh)
 cv2_imshow(thresh)
cv.waitKey(0)
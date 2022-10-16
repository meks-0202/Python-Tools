import cv2 as cv
from google.colab.patches import cv2_imshow # This is needed only for google colab

img = cv.imread('/content/cats.jpg')
#cv.imshow('Cats', img) # This is used for local computer 
cv2_imshow(img) #This is used only in google colab
cv.waitKey(0)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
cv2_imshow(gray)
cv.waitKey(0)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)
cv2_imshow(blur)
cv.waitKey(0)
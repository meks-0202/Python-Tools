import cv2 as cv
from google.colab.patches import cv2_imshow # This is needed only for google colab

img = cv.imread('/content/cats.jpg')
#cv.imshow('Cats', img) # This is used for local computer 
cv2_imshow(img) #This is used only in google colab
cv.waitKey(0)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)
cv2_imshow(canny)
cv.waitKey(0)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)
cv2_imshow(dilated)
cv.waitKey(0)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)
cv2_imshow(eroded)
cv.waitKey(0)
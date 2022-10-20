import cv2 as cv
from google.colab.patches import cv2_imshow # This is needed only for google colab

img = cv.imread('/content/cats.jpg')
#cv.imshow('Cats', img) # This is used for local computer 
cv2_imshow(img) #This is used only in google colab
cv.waitKey(0)


# Cropping
cropped = img[50:200, 200:400]
#cv.imshow('Cropped', cropped)
cv2_imshow(cropped)
cv.waitKey(0)
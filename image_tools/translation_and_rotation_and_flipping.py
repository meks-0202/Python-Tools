import cv2 as cv
import numpy as np
from google.colab.patches import cv2_imshow # This is needed only for google colab

img = cv.imread('/content/park.jpg')
#cv.imshow('Park', img) # This is used for local computer 
cv2_imshow(img) #This is used only in google colab
cv.waitKey(0)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
#cv.imshow('Translated', translated)
cv2_imshow(translated)
cv.waitKey(0)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
#cv.imshow('Rotated', rotated)
cv2_imshow(rotated)

# Rotation
rotated_rotated = rotate(img, -90)
#cv.imshow('Rotated Rotated', rotated_rotated)
cv2_imshow(rotated_rotated)
cv.waitKey(0)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)
cv2_imshow(resized)
cv.waitKey(0)

# Flipping
flip = cv.flip(img, -1)
#cv.imshow('Flip', flip)
cv2_imshow(flip)
cv.waitKey(0)


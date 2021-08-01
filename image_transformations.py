# importing the libraries
import cv2 as cv
import numpy as np

img = cv.imread('Photos/shin.png')
cv.imshow('shinchan', img)

print("shape of the image", img.shape)
#  the shape is (225, 225, 3)
#  image height : 225
# image width : 200
# number of channels 4

# Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.

# Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.

# Number of Channels represents the number of components used to represent each pixel.

# In the above example, Number of Channels = 4 represent Alpha, Red, Green and Blue channels.

# translation5
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down
    
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)
# --------------------------------------------------***-------------------------------------------------------------

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotate = rotate(img, 45)
cv.imshow('rotated', rotate)
# ---------------------------------------------------***--------------------------------------------------------------

# resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized_image', resized)

# flipping
# 0 -> flipping vertically
# 1 -> flipping horizontally
# -1 -> both vertically as well as horizontally
flip = cv.flip(img, 0)
cv.imshow('flipped images vertically', flip)

fliph = cv.flip(img, 1)
cv.imshow('flipped images vertically', fliph)

flipb = cv.flip(img, -1)
cv.imshow('flipped images vertically', flipb)

# cropped
# croped = img[50:50, 50:50]
# cv.imshow('cropped', croped)




















cv.waitKey(0)
# importing libraries 
import cv2 as cv

img = cv.imread('Photos/shin_1.png')
cv.imshow('shinchan', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray shinchan', gray)

#how to blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascading
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# dilate an image using structuring elements
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dialated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# resize and crop images
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropped
cropped = resized[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)

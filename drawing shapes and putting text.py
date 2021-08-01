# importing libraries
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# paint the image a color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('green', blank)
# cv.waitKey(0)

# # draw the rectangle
# rect = cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.imshow('rectangle', rect)

# # draw a circle
# cir = cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# cv.imshow('circle', cir)

# # draw a line 
# line = cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
# cv.imshow('line', line)

# writing text on an image 
cv.putText(blank, 'Hello, my name is Piyush', (10,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('text', blank)
# img = cv.imread('Photos/shin.png')
# cv.imshow('shinchan', img)

cv.waitKey(0)
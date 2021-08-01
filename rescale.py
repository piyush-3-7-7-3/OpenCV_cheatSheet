import cv2 as cv

def rescaleFrame(frame, scale=0.20):
    # images, videos, live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)
    
capture = cv.VideoCapture('Videos/shin_1.mp4')

img = cv.imread('Photos/shin_1.png')
resizedImg = rescaleFrame(img)
cv.imshow('shinchan', img)
cv.imshow('shinchanResized', resizedImg)

capture = cv.VideoCapture('Videos/shin_1.mp4')
while True:
    isTrue, frame = capture.read()
    if isTrue == True:
        frame_resized = rescaleFrame(frame)
        cv.imshow('video', frame)
        cv.imshow('video_resized', frame_resized)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
import cv2 as cv

img =  cv.imread('Photos/shin.png')
cv.imshow('shin', img)
cv.waitKey(0)

capture = cv.VideoCapture('Videos/shin_1.mp4')
while True:
    isTrue, frame = capture.read()
    if isTrue == True:
        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()


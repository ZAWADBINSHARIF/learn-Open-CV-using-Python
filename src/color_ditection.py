import cv2 as cv
import numpy as np
from stackImg import stackImages

path = "resources/lambo.png"
img = cv.imread(path)


def empty(a):
    pass


cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("HUE MIN", "TrackBars", 0, 179, empty)
cv.createTrackbar("HUE MAX", "TrackBars", 19, 179, empty)
cv.createTrackbar("SAT MIN", "TrackBars", 110, 255, empty)
cv.createTrackbar("SAT MAX", "TrackBars", 240, 255, empty)
cv.createTrackbar("VAL MIN", "TrackBars", 153, 255, empty)
cv.createTrackbar("VAL MAX", "TrackBars", 255, 255, empty)

imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

while True:
    hue_min = cv.getTrackbarPos("HUE MIN", "TrackBars")
    hue_max = cv.getTrackbarPos("HUE MAX", "TrackBars")
    sat_min = cv.getTrackbarPos("SAT MIN", "TrackBars")
    sat_max = cv.getTrackbarPos("SAT MAX", "TrackBars")
    val_min = cv.getTrackbarPos("VAL MIN", "TrackBars")
    val_max = cv.getTrackbarPos("VAL MAX", "TrackBars")

    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    lower = np.array([hue_min, sat_min, val_min])
    higher = np.array([hue_max, sat_max, val_max])
    mask = cv.inRange(imgHSV, lower, higher)
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # cv.imshow("Original", img)
    # cv.imshow("HSV", imgHSV)
    # cv.imshow("Mask", mask)
    # cv.imshow("Result", imgResult)

    stackImg = stackImages(0.7, [[img, imgHSV], [mask, imgResult]])
    cv.imshow("Stack Images", stackImg)

    cv.waitKey(1)

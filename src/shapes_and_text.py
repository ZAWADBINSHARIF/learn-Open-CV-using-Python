import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv.line(img, (0,0),(img.shape[0],img.shape[1]), (0,255,0), 5)
cv.rectangle(img, (0,0), (250,350), (0,0,255), 5)
cv.circle(img, (350,100), 50, (255,255,0), 5)
cv.putText(img, "OPEN CV", (300,200), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv.imshow("Image", img)

cv.waitKey(0)
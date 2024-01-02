import cv2 as cv
from stackImg import stackImages

path = "resources/lena.png"
img = cv.imread(path)
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, [[img, grayImg, img], [grayImg, img, grayImg]])

cv.imshow("Stack Image", imgStack)

cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread("resources/cards.jpg")

width, height = 250, 350

# A  _______________ B
#   |               |
#   |               |
#   |               |
#   |               |
# C |_______________| D

print("A  _______________ B")
print("  |               | ")
print("  |               | ")
print("  |               | ")
print("  |               | ")
print("C |_______________| D")

A, B, C, D = [527, 144], [771, 190], [404, 396], [676, 458]

pts1 = np.float32([A, B, C, D])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Image", img)
cv.imshow("Warp Perspective", imgOutput)

cv.waitKey(0)

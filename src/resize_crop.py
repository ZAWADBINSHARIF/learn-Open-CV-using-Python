import cv2

img = cv2.imread("resources/test.png")
print(img.shape)
resizeImg = cv2.resize(img, (300, 200))
imgCrop = img[0:200, 0:400]

cv2.imshow("Image", img)
cv2.imshow("Resize", resizeImg)
cv2.imshow("Crop", imgCrop)

cv2.waitKey(0)
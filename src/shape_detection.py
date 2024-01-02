import cv2 as cv
import numpy as np
from stackImg import stackImages

path = "resources/shapes.png"
img = cv.imread(path)
imgContour = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv.Canny(imgBlur, 50, 50)
blankImg = np.zeros_like(img)


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    i = 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area >= 55:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv.arcLength(cnt, True)
            epsilon = 0.02 * perimeter
            approx = cv.approxPolyDP(cnt, epsilon, True)
            objCor = len(approx)

            i += 1
            x, y, w, h = cv.boundingRect(approx)

            offset = 4
            objectType = "Unknown"
            print(i, objCor)
            # cv.circle(imgContour, (int(x+w/2), int(y+h/2)), int(h/2), (0, 255, 0), 2)
            cv.rectangle(imgContour, (x - offset, y - offset), (x + w + offset, y + h + offset), (0, 0, 255), 2)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if 0.98 < aspRatio < 1.03: objectType = "Square"
            else:
                objectType = "Cir"
            cv.putText(imgContour, f"{i} {objectType}", (x, int(y + h / 2)), cv.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)


getContours(imgCanny)

stackImg = stackImages(0.6, [
    [img, imgGray, imgBlur],
    [imgCanny, imgContour, blankImg]
])
cv.imshow("Stack Image", stackImg)
cv.imshow("Contours Image", imgContour)

cv.waitKey()

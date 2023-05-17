import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, '  ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + '   ' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)


img = cv2.imread('messi5.jpg')

print(img.shape)  # returns a tuple of rows, columns and channels
print(img.size)  # returns the Total number of pixels accessed
print(img.dtype)  # returns the obtained image datatype

points = []

# b, g, r = cv2.split(img)
# img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
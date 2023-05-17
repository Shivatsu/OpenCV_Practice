import cv2
import numpy as np


img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img1.shape)  # returns a tuple of rows, columns and channels
print(img1.size)  # returns the Total number of pixels accessed
print(img1.dtype)  # returns the obtained image datatype

points = []

# b, g, r = cv2.split(img1)
# img1 = cv2.merge((b, g, r))

ball = img1[280:340, 330:390]
img1[273:333, 100:160] = ball

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst1 = cv2.add(img1, img2)  # just for adding 2 images
dst = cv2.addWeighted(img1, .2, img2, .8, 0)  # for adding images with some weight t them
cv2.imshow('image1', dst1)
cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
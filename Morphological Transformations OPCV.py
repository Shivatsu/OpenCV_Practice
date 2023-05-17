import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', cv2.IMREAD_GRAYSCALE)
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=2)
erosion = cv2.erode(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
mgrad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
mtop = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

titles = ['img', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mgrad', 'mtop']
images = [img, img, dilation, erosion, opening, closing, mgrad, mtop]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

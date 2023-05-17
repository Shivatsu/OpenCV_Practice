import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Halftone,_Gaussian_Blur.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)


titles = ['image', '2D Convo', 'blur', 'gblur']
images = [img, dst, blur, gblur]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

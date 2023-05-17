import numpy as np
import cv2

# img = cv2.imread("lena.jpg", 1)
img = np.zeros([512, 512, 3], np.uint8)

p1 = [250, 120]
p2 = [170, 190]
p3 = [330, 190]
p4 = [330, 310]
p5 = [250, 380]
p6 = [170, 310]
pts = np.array([p1, p3,  # coordinates for a perfect polygon i think
                p4, p5,
                p6, p2],
               np.int32)

img = cv2.polylines(img, [pts], True, (0, 255, 255))

img = cv2.ellipse(img, (250, 250), (100, 50), 90, 0, 360, (255, 0, 255), 5, cv2.LINE_4)

img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 255, 0), 5)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)  # -1 -> will fill the shape with the color
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 470), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

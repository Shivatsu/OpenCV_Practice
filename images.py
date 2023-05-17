import cv2

img = cv2.imread("lena.jpg", 1)

cv2.imshow('Image', img)
k = cv2.waitKey(0)  # & 0xff - if it doesn't work in a 64 bit machine

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()

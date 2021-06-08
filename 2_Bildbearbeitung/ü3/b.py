import numpy as np
import cv2

'''Bild einlesen'''
img = cv2.imread("data/normal.jpg")
rows, cols, channels = img.shape

M1 = np.float32(
    [
        [np.cos(np.pi / 4), np.sin(np.pi / 4), 0],
        [-np.sin(np.pi / 4), np.cos(np.pi / 4), 0]
    ]
)
print(M1)

new_img = cv2.warpAffine(img, M1, (cols, rows))
cv2.imshow("1. Transformation", new_img)
cv2.waitKey(0)


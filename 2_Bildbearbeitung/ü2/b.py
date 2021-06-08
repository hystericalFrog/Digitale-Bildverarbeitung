import numpy as np
import cv2

'''Bild einlesen'''
I_in = cv2.imread("data/edge_01.png")
I_in = cv2.cvtColor(I_in, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", I_in)

'''1. Operation: Median-Filter'''
I_in = cv2.medianBlur(I_in, 9)
cv2.imshow("1. Operation: Median-Filter", I_in)

'''2. Operation: Kantenfilter'''
edge = [
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]
edge = np.asarray(edge)
I_in = cv2.filter2D(I_in, ddepth=cv2.CV_64F, kernel=edge, borderType=cv2.BORDER_REPLICATE)
cv2.imshow("2. Operation: Kanten-Filter vertikal", I_in)

'''3. Operation: Tiefpassfilter'''
edge = np.ones(shape=(3, 3)) / 9
edge = np.asarray(edge)
print(edge)
I_in = cv2.filter2D(I_in, ddepth=cv2.CV_64F, kernel=edge, borderType=cv2.BORDER_REPLICATE)
I_in = I_in / np.max(I_in)

cv2.imshow("3. Operation: Tiefpassfilter", I_in)


cv2.waitKey(0)

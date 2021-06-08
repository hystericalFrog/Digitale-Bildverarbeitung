import cv2
import numpy as np


I_in = [
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
    [100, 100, 100, 100, 100],
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
 ]
I_in = np.asarray(I_in, dtype="uint8")

print("Bild vor der Bearbeitung")
print(I_in)
print()


def hochpassfilter(img):
    hp_kernel = [
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]
    hp_kernel = np.asarray(hp_kernel)
    img = cv2.filter2D(src=img, ddepth=cv2.CV_64F, kernel=hp_kernel, borderType=cv2.BORDER_REPLICATE)
    print("Hochpassfilter")
    print(img)
    print()
    return img


def v_edge_filter(img):
    v_edge_kernel = [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]
    v_edge_kernel = np.asarray(v_edge_kernel)
    img = cv2.filter2D(src=img, ddepth=cv2.CV_64F, kernel=v_edge_kernel, borderType=cv2.BORDER_REPLICATE)
    print("Kantenfilter vertikal")
    print(img)
    print()
    return img


def h_edge_filter(img):
    h_edge_kernel = [
        [-1, -1, -1],
        [0,   0,  0],
        [1,   1,  1]
    ]
    h_edge_kernel = np.asarray(h_edge_kernel)
    img = cv2.filter2D(src=img, ddepth=cv2.CV_64F, kernel=h_edge_kernel, borderType=cv2.BORDER_REPLICATE)
    print("Kantenfilter horizontal")
    print(img)
    print()
    return img


def median_filter(img):
    img = cv2.medianBlur(img.astype("float32"), 3)
    print("Medianfilter")
    print(img)
    print()
    return img


def schwellwertbildung(img):
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    print("Schwellwertbildung")
    print(img)
    print()
    return img


def betragsbildung(img):
    img = np.abs(img)
    print("Betragsbildung")
    print(img)
    print()
    return img


print("Operation 1:")
I_in = h_edge_filter(I_in)
print("Operation 2:")
I_in = betragsbildung(I_in)
print("Operation 3:")
I_in = median_filter(I_in)
print("Operation 4:")
I_in = schwellwertbildung(I_in)

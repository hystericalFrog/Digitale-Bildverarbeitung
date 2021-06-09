import cv2
import numpy as np

from . import Algorithm


class Vorverarbeitung(Algorithm):
    """ The implementation of your algorithm """

    def __init__(self):
        """ Inititation of your algorithm. You can store member variables here! """
        self.prev_image = None
        self.curr_image = None

    def process(self, img):
        """ Here the input image (img) is processed and returned """
        '''Rauschreduktion'''
        if self.curr_image is None:
            self.curr_image = img
            return img
        self.prev_image = self.curr_image
        self.curr_image = img

        img = (self.curr_image.astype(np.uint16) + self.prev_image.astype(np.uint16)) / 2
        img = img.astype(np.uint8)

        '''Histogramm-Spreizung'''
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img = img.astype(np.float64)
        img[:, :, 2] = 255 * (img[:, :, 2] - np.min(img[:, :, 2])) / (np.max(img[:, :, 2]) - np.min(img[:, :, 2]))
        img = img.astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

        return img


    def mouse_callback(self, event, x, y, flags, param):
        """ The mouse callback react on mouse events """
        if event == cv2.EVENT_LBUTTONUP:
            print("self.img.dtype")



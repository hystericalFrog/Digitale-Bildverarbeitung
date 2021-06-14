import cv2
import numpy as np

from . import Algorithm


class Segmentierung(Algorithm):
    """ The implementation of your algorithm """

    def __init__(self):
        """ Inititation of your algorithm. You can store member variables here! """
        self.prev_image = None
        self.curr_image = None
        self.binary_mask = None
        self.background = None
        self.c = None
        self.count = 0
        self.img = None

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

        '''Statisches Schwellwertverfahren'''
        # hue
        channelh = 0
        lower_boundh, upper_boundh = 5, 15
        is_condition_h_true = (lower_boundh < img[:, :, channelh]) * (img[:, :, channelh] < upper_boundh)
        # sat
        channels = 1
        lower_bounds, upper_bounds = 100, 160
        is_condition_s_true = (lower_bounds < img[:, :, channels]) * (img[:, :, channels] < upper_bounds)

        self.binary_mask = is_condition_h_true * is_condition_s_true
        self.binary_mask = self.binary_mask.astype(np.uint8) * 255

        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        self.img = img

        '''Binärmaske'''
        kernel = np.ones(shape=(5, 5))
        self.binary_mask = cv2.erode(self.binary_mask, kernel)
        self.binary_mask = cv2.dilate(self.binary_mask, kernel)

        (cnts, _) = cv2.findContours(self.binary_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.ones_like(img)
        maskinv = np.zeros_like(img)
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea, default=0)
            mask = cv2.drawContours(mask, [c], -1, color=0, thickness=-1)
            maskinv = cv2.drawContours(maskinv, [c], -1, (1, 1, 1), thickness=-1)

        if self.background is not None:
            img = mask * img + self.background * maskinv

        self.img = img
        return img


    def mouse_callback(self, event, x, y, flags, param):
        """ The mouse callback react on mouse events """
        if event == cv2.EVENT_LBUTTONUP:
            if self.count == 0:
                self.background = self.img
                cv2.imwrite("background.png", self.background)
                self.count = 1
            elif self.count == 1:
                cv2.imwrite("mitMotiv.png", self.img)
                self.count = 2
            elif self.count == 2:
                cv2.imwrite("mitMotivUndUmhang.png", self.img)



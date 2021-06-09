import cv2
import numpy as np
from matplotlib import pyplot as plt

from . import Algorithm


class Farbanalyse(Algorithm):
    """ The implementation of your algorithm """

    def __init__(self):
        """ Inititation of your algorithm. You can store member variables here! """
        self.prev_image = None
        self.curr_image = None
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

        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        self.img = img
        '''RGB'''


        return img




    def mouse_callback(self, event, x, y, flags, param):
        """ The mouse callback react on mouse events """
        if event == cv2.EVENT_LBUTTONUP:
            pfad = "mitUmhang/" #"keinUmhang/"    #"mitUmhang/"
            cv2.imwrite(pfad+"bildBGR.png", self.img)

            hist_size = 256
            hist_range = [0, 256]
            histr_b = cv2.calcHist([self.img], [0], None, [hist_size], hist_range)
            plt.plot(histr_b, color="b")
            plt.xlim([0, 256])
            plt.savefig(pfad+"hist_b.png")
            plt.show()

            histr_g = cv2.calcHist([self.img], [1], None, [hist_size], hist_range)
            plt.plot(histr_g, color="g")
            plt.xlim([0, 256])
            plt.savefig(pfad+"hist_g.png")
            plt.show()

            histr_r = cv2.calcHist([self.img], [2], None, [hist_size], hist_range)
            plt.plot(histr_r, color="r")
            plt.xlim([0, 256])
            plt.savefig(pfad+"hist_r.png")
            plt.show()




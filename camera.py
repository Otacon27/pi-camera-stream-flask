#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
import imutils
import time
import numpy as np


class PiCamera(object):
    def __init__(self, flip = False):
        from imutils.video.pivideostream import PiVideoStream
        self.vs = PiVideoStream().start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


class WebCam(object):
    def __init__(self, flip = False):
        self.vs = cv2.VideoCapture(0)
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.release()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        ret, frame = self.vs.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        #ret, jpeg = cv2.imencode('.jpg', frame)
        return buffer.tobytes()
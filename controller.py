import os
import cv2
from detect import Detector
import time

class Controller:
    def __init__(self):
        self.detector = Detector()
    def getScreenShot(self):
        os.system("adb shell screencap -p /sdcard/tmp.png")
        os.system("adb pull /sdcard/tmp.png")
        img = cv2.imread("tmp.png")
        return img
    def tap(self):
        img = self.getScreenShot()
        h,w,t = img.shape
        print(img.shape)
        positons = self.detector.detect(img)
        print(positons)
        hRate = 1920 / 2243
        wRate = 1080 / 1079
        for x,y in positons:
            x = (x+20) / 800 * h
            y = (y+20) / 400 * w
            print(x,y)
            os.system("adb shell input tap " + str(int(y)) + " " + str(int(x)))
    def searchAvailableAndTap(self):
        img = self.getScreenShot()
        for i in range(img.shape[0]):
            if img[i,-1][0] ==  109:
                os.system("adb shell input tap " + str(100) + " " + str(int(i)))
                time.sleep(1)
                self.tap()
                time.sleep(1)
                os.system("adb shell input keyevent 4")
                img = self.getScreenShot()
                i += 100
    def swipe(self):
        os.system("adb shell input swipe 0 1000 0 0")
    def run(self):
        self.showMoreFriends()
        time.sleep(1)
        for i in range(10):
            self.searchAvailableAndTap()
            self.swipe()
        os.system("adb shell input keyevent 4")
    def showMoreFriends(self):
        img = self.getScreenShot()
        os.system("adb shell input tap " + str(100) + " " + str(int(img.shape[0] - 20)))


controller = Controller()
controller.run()
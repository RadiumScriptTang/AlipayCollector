import keras
import numpy as np
import cv2
import time

class Detector:
    def __init__(self):
        self.model = keras.models.load_model("model")
        self.windowSize = (100,100)
        self.windowStride = 10
    def detect(self,img,show=False):
        positions = []
        img = cv2.resize(img,(400,800))
        img = img[:350,:]
        for i in range(100,250,self.windowStride):
            for j in range(0,305,self.windowStride):
                x,y = i,j
                window = img[x:x+100,y:y+100]
                window = cv2.resize(window,(100,100))
                p = self.model.predict(np.array([window]))[0][1]
                if p > 0.59:
                    positions.append((x,y))
                    j += 80
        # for x,y in positions:
        #     cv2.rectangle(img,(y+10,x+10),(y+90,x+90),(0,255,0),2)
        # cv2.imshow("iamge",img)
        # cv2.waitKey(0)
        return positions
# detector = Detector()
# t1 = time.time()
# detector.detect("12.png")
# t2 = time.time()
# print(t2-t1)
# while True:
#     a = input()
#     t1 = time.time()
#     detector.detect(a + ".png")
#     t2 = time.time()
#     print(t2-t1)
import keras
import numpy as np
import cv2

model = keras.models.load_model("model")
img = cv2.imread("test_a.jpg")
img = cv2.resize(img,(100,100))
print(model.predict(np.array([img])))

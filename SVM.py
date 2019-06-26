from sklearn.svm import SVC
import numpy as np
import cv2
import matplotlib.pyplot as plt

female = np.array([[155,48],[159,50],[164,53],[168,56],[172,60]])
male = np.array([[152,53],[156,55],[160,56],[172,64],[176,65]])

label = np.array([-1 for i in range(5)]+[1 for i in range(5)])

data = np.vstack((female,male))
data = np.array(data,dtype="float32")

# print(data)
#
model = SVC()
model.fit(data,label)
model.decision_function()
print(model.predict(np.array([[173,80],[162,50]])))

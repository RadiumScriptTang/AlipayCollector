import cv2
import numpy as np

female = np.array([[155,48],[159,50],[164,53],[168,56],[172,60]])
male = np.array([[152,53],[156,55],[160,56],[172,64],[176,65]])

label = np.array([0 for i in range(5)]+[1 for i in range(5)])
data = np.vstack((female,male))
data = np.array(data,dtype="float32")

svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(0.01)
svm.train(data,cv2.ml.ROW_SAMPLE,label)
svm.predict(np.array([[160,49]]))
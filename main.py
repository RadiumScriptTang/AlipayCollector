import numpy as np
import cv2
import pickle
#设置参数
posNum = 20
negNum = 20
winSize = (64,128)
blockSize = (16,16)
blockStride = (4,4)
cellSize = (4,4)
binNum = 9

#创建hog
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,binNum)

#创建svm
svm = cv2.ml.SVM_create()

#准备 样本和标签
featureNum = 3780
featureArray = np.zeros((posNum + negNum , featureNum),dtype="float32")
labelArray = np.zeros((posNum + negNum , 1),dtype="int")

# 填充样本和标签
for i in range(0,posNum):
    img = cv2.imread('pos/'+str(i+1)+'.png')
    img = img[:600,:]
    hist = hog.compute(img,(4,4))
    for j in range(featureNum):
        featureArray[i,j] = hist[j]
    labelArray[i,0] = 1
for i in range(negNum):
    img = cv2.imread('neg/'+str(i+1)+'.png')
    img = img[:600,:]
    hist = hog.compute(img,(4,4))
    for j in range(featureNum):
        featureArray[i + posNum,j] = hist[j]
    labelArray[i + posNum, 0] = -1

print(featureArray)
#训练svm
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(1)

res = svm.train(featureArray,cv2.ml.ROW_SAMPLE,labelArray)

alpha = np.zeros((1),np.float)
rho = svm.getDecisionFunction(0,alpha)
alphaArray = np.zeros((1,1),np.float)
supportVector = np.zeros((1,featureNum),np.float)
resultArray = -1 * alphaArray * supportVector
alphaArray[0,0] = alpha

myDetector = np.zeros((3781),np.float)
for i in range(3780):
    myDetector[i] = resultArray[0,i]
myDetector[3780] = rho[0]
f = open("myDetector.txt","wb")
pickle.dump(myDetector,f)

hogDetector = cv2.HOGDescriptor()
hogDetector.setSVMDetector(myDetector)

imgTest = cv2.imread("pos/1.png",1)
imgTest = cv2.resize(imgTest, (64,128))

objs = hogDetector.detectMultiScale(imgTest,0,(4,4),(32,32),1.05,2)
x,y,w,h = int(objs[0][0][0]),int(objs[0][0][1]),int(objs[0][0][2]),int(objs[0][0][3])
cv2.rectangle(imgTest,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("image",imgTest)
cv2.waitKey(0)

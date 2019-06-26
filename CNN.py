import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,Convolution2D, MaxPooling2D, Flatten,Dropout
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

import cv2

posNum = 69
negNum = 65
imageList = []
labelList = []
for i in range(posNum):
    img = cv2.imread("pos/" + str(i+1) + ".png")
    img = cv2.resize(img,(100,100))
    imageList.append(img)
    labelList.append(1)
for i in range(negNum):
    img = cv2.imread("neg/" + str(i+1) + ".png")
    img = cv2.resize(img,(100,100))
    imageList.append(img)
    labelList.append(0)

X_train = np.array(imageList)
Y_train = np_utils.to_categorical(labelList,2)
print(Y_train)


model = Sequential([
    Convolution2D(50,(10,10),input_shape=(100,100,3)),
    Activation('tanh'),
    MaxPooling2D(4,4),
    Convolution2D(50,(4,4)),
    Activation("tanh"),
    MaxPooling2D(2,2),
    Dropout(0.25),
    Flatten(),
    Dense(100),
    Activation("tanh"),
    Dense(2),
    Activation("softmax")
])
sgd = SGD(lr=0.0001)
model.compile(
    optimizer=sgd,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train,Y_train, epochs=20, batch_size=30)
model.save("model")

# loss,accuracy = model.evaluate(X_test,Y_test)
#
# print('test loss:',loss)
# print("test accuracy:" ,accuracy)

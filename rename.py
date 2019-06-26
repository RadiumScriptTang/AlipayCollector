#coding:utf-8
import os
for root, dirs, files in os.walk("neg"):
    path = 'neg/'
    count = 1
    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path,str(count)+".png"))
        count += 1

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:28:56 2020

@author: zhangkerou
"""

import os
import random
 
def writeTxt(content,fileName):
    with open(fileName,'w') as f:
        for i in range(len(content)):
            name = content[i]
            f.writelines(name.strip('.jpg')+'\n')
    f.close()


root_PATH = r'C:\Users\zhangkerou\Desktop\R\vehicle_dataset\cons_vehcl_dataset'
img_PATH = root_PATH+'\jpgimages'
txt_PATH= root_PATH+'\ImageSets'
# os.chdir(img_PATH)
img_list = os.listdir(img_PATH)
random.shuffle(img_list)


train_ratio = 0.8
val_ratio = 0.1
test_ratio = 1-train_ratio-val_ratio


fileNum = int(len(img_list))
trainIndex = int(fileNum*train_ratio)
valIndex = int(fileNum*(train_ratio+val_ratio))



trainTxt = txt_PATH+'\\train.txt'
valTxt = txt_PATH+'\\val.txt'
testTxt = txt_PATH+'\\test.txt'
trainValTxt = txt_PATH+'\\trainVal.txt'

trainImgList = img_list[:trainIndex]
valImgList = img_list[trainIndex:valIndex]
testImgList = img_list[valIndex:]
trainValImgList = img_list[:valIndex]

writeTxt(trainImgList,trainTxt)
writeTxt(valImgList,valTxt)
writeTxt(testImgList,trainValTxt)
writeTxt(trainValImgList,testTxt)
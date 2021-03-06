
import os
import random


trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'VOC2007/Annotations'
txtsavepath = 'VOC2007/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('VOC2007/ImageSets/trainval.txt', 'w')
ftest = open('VOC2007/ImageSets/test.txt', 'w')
ftrain = open('VOC2007/ImageSets/train.txt', 'w')
fval = open('VOC2007/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()


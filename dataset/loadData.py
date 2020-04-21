import scipy.misc as misc
from keras.datasets import mnist
from PIL import Image
import os
import numpy as np

def gray_to_gray(imgArr):
    digit = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            ch1 = imgArr[i][j]
            if(ch1 < 150):
                digit[i][j] = 0
            else:
                digit[i][j] = ch1
    return digit

def load_image(imgs, labs):
    for a in range(len(imgs)):
        digit = gray_to_gray(imgs[a])
        im = Image.fromarray(digit)
        im = im.convert('RGB')
        if(not os.path.exists(str(labs[a]))):
            os.mkdir(str(labs[a]))
        im.save(str(labs[a])+"/"+str(count[labs[a]])+ ".jpg")
        count[labs[a]] = count[labs[a]] + 1

count = [0,0,0,0,0,0,0,0,0,0]# 0,1,2,3,4,5,6,7,8,9

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
load_image(train_images, train_labels)
load_image(test_images, test_labels)

print(count)
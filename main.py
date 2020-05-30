from training import *

temp = HaarTraining("car.jpg")
temp.resize_positive_image()
temp.train(num=1200,numPos=1100,numNeg=550)

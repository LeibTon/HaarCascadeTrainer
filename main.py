from training import *

temp = HaarTraining("car.jpg")
links = ["http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00021939"]
temp.store_negative_images(self,links)
temp.resize_positive_image()
temp.create_list()
temp.train(num=1200,numPos=1100,numNeg=550)

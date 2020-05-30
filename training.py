import urllib.request
import cv2
import numpy as np
import os

class HaarTraining:
    def __init__(self, positive_image, neg_loc="negative",pos_loc="positive"):
        self.neg_loc=neg_loc
        self.positive_image=positive_image
        self.pos_loc=pos_loc

    def store_negative_images(self,neg_image_links):
        if not os.path.exists(self.neg_loc):
            os.makedirs(self.neg_loc)

        pic = 460
        for neg_image_link in neg_image_links:
            neg_image_urls = urllib.request.urlopen(neg_image_link).read().decode()
            for i in neg_image_urls.split('\n'):
                try:
                    urllib.request.urlretrieve(i,self.neg_loc+"/"+str(pic)+'.jpg')
                    img=cv2.imread(self.neg_loc+"/"+str(pic)+'.jpg', cv2.IMREAD_GRAYSCALE)
                    resized_image = cv2.resize(img,(200,200))
                    cv2.imwrite(self.neg_loc+"/"+str(pic)+'.jpg',resized_image)
                    pic+=1
                except Exception as e:
                    print(str(e))


    def delete_bad_ones(self,uglies_dir):
        for file_type in [self.neg_loc]:
            for img in os.listdir(file_type):
                for ugly in os.listdir(uglies_dir):
                    try:
                        current_image_path=str(file_type)+'/'+str(img)
                        ugly = cv2.imread(uglies_dir+'/'+str(ugly))

                        picture=cv2.imread(current_image_path)
                        if ugly.shape==picture.shape and not(np.bitwise_xor(ugly,picture).any()):
                            os.remove(current_image_path)
                            print(current_image_path)
                    except Exception as e:
                        print(str(e))


    def create_list(self):
        for file_type in [self.neg_loc]:
            for img in os.listdir(file_type):
                if file_type ==self.neg_loc:
                    line=file_type+'/'+img+'\n'
                    with open('bg.txt','a') as f:
                        f.write(line)
                elif file_type == self.pos_loc:
                    line=file_type+'/'+img+'1 0 0 50 50\n'
                    with open('info.dat','a') as f:
                        f.write(line)


    def resize_positive_image(self,height=50,width=50):
        try:
            positive=cv2.imread(self.positive_image)
            resized=cv2.resize(positive,(width,height))
        except:
            print("Image doesn't exist")
            exit(0)
        cv2.imwrite(self.positive_image,resized)


    def train(self,maxxangle=0.5,maxyangle=-0.5,maxzangle=0.5,num=1165,numPos=1000,numNeg=500,numStages=5):
        command1="opencv_createsamples -img "+self.positive_image+" -bg  bg.txt -info info/info.lst -pngoutput info -maxxangle "+str(maxxangle)+" -maxyangle "+str(maxyangle)+" -maxzangle "+str(maxzangle)+" -num "+str(num)
        command2="opencv_createsamples  -info info/info.lst -num "+str(num)+" -w 20 -h 20 -vec positive.vec"
        if not os.path.exists("data"):
            os.makedirs("data")
        command3="opencv_traincascade -data data -vec positive.vec -bg bg.txt -numPos "+str(numPos)+" -numNeg "+str(numNeg)+" -numStages "+str(numStages)+" -w 20 -h 20"
        os.system(command1)
        os.system(command2)
        os.system(command3)

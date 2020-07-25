# HaarCascadeTrainer
## Training custom Haar cascades to detect complex objects.
***Before explaining the class details, lets focus on some terminology.***
1. The dataset required for training haar cascades should have the images with object and without object. Then a *.txt* file should contain the name of images with object, with the position of object in it. Generally it is difficult for doing this for large number of images. So we generate these using positive and negative images which are explained later.
2. **positive image:** This is the image of the object to be detected. It should be clear and contain only the object.
3. **negative images:** These are the images of background in which the object need to be detected. These images should not conatin the object that is to be detected. For example: *for detecting cars, images of roads acts as negative images.*
4. **Opencv Applications:** After setting up the dataset for training, we call 3 opencv applications: *opencv_createsamples, opencv_traincascade.*
### class Name: HaarTraining

While creating object of the class, the location of positive image, the location for folder with negative images (by default set to 'negative'), the location for folder with images with object {needed if you are creating your own .txt file} (by default set to 'positive').
```
temp = HaarTraining("cars.jpg","negative")
```
Functions within the class:
1. **store_negative_images(neg_image_links):** Note that we need negative images for training purpose. To download the images you can take help of [image-net](http://www.image-net.org/). Search for the images, Go to downloads, then click on url, copy the url of the web page(containing urls of images) that is opened. Make a list of such urls in [main.py](main.py) and pass it to the function store_negative_images() in place of neg_image_links.
This function downloads all images and save it to *negative* folder.
2. **delete_bad_ones(uglies_dir):** After downloading the images, some images are not desirable, basically due to *not found*, make a folder, copy all those images in that folder, and pass the location of that folder in place of *uglies_dir*.
3. **create_list():** Now all images are downloaded and filtered, its time to create the list of images that are stored for training. Just call the function, it will make *bg.txt*, a list of images.
4. **resize_positive_images(height, width):** If you wanna resize the positive image, pass height(*by default, 50*) and width(*by default, 50*).
5. **train(maxxangle,maxyangle,maxzangle,num,numPos,numNeg,numStages):** Now every thing is set, it's time to train the cascades. This fucntion starts training, the parameters are set to default values, you can pass it if you wish to change. However, the value of num, numPos,numNeg and numStages, depends on the number of negative images available. 
-*num* is number of negative images.
-*numPos* number of negative images with object you want to make, it should be less than *num*.
-*numNeg* should be approx. half of *numPos*.
-*numStages* affects the training part. In how many stages you want to train model. It increases with number of negative images.
Here are the commands:
```
opencv_createsamples -img positive_image -bg  bg.txt -info info/info.lst -pngoutput info -maxxangle (maxxangle) -maxyangle (maxyangle) -maxzangle maxzangle -num (num)
opencv_createsamples  -info info/info.lst -num (num) -w 20 -h 20 -vec positive.vec
opencv_traincascade -data data -vec positive.vec -bg bg.txt -numPos numPos -numNeg (numNeg) -numStages (numStages) -w 20 -h 20
```
Here the first command creates, background image with object, check info folder after running this command. Second one creates *.vec*. And then third one finally begins training.

If you need more help, watch this:
> [Custom Haar Cascade Training](https://www.youtube.com/watch?v=jG3bu0tjFbk)

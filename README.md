

# Agriprotec

## Abstract
Time since there exsisted the problem of wild animals entering and destroying crops in farmlands adjoining forests in Kerala.As per the field survey conducted by  Kerala Forest
Department, the main animals involved in crop damage were elephant (Elephas maximus ),gaur (Bos gaurus), sambar (Cervus unicolor), wild boar (Sus scrofa ), bonnet macaque (Macaca radiata), common langur (Presbytis entellus).Among these,elephant and wild boar did maximum damage.Conventional system of electrified wire fences is not an efficient method as long-term success has often fallen well below expectation and also due to the danger to non-targeted species.

As a solution to this problem,Agriprotec has made a system that tracks,identifies and takes apt solution only against the targeted threat.In this endure we implanted PIR sensors
inside the forest area,when it detects motion of any animal it tiggers the microcontroller active from sleep and sends a signal to the inteligent camera system which capture of image from the active sensor area,processes the image and identifies if it an elephant or boar.If it is an elephant then the system activates the siren which produces buzz sound
if boar then system activates the strobe light + siren.by this kind of system we were able to save cost and electric energy.



## Research Question 
Is Capsule Network better than Convolutional Neural Network in classifying wild animal
species in camera trap images?

## Dataset
An annotated camera-trap dataset of 20 species commonly found in North - America is used for training the model. The dataset contains 15826 images of 20 species namely Agouti, Bird spec, Coiban Agouti, Collared Peccary, Common Opossum, European
Hare, Great Tinamou, Mouflon, Ocelot, Paca, Red Brocket Deer, Red Deer, Red Fox, Red Squirrel, Roe Deer, Spiny Rat, White Tailed Deer, White-nosed Coati, Wild Boar, and Wood Mouse. The dataset contains a collection of gray-scale and color images. 

The images captured at night are in gray-scales and images captured in daytime are in colored.

Every image contains only one species out of 20 species. 80% of the dataset, i.e., 12660 images is used for training and the rest 20% for testing.

Link to Dataset Repo 

https://data.world/deana/camera-traped-wild-animals-images

or

https://drive.google.com/open?id=14vII7LJP8Hv-Uz4Av5DA33_Hyz95PL0I


![](Images/Page_00.png)
![](Images/Page_01.png)

## 

## Hardware Used

Since image recognition using deep learning involves many complex matrix calculations, training a model requires a certain amount of computing resources. In recent year, the use of GPU ( Graphical Processing Units) is becoming popular for deep learning, without which the training would take several days or months to obtain practical results.

For the experiment, two systems are used as mentioned below:

(i) A Macintosh with macOS High Sierra (v10.13.3) with 1.8 GHz Intel Core i5, memory of 8GB 1600 MHz DDR3 and Intel HD Graphics 6000 of 1536 MB, to execute Convolutional Neural Network.

(ii) A cloud computing instance; Amazon's Web Services (AWS) EC2 cloud computing (Elastic Compute 2), is set up with g2.2xlarge GPU. This version of the instance has 15GB Memory, 60GB of local SSD storage, 8 vCPU and a single NVIDIA Kepler GK104 graphics card with 1536 CUDA cores, for the execution of Capsule Network.

# Programming language used

Python 3 is used as the programming language with keras framework using tensorflow backend. Keras is a user-friendly open source neural network library written in python. It can be used on top of tensorflow or theano.

# Traning the networks

The Convolutional Neural Network was trained on the first-mentioned hardware, and the Capsule Network was trained on the AWS cloud instance. Both the networks are trained using ADAM optimizer with an initial learning rate of 0.001. Since training
both the models is time-consuming and computationally expensive, the number of epochs chosen was 40 and a batch size of 32 for both the models.  

# Results 




# Conclusions




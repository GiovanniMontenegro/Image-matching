# Image-matching
Image matching and calculation of fourier descriptors

I created a proj to calculate the fourier descriptor that are scaling and rotation invariant.

The result is using SURF.

In the class FourierSurf in Descriptor.py we have:
-def setImage(self,imgUrl) 
  set the image for which have to calculate the descriptor. imgUlr = just the name of the image with extension
	
-def calculateDescriptors(self)
  Calculate the descriptors and write them on csv file with the name of the image.

-def setTwoImages(self,imgUrl1,imgUrl2):
  set two images for which have to calculate the similarity.

-def calculateSimilarity(self):
  calculate the similarity and print the results.
  
  The percentage is given by the key point matched divide by the max key point between the two images

-def takeImageName(self)
  method to have the name of the image without extension.

-def setLocalUrl(self,str):
  set the local path for the folder

The result of Test.py are:

--Test 1--Obtain csv of descriptors
apple-1.csv saved with success
--Test 2--Similarity between the same image
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  65
Keypoint matched:  65
Similarita':  100.0 %
--Test 3--Similarity between an apple and a rotate apple
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  65
Keypoint matched:  65
Similarita':  100.0 %
--Test 4--Similarity between an apple and a scaled apple
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  30
Keypoint matched:  49
Similarita':  75.3846153846 %
--Test 5--Similarity between an apple and a bat
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  381
Keypoint matched:  6
Similarita':  1.57480314961 %
--Test 5--Similarity between an apple and a camel
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  190
Keypoint matched:  17
Similarita':  8.94736842105 %
--Test 5--Similarity between an apple and a device 
Number of KeyPoint of the first image:  65
Number of KeyPoint of the second image:  197
Keypoint matched:  5
Similarita':  2.53807106599 %

The images are in mpeg7 folder.

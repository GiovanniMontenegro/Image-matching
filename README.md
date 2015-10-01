# Image-matching
Image matching and calculation of fourier descriptors

I created a proj to calculate the fourier descriptor that are scaling and rotation invariant.

The result is using SURF.

In the class FourierSurf in Descriptor.py we have: <br>
-def setImage(self,imgUrl)  <br>
  set the image for which have to calculate the descriptor. imgUlr = just the name of the image with extension
	
-def calculateDescriptors(self) <br>
  Calculate the descriptors and write them on csv file with the name of the image.

-def setTwoImages(self,imgUrl1,imgUrl2): <br>
  set two images for which have to calculate the similarity.

-def calculateSimilarity(self): <br>
  calculate the similarity and print the results.
  
  The percentage is given by the key point matched divide by the max key point between the two images

-def takeImageName(self) <br>
  method to have the name of the image without extension.

-def setLocalUrl(self,str): <br>
  set the local path for the folder

The result of Test.py are:

--Test 1--Obtain csv of descriptors <br>
apple-1.csv saved with success <br>
--Test 2--Similarity between the same image <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  65 <br>
Keypoint matched:  65 <br>
Similarita':  100.0 % <br>
--Test 3--Similarity between an apple and a rotate apple <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  65 <br>
Keypoint matched:  65 <br>
Similarita':  100.0 % <br>
--Test 4--Similarity between an apple and a scaled apple <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  30 <br>
Keypoint matched:  49 <br>
Similarita':  75.3846153846 % <br>
--Test 5--Similarity between an apple and a bat <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  381 <br>
Keypoint matched:  6 <br>
Similarita':  1.57480314961 % <br>
--Test 5--Similarity between an apple and a camel <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  190 <br>
Keypoint matched:  17 <br>
Similarita':  8.94736842105 % <br>
--Test 5--Similarity between an apple and a device  <br>
Number of KeyPoint of the first image:  65 <br>
Number of KeyPoint of the second image:  197 <br>
Keypoint matched:  5 <br>
Similarita':  2.53807106599 % <br>

The images are in mpeg7 folder.

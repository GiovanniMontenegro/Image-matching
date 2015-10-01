__author__ = 'Giovanni Montenegro'
import cv2
import numpy as np
class FourierSurf:

    localUrl = ""
    #  SURF Definition
    # The threshold determines how large the output from the Hessian filter must be in order for a point to be used
    # as an interest point. A larger value will result in fewer, but (theoretically) more salient interest points,
    # whereas a smaller value will result in more numerous but less salient points. (take from StackExchange)
    # In my testing, I noticed that over 1000 there isn't a great improvement. So I put 1000 as threasold.
    minHessian = 1000
    surf = cv2.SURF(minHessian)

    #variable for 2 images comparison
    img1 = ""
    img2 = ""
    keyPoint1 = ""
    keyPoint2 = ""
    descriptors1 = ""
    descriptors2 = ""

    #variable for 1 image descriptor calculation
    img = ""
    imgName = ""
    keyPoint = ""
    descriptors = ""


    #set the image url and load it
    def setImage(self,imgUrl):
        self.imgName = imgUrl
        self.img= cv2.imread(self.localUrl+imgUrl,0)

    #calculate and save in a csv, the descriptors value.
    #the saved output is a 2D matrix
    def calculateDescriptors(self):

        # Find keypoints and descriptors directly
        self.keyPoint, self.descriptors = self.surf.detectAndCompute(self.img,None)
        imageName = self.takeImageName()
        np.savetxt(imageName+'.csv', self.descriptors, delimiter=';')
        print imageName+".csv saved with success"

    #Set the two images url and load them
    def setTwoImages(self,imgUrl1,imgUrl2):
        self.img1= cv2.imread(self.localUrl+imgUrl1,0)
        self.img2 = cv2.imread(self.localUrl+imgUrl2,0)

    #Calculate the similarity between two images (use setTwoImages first)
    def calculateSimilarity(self):

        # Find keypoints and descriptors directly
        self.keyPoint1, self.descriptors1 = self.surf.detectAndCompute(self.img1,None)
        self.keyPoint2, self.descriptors2 = self.surf.detectAndCompute(self.img2,None)

        # BFMatcher with default params
        # REF: http://docs.opencv.org/master/d3/da1/classcv_1_1BFMatcher.html#gsc.tab=0
        bf = cv2.BFMatcher()
        # knnMatch() Finds the k best matches for each descriptor from a query set.
        matches = bf.knnMatch(self.descriptors1,self.descriptors2, k=2)

        # Apply ratio test
        good = []
        for m,n in matches:
         if m.distance <= 0.75*n.distance:
             good.append([m])

        print "Number of KeyPoint of the first image: ",len(self.keyPoint1)
        print "Number of KeyPoint of the second image: ",len(self.keyPoint2)
        print "Keypoint matched: ",len(good)

        #Compute the similarity.
        #the number of matched key points divided by the max number of Key Point
        #between the 2 images.
        sim = float(len(good))/max(len(self.keyPoint1),len(self.keyPoint2))
        print "Similarita': ",sim*100,"%"

    #take the image name from the url
    def takeImageName(self):
        l = list(self.imgName)
        str = ""
        for c in l:
            if(c == "."):
                break
            str += c
        return str

    def setLocalUrl(self,str):
        self.localUrl = str

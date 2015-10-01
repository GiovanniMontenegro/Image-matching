__author__ = 'Giovanni Montenegro'
from  Descriptor import FourierSurf

ds = FourierSurf()
#Set the local reference for images
ds.setLocalUrl("C:/Users/yourUserName/whereYouPutTheFolder/mpeg7/")

print "--Test 1--Obtain csv of descriptors"
ds.setImage("apple-1.tiff")
ds.calculateDescriptors()

print "--Test 2--Similarity between the same image"
ds.setTwoImages("apple-1.tiff","apple-1.tiff")
ds.calculateSimilarity()

print "--Test 3--Similarity between an apple and a rotate apple"
ds.setTwoImages("apple-1.tiff","apple-rotate.tiff")
ds.calculateSimilarity()

print "--Test 4--Similarity between an apple and a scaled apple"
ds.setTwoImages("apple-1.tiff","apple-scale.tiff")
ds.calculateSimilarity()

print "--Test 5--Similarity between an apple and a bat"
ds.setTwoImages("apple-1.tiff","bat-1.tiff")
ds.calculateSimilarity()

print "--Test 5--Similarity between an apple and a camel"
ds.setTwoImages("apple-1.tiff","camel-1.tiff")
ds.calculateSimilarity()

print "--Test 5--Similarity between an apple and a device "
#the devide in this situation is very similar
ds.setTwoImages("apple-1.tiff","device9-3.tiff")
ds.calculateSimilarity()



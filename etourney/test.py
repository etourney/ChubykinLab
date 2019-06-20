import numpy
import cv2 as cv
import os

#Load image
pngdir = os.path.dirname(os.path.abspath(__file__))
inppng = pngdir + "\\download.jpg"
img = cv.imread(inppng,1)
#print(img.shape)

#chunk = img[100:200, 100:200]
#img[200:300, 200:300] = chunk
#img2 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
kernel = numpy.ones((5,5),numpy.uint8)
img2 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
#img2 = cv.Canny(img,100,200)

#Show image
cv.imshow('trialpic',img2)
cv.waitKey(0)
cv.destroyAllWindows()

#Write image
outpng = pngdir + "\\outputpic.jpg"
cv.imwrite(outpng,img2)

#https://gke.mybinder.org/v2/gh/chubykin/AutoPatcher_IG/master
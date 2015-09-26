__author__ = 'John'

import cv2
import numpy as np

#cv2.waitKey(0)
#cv2.imshow('img',img)
#cv2.destroyAllWindows

# step 1: take a picture
# credit: http://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/

print"turning on camera"
camera = cv2.VideoCapture(0)

print "setting up camera"
def get_image():
    retval, im = camera.read()
    return im


print "taking picture"
#take picture
camera_capture = get_image()

#picture path
location = "C:/Users/John/Desktop/Current.png"
location2 = "C:/Users/John/Desktop/Processed.png"
location3 = "C:/Users/John/Desktop/Lines.png"

#save picture
print "saving picture"
#cv2.imwrite(location, camera_capture)

#create a processed image

print "saving initial processed picture"
#cv2.imwrite(location2, camera_capture)




img = cv2.imread(location)
# codeplazma.com

del(camera)

# step 3: process image for color

print "initalizing variables"

x = 0
y = 0
xmax = 480
ymax = 640
mod = 10  #modifier for sensitivity


cv2.imshow('img1',img)  #show image
cv2.waitKey(500)        #whow image

print "setting up arrary"
RGB = np.empty([xmax,ymax], dtype=int)

print "processing image"
while y < ymax:
    x = 0
    while x < xmax:
        #print "\n CHECKING PIXEL AT POS", y,",", x
        B = img[x,y,0]
        G = img[x,y,1]
        R = img[x,y,2]


        if B < 150 and R < 150 and G < 150:
            img[x,y] = [0,0,0]
            RGB[x,y] = 0

        if B > G and B > R:
            img[x,y] = [255,0,0]
            RGB[x,y] = 1

        elif G > B + mod and G > R + mod:
            img[x,y] = [0,255,0]
            RGB[x,y] = 2

        elif R > G + mod and R > B + mod:
            img[x,y] = [0,0,255]
            RGB[x,y] = 3

        else:
            img[x,y] = [255,255,255]
            RGB[x,y] = 4
        x += 1
    y += 1
print "saving processed picture"

cv2.imwrite(location2, img)
cv2.imshow('img1',img)
cv2.waitKey(500)

##############
# V LINE CODE#
##############

print "saving line image"
cv2.imwrite(location3, img)

y = 0
x = 0
nr = 0  # number of red pixles
nb = 0  # blue pixles
ng = 0  # green pixles
line = np.empty([xmax,ymax], dtype=int)  #create a line array with dimensions x max,y max that is only used for intergers
sens = 450  # sensitivity

print "processing second image"
while y < ymax:
    x = 0
    nr = 0
    nb = 0
    ng = 0
    while x < xmax:
        if RGB[x,y] == 3:
            nr += 1
        elif RGB[x,y] == 1:
            nb += 1
        elif RGB[x,y] == 2:
            ng += 1
        x += 1
    x = 0

    #print y, nb, ng, nr, "\n"
    if nr > sens:
        while x < xmax:
            line[x,y] = 3
            img[x,y] = [0,0,255]
            x += 1
    elif nb > sens:
        while x < xmax:
            line[x,y] = 1
            img[x,y] = [255,0,0]
            x += 1
    if ng > sens:
        while x < xmax:
            line[x,y] = 2
            img[x,y] = [0,255,0]
            x += 1
    else:
        while x < xmax:
            line[x,y] = 0
            img[x,y] = [0,0,0]
            x += 1
    y += 1

print "processing x of second image image"



##############
# H LINE CODE#
##############

sensB = 400  # sens for the other direction
x = 0

while x < xmax:
    y = 0
    nr = 0
    nb = 0
    ng = 0
    while y < xmax:
        if RGB[x,y] == 3:
            nr += 1
        elif RGB[x,y] == 1:
            nb += 1
        elif RGB[x,y] == 2:
            ng += 1
        y += 1
    y = 0

    #print y, nb, ng, nr, "\n"
    if nr > sensB:
        while y < ymax:
            line[x,y] = 3
            img[x,y] = [0,0,255]
            y += 1
    elif nb > sensB:
        while y < ymax:
            line[x,y] = 1
            img[x,y] = [255,0,0]
            y += 1
    if ng > sensB:
        while y < ymax:
            line[x,y] = 2
            img[x,y] = [0,255,0]
            y += 1
    #else:
    #    while y < ymax:
    #       line[x,y] = 0
    #        img[x,y] = [0,0,0]
    #        y += 1
    x += 1

print "saving line image"
cv2.imwrite(location3, img)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

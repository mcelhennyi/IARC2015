__author__ = 'John'

__author__ = 'John'

import numpy as np
import cv2
import time


camera = cv2.VideoCapture(-1) # turns on camera
print "%r" %camera

def get_image():
    retval, im = camera.read() # reads from camera
    return im

global LARY
global xmax
global ymax
global height
global img

#height = float(raw_input("How high is the camera in meters"))
height = 3
xmax = 480
ymax = 640

img = cv2.imread("C:/Users/John/Desktop/IARC/corner2.png")
xmax, ymax = img.shape[:2]
print "xmax:", xmax, "  ymax:,",ymax
LARY = np.zeros([xmax, ymax], dtype = int)
llistx = []
llisty = []

ysearch = ymax /2
xsearch = xmax /2

rho = 100.0
theta = 10.0

print "def main... \t \t",
def main(LARY):
    #img = get_image()
    img = cv2.imread("C:/Users/John/Desktop/IARC/corner2.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,10,10,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,60)


    #cv2.imshow('edges image',edges)

    if lines is not None:
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            # horizontal lines 70 to 110 deg
            if 1.50< theta < 1.64:
                cv2.line(LARY,(x1,y1),(x2,y2),(1),1)
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

            # verticle lines 160 to 200 deg
            if 3 < theta < 3.28:
                cv2.line(LARY,(x1,y1),(x2,y2),(2),1)
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

            #else:
            #   cv2.line(LARY,(x1,y1),(x2,y2),(1),2)


    #cv2.imshow("edges",edges)
    cv2.waitKey(3)
    cv2.imshow("lineimage", img)

    cv2.waitKey(5)
    return LARY
print "done"

print "def LARYprinting... \t",
def LARYprinting(xmax, ymax):
    y = 0
    while y < ymax:
        x = 0
        while x < xmax:
            print LARY[x, y],
            x += 2
        print "\n"
        y += 2
print "done"


print "def angtolength... \t",
def angtolength(dist):
    length = height*dist/738.6
    print length, "m"
    return length
print "done"

print "def angtolength_x... \t",
def angtolength_x(dist):
    length = height*dist/718.7lj
    print length, "m"
    return length
print "done"

print "def angtolengths... \t",
def angtolengths(x, y):

    print x,"\t\t\t",y

    if x == 999:
        lengthx = 990
    else:
        lengthx = height*x/718.7
    print lengthx, "m\t\t",

    if y == 999:
        lengthy = 990
    else:
        lengthy = height*y/738.6
    print lengthy, "m"
print "done"

print "def search...\t",
def search(llistx,llisty):

    LARY = np.zeros([xmax, ymax], dtype = int)
    main(LARY)

    #print "horizontal lines \t\t",
    dist = 0
    searchc = xmax / 2
    check5(dist, LARY, searchc, llistx)
    llistx.sort()

    #print "verticle lines \t\t",
    dist_y = 0
    searchc = ymax / 2
    check_y5(dist_y, LARY, searchc, llisty)
    llisty.sort()

    return llistx, llisty
print "done"

print "def check5... \t \t",
def check5(dist, LARY, searchc, llistx):
    if LARY[(searchc+dist), ysearch] == 1:
        llistx.append(dist+240)

    if LARY[(searchc-dist), ysearch] == 1:
        llistx.append(-dist+240)

    dist += 1
    if dist+searchc+1 > xmax:
        return

    check5(dist, LARY, searchc, llistx)
print "done"

print "def check_y5... \t",

def check_y5(dist, LARY, searchc, llisty):
    if LARY[xsearch, (searchc+dist)] == 2:\
        llisty.append(dist+320)

    if LARY[xsearch, (searchc-dist)] == 2:\
        llisty.append(-dist+320)

    dist += 1
    if dist+searchc+1 > ymax:
        return

    check_y5(dist, LARY, searchc, llisty)
print "done"

#start = time.time()

print"def center... \t",
def center():
    llistx = []
    llisty = []

    search(llistx,llisty)

    #print llistx
    #print llisty

    if not llistx:
        xmove = 999
    else:
        xmove= min(llistx, key=lambda x:abs(x-0))

    if not llisty:
        ymove = 999
    else:
        ymove = min(llisty, key=lambda x:abs(x-0))

    angtolengths(xmove,ymove)
print "done"

print "def PXbrightness (px)...\t",
def pxbrightness(img,x,y):

    img = cv2.imread("C:/Users/John/Desktop/IARC/corner2.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print gray[xmax-x,y]
print"done"

print "def edgecheck... \t",
def edgecheck(llisty,llistx):


    tollerence = 30

    #img = get_image()

    img = cv2.imread("C:/Users/John/Desktop/IARC/corner2.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("greyimage", gray)

    search(llistx,llisty)

    if not llistx:
        xlow = 999
    else:
        xlow= min(llistx)

    if not llisty:
        ylow = 999

    else:
        ylow = min(llisty)

        #print  line to check on the image
        cv2.line(img,(xlow,0),(xlow,ymax),(0,0,255),2)
        cv2.imshow("checking this line", img)
        cv2.waitKey(5)

       #check the leftmost verticle lines
        if xlow is not 999:
            print "1 is line right, 2 is line both ways, 3 is line left, 0 is confuse"
            llistytl =[]
            print "Y (xlow) line type", xlow
            ycount = len(llisty)
            yline = 0

            while yline < ycount:

                cbrightness = gray[xlow, llisty[yline]]
                print cbrightness,

                left = False
                LR = -30
                Lbrightness = gray[xlow + LR, llisty[yline]]
                if cbrightness - tollerence < Lbrightness < cbrightness + tollerence:
                    left = True
                print Lbrightness,

                right = False
                LR = 30
                Rbrightness = gray[xlow + LR, llisty[yline]]
                if cbrightness - tollerence < Rbrightness < cbrightness + tollerence:
                    right = True
                print Rbrightness


                if left == True and right == True:
                    list.append(llistytl, 2)
                elif left == True and right == False:
                    list.append(llistytl, 3)
                elif left == False and right == True:
                    list.append(llistytl, 1)
                elif left == False and right == False:
                    list.append(llistytl, 0)

                yline += 1
            print "\n", llisty
            print llistytl
        else:
            print "no verticle line"
print "done"

whatdoP = "c"
print "\nWhen prompt, enter a method"
while True:


    whatdo = raw_input("What can I do for you?\n")
    #whatdo = "edgecheck"

    if whatdo == "center":
        print "center:"
        center()
    elif whatdo == "edgecheck":
        edgecheck(llisty,llistx)
    elif whatdo == "break":
        break
    elif whatdo == "search":
        llistx =[]
        llisty = []
        search(llistx,llisty)
        print llistx
        print llisty
    elif whatdo == "px":
        x = raw_input("x:",)
        y = raw_input("y:",)
        pxbrightness(img,x,y)
    elif whatdo == "loop":
        print "sorry, I didn't code a loop into this software"
    else:
        print "unrecognized command"

    #cv2.waitKey(0)

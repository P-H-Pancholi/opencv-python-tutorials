#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:00:38 2020

@author: phalinp
"""

import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),dtype = np.uint8)
cv.namedWindow('image')

#create trackbar for colour change
#we slide the trackbar and corresponding colour of the window changes
#Here, I have created 3 trackbar for 3 colors.
#If we don't specify trackbar of any colour by default it's value will be 255
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)


#As opencv doesn't provide switch, I have created trackbar for switch, thus
#if we don't slide it changes won't happen in the image
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch,'image',0,255,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    #get current position of four trcakbar
    r = cv.getTrackbarPos('R','image')
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    s = cv.getTrackbarPos(switch,'image')
    
    if s == 0:
        #if switch is not enabled
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()
    

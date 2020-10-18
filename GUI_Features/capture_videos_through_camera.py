#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:41:45 2020

@author: phalinp
"""

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#Creates a VideoCapture Object, Argument can be device index or file name

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    #ret:bool , if frame read correctly ret will be true
    
    if not ret:
        print("Cannot recieve frame")
        break
        
    #operations on frame come here
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break


#when everything done, release the capture
cap.release()
cv.destroyAllWindows()

#To access feature of the video cv.get(propId) and To modify feature
#cv.set(propId,value)

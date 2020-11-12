#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:33:40 2020

@author: phalinp
"""
import numpy as np
import cv2 as cv

drawing = False #true if mouse pressed
mode = True #if true, draw rectangle. press m to toggle
ix,iy = -1,-1

def draw_circle_or_rectangle(event,x,y,flags,param):
    """
    This funtion is a mouse call back function and will draw rectangle or
    circle depending on boolean value of mode
    """
    global ix,iy,drawing,mode
    
    if event == cv.EVENT_LBUTTONDOWN:
        #whenever left button of mouse is clicked, the x,y coordinates are 
        #stored in global variables
        drawing = True
        ix, iy = x,y
        
    elif event == cv.EVENT_MOUSEMOVE:
        #cv.EVENT_MOUSEMOVE shows that mouse has been moved in the window
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
                
    elif event == cv.EVENT_LBUTTONUP:
        #cv.EVENT_LBUTTONUP indicates that the left mouse button is released
        if drawing == False:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
                
img = np.zeros((512,512,3), dtype = np.uint8)
cv.namedWindow('Image')
cv.setMouseCallback('Image',draw_circle_or_rectangle)

while(1):    
    cv.imshow('Image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        #to change mode from rectangle -> circle or vice versa
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()

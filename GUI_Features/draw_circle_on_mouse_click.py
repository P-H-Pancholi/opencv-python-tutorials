#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:42:57 2020

@author: phalinp
"""

import numpy as np
import cv2 as cv

def draw_circle(event,x,y,flags,param):
    """
    Parameters passed: event related to mouse like right click, left click
    x,y coordinates of mouse click and optional parameters.
    This function draws circle around the mouse click.
    """
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3),dtype = np.uint8)
#Create a black image and bind mouse callback function 
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
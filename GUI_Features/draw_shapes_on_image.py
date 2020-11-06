#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:54:41 2020

@author: phalinp
"""

import cv2 as cv
import numpy as np


def draw_rectangle(img):
    cv.rectangle(img,(384,0),(510,128),(0,255,255),3)
    
    #For rectangle if have to give top left corner i.e. (384,0)
    #and bottom right i.e (510,128) (0,255,255) is colour and 3 is
    #thickness
    
    cv.imshow("image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def draw_circle(img):
    cv.circle(img,(447,63),63,(0,0,255),-1)
    
    #for circle, center(447,63), radius = 63, colour and thickness is needed
    #thickness = -1 to fill colour in circle.
    
    cv.imshow("image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def draw_ellipse(img):
    cv.ellipse(img,(200,200),(100,100),0,0,360,(0,0,255),-1)
    
    #For ellipse we have to define the center, the length of major and minor 
    #axes, angle of rotation of ellipse in anticlock vise direction, startangle
    # and endangle denotes start and end of ellipse arc
    
    cv.imshow("image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():
    img = np.zeros((512,512,3), dtype = np.uint8)
    
main()
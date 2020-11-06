#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:14:42 2020

@author: phalinp
"""
import cv2 as cv
import numpy as np

def opencv_logo(img):
    cv.ellipse(img,(150,200),(50,50),45,90,360,(0,0,255),20)
    cv.ellipse(img,(90,300),(50,50),290,90,360,(0,255,0),20)
    cv.ellipse(img,(220,300),(50,50),310,0,270,(255,0,0),20)

    cv.imshow("Opencv logo",img)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    
def main():
    img = np.zeros((512,512,3), dtype = np.uint8)
    opencv_logo(img)    
main()
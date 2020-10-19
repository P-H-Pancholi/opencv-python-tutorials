#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:43:21 2020

@author: phalinp
"""

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img is a black image to draw a line

cv.line(img,(0,0),(511,511),(255,0,0),10)
#Creates a line starting from (0,0) to (511,511) in img, (255,0,0) describes
#colour which is Blue as per BGR and 10 is thickness of line in px

 
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()

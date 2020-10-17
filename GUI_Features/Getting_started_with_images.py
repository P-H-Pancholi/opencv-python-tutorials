#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:03:48 2020

@author: phalinp
"""

import sys
import cv2 as cv

img = cv.imread("lena_cut.png")

if img is None:
    sys.exit("Could not find the image")

cv.imshow("Display Window",img)
cv.waitKey(0)
cv.destroyAllWindows()



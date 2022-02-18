#!/usr/bin/env python
# coding: utf-8


import pydicom as dicom
import matplotlib.pyplot as plt
import numpy as np
import os
#import cv2
from PIL import Image
import pandas as pd
import csv
import sys
import cv2



def read_xray(path):
    
    dcm = dicom.read_file(path)    
    data = dcm.pixel_array
    img2show = Image.fromarray(data)
    # Convert pixel_array (img) to -> gray image (img_2d_scaled)
    ## Step 1. Convert to float to avoid overflow or underflow losses.   
    img_2d = data.astype(float) 
    ## Step 2. Rescaling grey scale between 0-255
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0
    ## Step 3. Convert to uint
    img_2d_scaled = np.uint8(img_2d_scaled) #1024,1024
    #new_img = np.stack((img_2d_scaled,)*3, axis=-1)
    img2 = cv2.cvtColor(img_2d_scaled,cv2.COLOR_GRAY2RGB)
    
        
    return img2, img2show


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:09:02 2024

@author: adiag
"""

##############################
# "1" for Windows
# "2" for Mac
##############################

import pandas as pd
import sys
import os
import warnings
warnings.filterwarnings('ignore')

def read_csv():
    device = int(input("Select 1 if you are working in Windows Laptop and 2 for MacBook: "))

    if device == 1:
        os.chdir("D:/OneDrive - Northeastern University/Data-Science-datasets")
        print("Location changed for Windows")
        print("Updated Location is: D:/OneDrive - Northeastern University/Data-Science-datasets")

    elif device == 2:
        os.chdir("/Users/adityaagarwal/Library/CloudStorage/OneDrive-NortheasternUniversity/Data-Science-datasets/")
        print("Location changed for Mac")
        print("Updated Location is: /Users/adityaagarwal/Library/CloudStorage/OneDrive-NortheasternUniversity/Data-Science-datasets")
    else:
        print("Either enter 1 or 2")
#df = pd.read_csv("./Flight Status Prediction/Combined_Flights_2022.parquet")
#df.head(3)

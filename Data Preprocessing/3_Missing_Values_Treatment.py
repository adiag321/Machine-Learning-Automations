# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:05:26 2024

@author: adiag
"""
###################################
# Handling Missing Values
###################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

def identify_miss_val(data):
    print("Missing values in each row --")
    data.isnull().sum()

    print("Plot of missing values --")
    sns.heatmap(data.isnull(), yticklabels=False, cbar=False, cmap='viridis')
    
    
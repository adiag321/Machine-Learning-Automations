# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:36:59 2024

@author: adiag
"""
################################
## Feature Scaling
# 1. Standarization
# 2. Normalization
# 2.1 MinMaxScaler
# 2.2 MinAbsScaler
################################

import numpy as np
import pandas as pd
import os
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings("ignore")

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

### Plot for showing the difference in the plots
def diff_plot(data, mod_data, col1, col2):
    # Original Plot
    fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize=(18,5))
    sns.histplot(data = data, x = col1, ax = axes[0,0])
    sns.histplot(data = data, x = col2, ax = axes[0,1])
    sns.scatterplot(data = data, x = col1, y = col2, ax = axes[0,2])
    
    # Standardized plot
    sns.histplot(data = mod_data, x = col1, ax = axes[1,0])
    sns.histplot(data = mod_data, x = col2, ax = axes[1,1])
    sns.scatterplot(data = mod_data, x = col1, y = col2, ax = axes[1,2])
    plt.show()

def feature_scaling(data):
    type = int(input("Select 1 for Standarzation, 2 for MinMaxScaler (Normalization), 3 for MinAbsScaler (Normalization)"))
    print("Pass only Numeric Values")
    
    if type == 1:
        ## Standardization
        column1 = str(input("Select column 1"))
        column2 = str(input("Select column 2"))
        
        # Scaling the data
        scaler = StandardScaler()
        standardscaler_df = pd.DataFrame(scaler.fit_transform(data), columns = data.columns)
        
        # Plotting the scaled data
        diff_plot(data = data, mod_data = standardscaler_df, col1 = column1, col2 = column2)
        
        print("Performed Standarization")
    
    elif type == 2:
        ## Normalization: MinMaxScaler
        column1 = str(input("Select column 1"))
        column2 = str(input("Select column 2"))
        
        # Scaling the data
        scaler = MinMaxScaler()
        minmaxscaler_df = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
        
        # Plotting the scaled data
        diff_plot(data = data, mod_data = minmaxscaler_df, col1 = column1, col2 = column2)
        
        print("Performed Normalization")
    
    else:
        print("Enter either 1 or 2 or 3")
    
  
#df = sns.load_dataset('tips')
#df = df[['total_bill', 'tip']]
#df.head()

# feature_scaling(df)

# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 22:18:11 2024

@author: adiag
"""

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

device = int(input("Select 1 for Windows and 2 for Mac"))
if device == 1:
    os.chdir("D:/OneDrive - Northeastern University/Jupyter Notebook/Machine Learning Algorithms/Datasets")
else:
    os.chdir("/Users/adityaagarwal/Library/CloudStorage/OneDrive-NortheasternUniversity/Data-Science-datasets/")
    
df = pd.read_csv("./Clean_data")
df.head(3)
    
# Creating a small subset of the data
df = df[["Alley","LotShape","GarageCond","MasVnrArea","SalePrice"]]
df.head(5)

################################################
## ONE HOT ENCODING USING PANDAS (GET DUMMIES)
################################################
def dummy_encoding(data):
    dummy = pd.get_dummies(data, drop_first=True)
    print("The columns are ", dummy.columns)
    
    # converting to 0/1
    dummy = dummy.astype(int)
    # replacing T/F to 0/1
    dummy = dummy.replace({'True': '1', "False": '0'})
    print(dummy.info())
    return dummy

dummy_data = dummy_encoding(df)

################################################
## ONE HOT ENCODING USNIG SCIKIT-LEARN
################################################
def one_hot_encoding(data):
    from sklearn.preprocessing import OneHotEncoder
    
    encoder = OneHotEncoder(categories = 'auto', drop = 'first', sparse = False, handle_unknown="error")
    # Fit
    encoder.fit(data)
    # Transform
    variables = encoder.transform(data)
    print("The categorical features are:", encoder.categories_)
    final_data = pd.DataFrame(variables, columns = encoder.get_feature_names_out(data.columns))
    
    return final_data
    
df_cat_values = df.drop(["MasVnrArea","SalePrice"],axis=1)
one_hot_data = one_hot_encoding(df_cat_values)



def value_counts(data):
    cat_list = data.select_dtypes(include='object').columns.tolist()
    print("The categorical columns are:", cat_list)
    
    for i in cat_list:
        print(df[i].value_counts(),'\n')
        
value_counts(df)
    


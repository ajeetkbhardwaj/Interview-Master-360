""" 

@Reference :
1. Dataset : https://www.kaggle.com/datasets/yogeerp/mercedes
2. Exploratory Analyssi : https://www.kaggle.com/code/kerneler/starter-mercedes-cfabb923-8
3. Feature Engineering :



"""
#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

#%% 1. 
data1 = pd.read_csv('data/mercedesbenz.csv',
                    sep=',')
df1 = data1
df1.dataframeName = 'mercedesbenz dataset'
(nrow, ncol) = df1.shape
print(f"shape of dataset : ({nrow}, {ncol})")
print(df1.head(10))




# %%

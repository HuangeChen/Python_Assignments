
# coding: utf-8

# Q1_Part Two
# Use ‘vehicle_collisions’ data set.
# For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# Display a few rows of the output use df.head().
# Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')
# 

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[2]:

df=pd.read_csv('/Users/huangechen/Desktop/Python Class/Assignment 3/Data/vehicle_collisions.csv')


# In[3]:

df.head()


# In[4]:

print(list(df))


# In[5]:

new_df=df[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE',]]
new_df.head()


# In[6]:

df.BOROUGH.unique()


# In[7]:

new_df.groupby('BOROUGH').count()


# In[8]:

new_df.groupby('BOROUGH').count().to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q1_part2.csv")


# In[ ]:




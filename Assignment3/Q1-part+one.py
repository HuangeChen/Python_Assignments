
# coding: utf-8

# Q1_Part one
# Use ‘vehicle_collisions’ data set.
# For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# Display a few rows of the output use df.head().
# Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# Step1, Get the sources I need, which are date and borough
# Step2, change date to date-format, and narrow data by month
# Step3, Since there are Nan in BOROUGH, so the total of date is the total vehicle_collisions in NYC
# Step4, get total vehicle_collisions in Manhattan
# Step5, combine NYC & Manhattan, get Percentage

# 

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import datetime


# In[2]:

df=pd.read_csv('/Users/huangechen/Desktop/Python Class/Assignment 3/Data/vehicle_collisions.csv')


# # Step1

# In[3]:

new_df=df[['DATE','BOROUGH']]
new_df.head(5)


# In[4]:

df['DATE']=pd.to_datetime(df['DATE'])


# In[5]:

#df2=new_df[pd.to_datetime(new_df['DATE']).dt.year==2016].reset_index()


# In[6]:

type(df['DATE'][0])


# In[7]:

df['MONTH']=df['DATE'].dt.strftime("%b")


# In[8]:

df.head()


# In[9]:

new_df=df[['DATE','BOROUGH','MONTH']]
new_df.head(5)


# # Step 2

# In[10]:

df2=df['DATE']


# In[11]:

df3=new_df[pd.to_datetime(df2).dt.year==2016]


# In[12]:

df3.head()


# In[13]:

df3.groupby('MONTH',sort=False).count()


# In[14]:

new_df3=df3.drop('BOROUGH', 1)


# # Step3

# In[15]:

new_df3.rename(columns={'DATE': 'NYC'}, inplace=True) 


# In[16]:

new_df3.groupby('MONTH',sort=False).count()


# In[17]:

#new_df3=df3.drop('BOROUGH', 1)


# In[18]:

#new_df3.head()


# # Step4

# In[19]:

df4=df3[df3['BOROUGH']=='MANHATTAN']


# In[20]:

df4.head()


# In[21]:

df4.groupby('MONTH',sort=False).count()


# In[28]:

df4.rename(columns={'BOROUGH': 'MANHATTAN'}, inplace=True) 


# In[29]:

new_df4=df4.drop('DATE',1)


# In[30]:

new_df4.head()


# In[31]:

new_df4.groupby('MONTH',sort=False).count()


# # Step5

# In[32]:

df5=new_df4.groupby('MONTH',sort=False).count().join(new_df3.groupby('MONTH',sort=False).count())


# In[33]:

df5


# In[34]:

df5['PERCENTAGE']=df5['MANHATTAN']/df5['NYC']


# In[35]:

df5


# In[36]:

df5.to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q1_part1.csv")


# In[ ]:




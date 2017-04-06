
# coding: utf-8

# Q4_part one
# Use ‘movies_awards’ data set.
# You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# Create two separate columns for each award category (won and nominated).
# Write your output to a csv file. (Sample output is given in next page)
# 

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[2]:

df=pd.read_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Data/movies_awards.csv")


# In[3]:

df.head()


# In[4]:

print(list(df))


# In[5]:

new_df=df[['Awards']]


# In[6]:

new_df.head()


# In[7]:

df_Awards=new_df.dropna().groupby('Awards').count()


# In[8]:

df_Awards.head()


# In[9]:

df[['Awards']]
df['Awards_won']=df['Awards'].str.extract('(\d+) win',expand=True).fillna(0)
df['Awards_nominated']=df['Awards'].str.extract('(\d+) nomination',expand=True).fillna(0)
df['Oscar_Awards_won']=df['Awards'].str.extract('won for (\d+) Oscars.',expand=True).fillna(0)
df['Oscar_Awards_nominated']=df['Awards'].str.extract('Nominated for (\d+) Oscars.',expand=True).fillna(0)
df['Golden Globes_Awards_won']=df['Awards'].str.extract('won for (\d+) Golden Globes',expand=True).fillna(0)


# In[10]:

final_df=df[['Awards']].join(df['Awards_won']).join(df['Awards_nominated']).join(df['Oscar_Awards_won']).join(df['Oscar_Awards_nominated']).join(df['Golden Globes_Awards_won'])


# In[11]:

final_df.dropna().head()


# In[12]:

final_df.dropna().to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q4.csv")


# In[ ]:




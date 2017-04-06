
# coding: utf-8

# Q2_PART ONE
# Use 'employee_compensation' data set.
# Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# Display a few rows of the output use df.head().
# 

# Step1, get unique Organization Groups which are 7 groups
# Step2, get the highest conpensation department of each Organization
# Step3, create DataFrame

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# # Step1

# In[2]:

df=pd.read_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Data/employee_compensation.csv")


# In[3]:

df.head()


# In[4]:

print(list(df))


# In[5]:

new_df=df[['Organization Group','Department','Total Compensation']]


# In[6]:

new_df.head()


# In[7]:

df['Organization Group'].unique()


# # Step2

# In[8]:

df1=new_df[new_df['Organization Group']=='Public Works, Transportation & Commerce']


# In[9]:

df1.sort(['Total Compensation'],ascending=False).head()


# In[10]:

df2=new_df[new_df['Organization Group']=='Community Health']


# In[11]:

df2.sort(['Total Compensation'],ascending=False).head()


# In[12]:

df3=new_df[new_df['Organization Group']=='Human Welfare & Neighborhood Development']


# In[13]:

df3.sort(['Total Compensation'],ascending=False).head()


# In[14]:

df4=new_df[new_df['Organization Group']=='General Administration & Finance']


# In[15]:

df4.sort(['Total Compensation'],ascending=False).head()


# In[16]:

df5=new_df[new_df['Organization Group']=='Culture & Recreation']


# In[17]:

df5.sort(['Total Compensation'],ascending=False).head()


# In[18]:

df6=new_df[new_df['Organization Group']=='Public Protection']


# In[19]:

df6.sort(['Total Compensation'],ascending=False).head()


# In[20]:

df7=new_df[new_df['Organization Group']=='General City Responsibilities']


# In[21]:

df7.sort(['Total Compensation'],ascending=False).head()


# # Step3

# In[22]:

Data={'Organization Group':['Public Works, Transportation & Commerce', 'Community Health',
       'Human Welfare & Neighborhood Development',
       'General Administration & Finance', 'Culture & Recreation',
       'Public Protection', 'General City Responsibilities'],
      'Department':['PUC Public Utilities Commission','Public Health','Human Services','Retirement System','Public Library',
                    'Police','General Fund Unallocated'],
      'Total Compensation':[445131.82,439541.54,394548.44,676156.26,336211.56,510574.44,137930.88]}


# In[23]:

frame=DataFrame(Data,columns=['Organization Group','Department','Total Compensation'])


# In[24]:

frame


# In[25]:

frame.to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q2_Part1.csv")


# In[ ]:




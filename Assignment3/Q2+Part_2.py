
# coding: utf-8

# Q2_Part Two
# Use 'employee_compensation' data set.
# Find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# For each job family these people are associated with (job family refers to ’Job Family' column), calculate what is the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column (Percent_total_benefit) which has the percentage value.
# Display the top 5 job families according to Percent_total_benefit using df.head().
# Write the output (jobs and Percent_total_benefit) to a csv.

# #step1, get useful sources,add a new column which is 5% of Salaries and get the differences of Overtime and 5% of Salaries 
# #step2,get people whose overtime salary is greater than 5% of salaries 
# #step3, create dataframe
# #step4, sort pecent_total_benefit from high to low

# # Step1

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[2]:

df=pd.read_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Data/employee_compensation.csv")


# In[3]:

df.head()


# In[4]:

print(list(df))


# In[5]:

new_df=df[['Salaries','Overtime']]


# In[6]:

new_df.head()


# # Step2

# In[7]:

new_df['New_Column']=new_df['Salaries'].apply(lambda x: x*0.05)


# In[8]:

new_df.head() #New_Colunm is 5% of Salaries


# In[9]:

data=new_df['Overtime']-new_df['New_Column'] # get the differences of Overtime and 5% of Salaries


# In[10]:

data.head()


# In[11]:

df1=DataFrame(data)


# In[12]:

df1.head()


# In[13]:

df2=new_df.join(df1)


# In[14]:

df2.head()


# In[15]:

df2[df2[0]>0].head()  #people whose overtime salary is greater than 5% of salaries 


# # Step3

# In[16]:

df3=df[['Job Family','Total Benefits','Total Compensation']]


# In[17]:

df3.head()


# In[18]:

df3['Percent_Total_Benefits']=df3['Total Benefits']/df3['Total Compensation']


# In[19]:

df3.head()


# # Step4

# In[22]:

df3.sort(['Percent_Total_Benefits'],ascending=False).head()


# In[24]:

df3.sort(['Percent_Total_Benefits'],ascending=False).head().to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q2_Part2.csv")


# In[ ]:




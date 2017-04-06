
# coding: utf-8

# Q3_PART ONE
# Use ‘cricket_matches’ data set.
# In this analysis, you are supposed to calculate the average score for each team which host the game and win the game.
# Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. 
# You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# Display a few rows of the output use df.head()
# 

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[2]:

df=pd.read_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Data/cricket_matches.csv")


# In[3]:

df.head()


# In[4]:

print(list(df))


# In[5]:

new_df=df[['match_details','scores','home','winner','innings1','innings1_runs','innings2','innings2_runs']]
new_df.head()


# In[6]:

df1=new_df[['home','innings1_runs','innings2_runs']]


# In[7]:

df1.head()


# In[8]:

df1['innings1_runs']-df1['innings2_runs']>0


# In[12]:

new_df1_win1=df1[df1['innings1_runs']-df1['innings2_runs']>0]


# In[14]:

new_df_win1=new_df1_win1.drop('innings2_runs',1).head()


# In[15]:

new_df_win1


# In[16]:

new_df_win1.rename(columns={'innings1_runs':'score'})


# In[17]:

df_win2=df1[df1['innings1_runs']-df1['innings2_runs']<0]


# In[18]:

new_df_win2=df_win2.drop('innings1_runs',1)


# In[19]:

#new_df_win2


# In[20]:

new_df_win2.rename(columns={'innings2_runs':'score'}).head()


# In[21]:

final_df=pd.concat([new_df_win1.rename(columns={'innings1_runs':'score'}),
           new_df_win2.rename(columns={'innings2_runs':'score'})])


# In[22]:

final_df.sort('score',ascending=False).head()


# In[24]:

final_df.sort('score',ascending=False).to_csv("/Users/huangechen/Desktop/Python Class/Assignment 3/Q3.csv")


# In[ ]:




# In[ ]:




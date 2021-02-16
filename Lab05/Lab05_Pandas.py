#!/usr/bin/env python
# coding: utf-8

# # Lab05 Python Data Science with Pandas

# In[46]:


# magic command to display matplotlib plots inline within the ipython notebook webpage
get_ipython().run_line_magic('matplotlib', 'inline')

# import necessary modules
import pandas as pd, numpy as np, matplotlib.pyplot as plt


# ## Part 1 <br /> Basics of Selecting and Slicing Data

# In[3]:


# create a pandas dataframe from the location data set
df = pd.read_csv('data/summer-travel-gps-full.csv')
df.head()


# In[94]:


# Q1: how to get 2 columns from the dataframe (city and country)?
q1=df[['city','country']]
q1


# To get a single "cell's" value out of a dataframe, pass a column name, then a row label. This is equivalent to slicing the dataframe down to a single series, then slicing a single value out of that series using [ ] indexing.

# In[97]:


# Q2: how to get the first 5 rows of the "city" column?
df.city.head(5)


# ### Using .loc[ ]

# In[98]:


# Q3: how to use .loc to select the third row of the dataframe?
df.loc[3]


# In[99]:


# Q4: how to use .loc to select the first row in "country" column?
df.country[1]


# In[100]:


# Q5: how to select the first 4 rows of ['city', 'date'] columns?
df[["city","date"]].head(4)


# ### Using .iloc[ ]

# In[101]:


# use .iloc for integer position based indexing
# Q6: how to get the value from the row in position 3 and the column in position 2
df.iloc[3,2]


# In[130]:


# Q7: how to use iloc to select every 300th row from a data set
import math
q7=pd.DataFrame()
dl=math.floor(len(df)/300)
for i in range(dl):
    q7t=df.iloc[300+300*i]
    q7=pd.concat([q7,q7t],axis=1)
q7.T


# ## Part 2 <br /> How to select rows by some value(s)

# In[58]:


# load a reduced set of gps data
df = pd.read_csv('data/summer-travel-gps-simplified.csv')
df.tail()


# In[141]:


# Q9: create a Series of true/false, indicating if each "city" row in the column is equal to "Munich"
for i in range(len(df)):
    q9=(df.city=="Munich")
q9


# In[145]:


# pandas logical operators are: | for or, & for and, ~ for not
# these must be grouped by using parentheses
# Q10: what cities were visited in spain that were not barcelona? Create a dataframe for it. 
df[(df.city!="Barcelona")&(df.country=="Spain")]


# In[146]:


# Q11: select rows where either the city is munich, or the country is serbia
df[(df.city=="Munich")|(df.country=="Serbia")]


# In[148]:


# Q12: how many observations are west of the prime meridian?
df[df.lon<0]


# In[184]:


# Q13: get all rows that contain a city that starts with the letter G
q13=pd.DataFrame()
dl=len(df)
for i in range(dl):
    if df.city[i].startswith("G"):
        q13t=df.loc[i]
        q13=pd.concat([q13,q13t],axis=1)
q13.T


# In[194]:


# Q14: how many unique cities and countries in the dataset? 
# Also can you check missing values for the dataframe
print("There are",len(df.drop_duplicates(subset=['city','country'])),"unique cities and countries in the dataset.")
df.isnull()
df.isnull().sum().sum()


# In[223]:


# Q15: group by country name and show the city names in each of the country
for name,group in df.groupby(['country','city']):
    print(name)


# ## Part 3 <br /> How to select based on a date-time values

# In[224]:


# load the location data set, indexed by the date field
# and, parse the dates so they're no longer strings but now rather Python datetime objects
# this lets us do date and time based operations on the data set
dt = pd.read_csv('data/summer-travel-gps-full.csv', index_col='date', parse_dates=True)
dt.head()


# In[275]:


# Q16: is the timestamp index unique? How can you use code to find it? 
if len(dt._stat_axis)==len(dt._stat_axis.drop_duplicates()):
    print("The timestamp index is unique.")
else:
        print("It is not unique.")


# In[293]:


# Q17: drop duplicate
dt[~(dt.index.duplicated())]


# In[337]:


# Q18: create a weekday and a weekend dataframe
from datetime import date
wd=pd.DataFrame()
wk=pd.DataFrame()
for i in range(len(dt)):
    if (dt.index[i].weekday()+1)<6:
        wdt=dt.iloc[i]
        wd=pd.concat([wd,wdt],axis=1)

for i in range(len(dt)):
    if (dt.index[i].weekday()+1)>5:
        wkt=dt.iloc[i]
        wk=pd.concat([wk,wkt],axis=1)

wd.T


# In[338]:


wk.T


# In[362]:


# Q19: calculate and plot the number of observations each day of the week has
m=[]
for i in range(7):
    k=0
    for j in range(len(dt)):
        if dt.index[j].weekday()==i:
            k=k+1
    m.append(k)

import matplotlib.pyplot as plt
import numpy as np
 
plt.bar(x=['1','2','3','4','5','6','7'],height=m, color='grey', alpha=0.8)


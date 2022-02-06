#!/usr/bin/env python
# coding: utf-8

# In[1]:



import csv
import numpy as np
from itertools import islice
data_origin=open("C:/Users/viran/Documents/PTUA2022/Lab04/lab/Lab04-1.gal")
data=[]
for line in islice(data_origin, 1, None):
    data.append(line.replace("\n","").split(" "))
data


# In[2]:


data01=data[::2]
data02=data[1::2]


# In[3]:


dict01={}
for i,val in enumerate(data02,start=1):
    dict01[i] = val
dict01


# In[4]:


for key in dict01:
    print(key, dict01[key])
    for neighbor in dict01[key]:
        print(key,' says ',neighbor, 'is a neighbor')
if key in dict01[neighbor]:
            print('ok')
else:
            print('not ok')
            print('because ', neighbor, ' says that ', key, 'is not a neighbor')
  




dict002= {}
for i, val in enumerate(data01,start=1):
        dict002[int(i)] = int(val[1]) 
        
dict002

dict02={}
for i,val in dict002.items():
    if val not in dict02.keys():
        dict02[val]=[i]
    else:
        dict02[val].append(i)
dict02


# In[24]:


import matplotlib.pyplot as plt
plt.hist(dict01,dict02[val])
plt.show()






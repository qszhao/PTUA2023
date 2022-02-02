#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

from itertools import islice
lab = open("/Users/emilyxu/Lab04/Lab04-1.gal")
text = []
for line in islice(lab, 1, None):
    text.append(line)
print(text)


# In[2]:


li = []
for i in text:
    i = i.replace("\n","").split(" ")
    li.append(i)
li


# In[3]:


df1 = {}


# In[28]:


for id, val in enumerate(li):
    if id % 2 == 1:
        value = val
        df1[key] = value
    else:
        key = val[0]


# In[29]:


df1


# In[6]:


df1["35"]


# In[20]:


temp = {}
for id, val in enumerate(li):
    if id % 2 == 0:
        temp[int((id+2)/2)] = int(val[1])
temp


# In[21]:


df2df2 = {}
for key,value in temp.items():
    if value not in df2.keys():
        df2[value] = [key]
    else:
        df2[value].append(key)
df2


# In[19]:


for key in df1:
    print(key, df1[key])
    for neighbor in df1[key]:
        print(key,' says ',neighbor, 'is a neighbor')
        if key in df1[neighbor]:
            print('ok')
        else:
            print('not ok')
            print('because ', neighbor, ' says that ', key, 'is not a neighbor')


# In[ ]:





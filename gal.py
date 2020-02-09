#!/usr/bin/env python
# coding: utf-8

# In[2]:


# read gal file
import pandas as pd
import os
os.chdir("D:\\Urban_Analytics\\UA\\PTUA2020-master\\Lab04")

data = []
with open ('Lab04-1.gal','r') as f:
    for line in f:
        data.append(list(line.strip('\n').split(' ')))
    #print(data)


# In[3]:


# return the key and id of neighbors:

def SpatialUnit (x):
    dic = {}
    n = 1
    for n in range(len(x)-1):
        if n < len(x):
            key = int(x[n][0])
            value = [int(i) for i in x[n + 1]]
            dic.update({key : value})
            n = n + 2
    return(dic)

gal = SpatialUnit(data)
print(gal)


# In[123]:


# return a second dictionary that has the histogram for the neighbor cardinalities

def neighbor(x):
    dic_count = []
    dic_new = {}
    values = list(x.values())
    keys = list(x.keys())
    for i in range(len(values)):
        count = len(values[i])
        dic_count.append([keys[i],count])
    for i, val in dic_count:
        if val not in dic_new:
            dic_new[val] = []
        dic_new[val].append(i)      
    return(dic_new)

test2 = neighbor(gal)
print(test2)    
    


# In[11]:


# test if there are any asymmetries. An asymmetry occurs when i says j is a neighbor of i, but j does not say i is a neighbor of j.
asy = {}
for key in gal:
    print (key, gal[key])
    for neighbor in gal[key]:
        print (key, 'says', neighbor, 'is a neighbor')
        if key in gal[neighbor]:
            print ('OK')          
        else:
            print(key)
            print('not, because ', neighbor, ' says that ', key, 'is not a neighbor')
            if key not in asy:
                asy[key] = []
            asy[key].append(neighbor)
print(asy)


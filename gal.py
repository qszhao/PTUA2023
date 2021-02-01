#!/usr/bin/env python
# coding: utf-8

# Open gal file with list

# In[14]:


gallist = []
with open ('F:\\PTUA2021-master\\Lab04\\Lab04-1.gal','r') as f:
    for line in f:
        gallist.append(list(line.strip('\n').split(' ')))
print(gallist)


# Define a dictionary that the key is the id of a spatial unit and the value is a list of the ids of its neighbors.

# In[18]:


def galdict(l):
    galdict ={} 
    i = 1
    for i in range(len(l)-1):
        if i < len(l):
            key = int(l[i][0])
            value = [int(i) for i in l[i + 1]]
            galdict.update({key : value})
            i = i + 2
    return(galdict)
print(galdict(gallist))


# Define the second dictionary that the key is the number of neighbors and the value is the list of ids that have key neighbors.

# In[28]:


def nbdict(x):
    sec_dict = {}
    num = []
    sec_value = list(x.values())
    sec_key = list(x.keys())
    for i in range(len(sec_value)):
        numbers = len(sec_value[i])
        num.append([sec_key[i],numbers])
    for i,val in num:
        if val not in sec_dict:
            sec_dict[val] = []
        sec_dict[val].append(i)
    
    return(sec_dict)

print(nbdict(galdict(gallist)))


# Test if there are any asymmetries.

# In[33]:


w = galdict(gallist)
for key in w:
    print(key, w[key])
    for neighbor in w[key]:
        print(key,' says ',neighbor, 'is a neighbor')
        if key in w[neighbor]:
            print('ok')
        else:
            print('not ok')
            print('because ', neighbor, ' says that ', key, 'is not a neighbor')


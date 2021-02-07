#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gal(gal_file):
    # read gal file
    f = open(gal_file, "r")
    lines = f.readlines()
    
    # Return a Python dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors
    line0 = lines[0]
    line0 = line0.strip().split()
    n_neighbors = int(line0[1])
    neighbors = {}
    lines = lines[1:]
    i = 0
    while i < n_neighbors * 2:
        header = lines[i].strip().split()
        info = lines[i+1].strip().split()
        key = header[0]
        neighbors[key] = info
        i += 2
    return(neighbors)
    
def hist(gal_file):
    #Take a gal dictionary from 1 and return a second dictionary that has the histogram for the neighbor cardinalities.
    neighbors = gal(gal_file)
    h = {}
    num = [1]
    for node in neighbors:
        num.append(len(neighbors[node]))
    for i, val in enumerate (num):
        if val not in h:
            h[val] = []
        h[val].append(i)
    del h[1]
    return(h)
        
def asymm(gal_file):
    # Take a gal dictionary from 1 and test if there are any asymmetries. 
    neighbors = gal(gal_file)
    for key in neighbors:
        print (key, neighbors[key])
        for neighbor in neighbors[key]:
            if key not in neighbors[neighbor]:
                print ('There is an asymmetry,''because ', neighbor, ' says that ', key, 'is not a neighbor')

    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv

from itertools import islice
lab = open("/Users/emilyxu/Lab04/Lab04-1.gal")
text = []
for line in islice(lab, 1, None):
    text.append(line)
print(text)


# In[6]:


li = []
for i in text:
    i = i.replace("\n","").split(" ")
    li.append(i)


# In[7]:


df3 = {}
for id, val in enumerate(li):
    if id % 2 == 1:
        value = val
        df3[int(key)] = list(map(int,value))
    else:
        key = val[0]


# In[8]:


df3


# In[10]:


class Vertex(object):
    def __init__(self, key):
        self.id = key 
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, weight=0):
            self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0 
        
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices = self.numVertices + 1 
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n] 
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f) 
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph() 
for i in range(6): 
    g.addVertex(i)
print(g.vertList)



for key, values in df3.items():
    for value in values:
        g.addEdge(key, value)

for v in g: 
    for w in v.getConnections():
        print("(%s, %s)" % (v.getId(), w.getId())) 


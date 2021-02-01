#!/usr/bin/env python
# coding: utf-8

# In[86]:


class Graph:
    """My class for Lab04"""
    def __init__(self, gal_file):

        # get file name
        self.gal_file = gal_file


        # open and read gal file
        fp = open('F:\\PTUA2021-master\\Lab04\\Lab04-1.gal')
        lines = fp.readlines()
        fp.close()
        self.lines = lines

        # build the dictionary
        line0 = lines[0]
        line0 = line0.strip().split()
        self.line0 = line0
        self.n_polygons = int(line0[1])
        neighbors = {}
        lines = lines[1:]
        processing = True 
        i = 0
        while i < self.n_polygons * 2:
            header = lines[i].strip().split()
            i_neighbors = lines[i+1].strip().split()
            node_i = header[0]
            neighbors[node_i] = i_neighbors
            i += 2
        self.neighbors = neighbors


        # answer questions under 2

    def summary(self):
        n_neighbors = 0
        maxc = 0
        L_max = []
        L_min = []
        for node in self.neighbors:
            n_neighbors += len(self.neighbors[node])
            n_node = len(self.neighbors[node])
            if n_node > maxc:
                maxc = n_node
                L_max.append(node)
            if n_node > 1:
                L_min.append(node)
            if n_node != 0:
                disc = 'there are no islands'
                
            


        average = n_neighbors * 1. / self.n_polygons
        results = {}
        results['average'] = average
        results['max connectivity'] = maxc, L_max
        results['min connectivity'] = L_min
        results['disconnected nodes'] = disc
        return results


if __name__ == '__main__':

    my_gal = Graph('F:\\PTUA2021-master\\Lab04\\Lab04-1.gal')
    print(my_gal.summary())


# In[ ]:





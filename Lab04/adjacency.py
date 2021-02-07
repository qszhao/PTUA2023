#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    def __init__(self, gal_file):
        # get file name
        self.gal_file = gal_file
        # read gal file
        f = open(gal_file, "r")
        lines = f.readlines()

        # Return a Python dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors
        line0 = lines[0]
        line0 = line0.strip().split()
        n_polygons = int(line0[1])
        neighbors = {}
        lines = lines[1:]
        self.n_polygons = n_polygons
        i = 0
        while i < n_polygons * 2:
            header = lines[i].strip().split()
            info = lines[i+1].strip().split()
            key = header[0]
            neighbors[key] = info
            i += 2
        self.neighbors = neighbors
    
    def summary(self):
        n_neighbors = 0
        mc = 0
        for node in self.neighbors:
            n_neighbors += len(self.neighbors[node])
            n_node = len(self.neighbors[node])
            if n_node > mc:
                mc = n_node
        mi = mc
        for node in self.neighbors:
            n_node = len(self.neighbors[node])
            if n_node < mi:
                mi = n_node
            if n_node < 1:
                dis = ("Disconnected nodes are", node)
            else:
                dis = "There are no islands."
        average = n_neighbors / self.n_polygons
        results = {}
        results['average'] = average
        results['max card'] = mc
        results['min card'] = mi
        results['Disconnected'] = dis
        return results

                    
if __name__ == '__main__':

    my_gal = Graph("Lab04-1.gal")
    


# In[ ]:





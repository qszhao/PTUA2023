class GAL:
    """My class for Lab04-1"""
    def dictionary1(gal_file):

        # open and read gal file
        fp = open(gal_file)
        lines = fp.readlines()

        # Return a Python dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors.
        line0 = lines[0]
        line0 = line0.strip().split()
        n_neighbors = int(line0[1])
        neighbors = {}
        lines = lines[1:]
        processing = True 
        i = 0
        while i < n_neighbors * 2:
            header = lines[i].strip().split()
            i_neighbors = lines[i+1].strip().split()
            node_i = header[0]
            neighbors[node_i] = i_neighbors
            i += 2
        return neighbors
    
    def dictionary2(gal_file):
        
        # Take a gal dictionary from 1 and return a second dictionary that has the histogram for the neighbor cardinalities.
        neighbors = dictionary1(gal_file)
        num = []
        for i in neighbors:
            number = len(neighbors[i])
            num.append(number)
        h = {}
        for i,val in enumerate(num):
            if val not in h:
                h[val] = []
            h[val].append(i)
            return h
    
    def asymmetries(gal_file):
        
        # Take a gal dictionary from 1 and test if there are any asymmetries.
        neighbors = dictionary1(gal_file)
        for key in neighbors:
            print(key, neighbors[key])
            for neighbor in neighbors[key]:
                print (key,' says ',neighbor, 'is a neighbor')
                if key in neighbors[neighbor]:
                    print('ok')
                else:
                    print ('not ok')
                    print ('because ', neighbor, ' says that ', key, 'is not a neighbor')

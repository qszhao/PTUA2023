def gal_dic(path):
    """ Return a Python dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors.
    
    path: string
    
    Returns: dictionary
    """
    f = open(path)
    num_str = f.readline()                      
    num = list(num_str.split())     # convert the first string line to list

    gal = {}                        
    for i in range(0, int(num[1])):    
    
        unit_str = f.readline()
        unit = []                   # read the key 
        unit.extend([int(number) for number in unit_str.split()])        
    
        neighbor_str = f.readline()      
        neighbor = []               # read the values of the key
        neighbor.extend([int(number) for number in neighbor_str.split()])
        
        gal.update({unit[0]:neighbor})
    return gal


def histogram_dic(gal):
    """ return a second dictionary that has the histogram for the neighbor cardinalities.
    
    gal: dictionary
    
    Returns: dictionary
    """
    number = []
    for i in gal:
        number.append(len(gal[i]))  # list of the number of neighbors

    histogram = {}
    for i,key in enumerate(number): # key: the number of neighbors
                                    # i: the id of a unit
        if key not in histogram :
            histogram[key] = []
        histogram[key].append(i+1)
    return histogram


def asymmetries(gal):
    """ test if there are any asymmetries.
    
    gal: dictionary
    """
    flag = True
    for key in gal:
        for neighbor in gal[key] :
            if key not in gal[neighbor]:
                print('There are asymmetries.')
                print('Because', key,'says',neighbor, 'is a neighbor,','but', neighbor, 'says that', key, 'is not a neighbor.')
                flag = False
                break
    if flag == True:
        print('There is no asymmetry.')
   

# test        
path = "Lab04-1.gal"
gal_dic1 = gal_dic(path)
print('GAL DICTIONARY is\n', gal_dic1)
histogram_dic1 = histogram_dic(gal_dic1)
print('HISTOGRAM DICTIONARY is\n', histogram_dic1)
asymmetries(gal_dic1)
import statistics 
class Graph(object):
    """ Class that allow for the representation of adjacency relations between spatial polygons borrowing concepts from graph theory.
    
    attributes: Node(dictionary)
    
    methods: average_con(),Maximum_con(),Minimum_con(),dis_con().
    """
    def __init__(self,path):
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
        self.Node = gal
        
    def average_con(self):
        number = []
        for i in self.Node:
            number.append(len(self.Node[i]))
        print("Average connectivity:",int(statistics.mean(number)))
    
    def Maximum_con(self):
        maxcon = 0
        nodes = []
        for i in self.Node:
            if maxcon < len(self.Node[i]):
                maxcon = len(self.Node[i])
                nodes = self.Node[i]
        print("Maximum connectivity:",maxcon)
        print("Nodes:",nodes)
        
    def Minimum_con(self):
        mincon = len(self.Node)
        nodes = []
        for i in self.Node:
            if mincon > len(self.Node[i]):
                mincon = len(self.Node[i])
                nodes = self.Node[i]
        print("Minimum connectivity:",mincon)
        print("Nodes:",nodes) 
        
    def dis_con(self):
        nodes = []
        for i in self.Node:
            if len(self.Node[i]) == 0:
                nodes = self.Node[i]
        if len(nodes) == 0:
            print("There are no islands.")
        else:
            print("Disconnected nodes:",nodes)

if __name__ == '__main__':
    test = Graph("Lab04-1.gal")
    print("Nodes:",test.Node)
    test.average_con()
    test.Maximum_con()
    test.Minimum_con()
    test.dis_con()
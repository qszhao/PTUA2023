
f = open("Lab04-1.gal", "r")

flines = f.readlines()
flines = flines[1: ] 

linelist = [] 
for x in flines:
  line = x[ :-1].split(' ')
  linelist.append(line)


list1=[]
for i, li in enumerate(linelist):
    if i%2 == 0:
        list1.append(li)


d = {}
for i,li in enumerate(list1):
    id1 = int(li[0])
    value = int(li[1]) 
    d[id1] = value


class Graph:
    
    def __init__(self, dic):
        self.nodes = list(dic.keys())
        self.values = list(dic.values())
    
    def ave_con(self):
        sum = 0
        for value in self.values:
            valuelist = value  
            edge = valuelist[0] 
            sum += edge
        return sum / self.nodes[-1]
    
    def max_con(self): 
        maxdic = {}
        for i,value in enumerate(self.values,1):
            node = i
            connectivity = value
            if value == max(self.values) and i not in maxdic:
                maxdic[node]=connectivity
        for key in maxdic:
            print("Node {} has max connectivity of {}".format(key, maxdic[key]))
                
    def min_con(self):
        mindic = {}
        for i,value in enumerate(self.values,1):
            node = i
            connectivity = value
            if value == min(self.values) and i not in mindic:
                mindic[node]=connectivity
        for key in mindic:
            print("Node {} has min connectivity of {}".format(key, mindic[key]))
    
    def dis_con(self):
        dislist = []
        for i,value in enumerate(self.values,1):
            node = i
            connectivity = value
            if value == 0 and i not in dislist:
                dislist.append(node)
        if dislist == []:
            print("There are no islands")
        else:
            print(dislist)
        
        


graph1 = Graph(d)


print(graph1.nodes[0])


graph1.ave_con()


graph1.max_con()


graph1.min_con()


graph1.dis_con()


get_ipython().system('jupyter nbconvert --to script []')
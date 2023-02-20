#!/usr/bin/env python
# coding: utf-8

# In[26]:



with open('G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal', mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # 读取文件
    try:
        lines = lines[1:] # 只读取第一行之后的内容
        f.close()             # 关闭文件
    except:
        pass

node = {}
i=1
for line in lines:
    
    #line1
    if i%2 == 1:      
        list1 = line[:-1].split(' ')
        key = list1[0]
        num = int(list1[1])
        i = i+1
    #line2
    elif i%2 == 0:
        list2 = line[:-1].split(' ')
        node[key] = list2
        i = i+1
print(node)

#The code above is to get the dictionary of node.

class Graph(object):
    def __init__(self,n):
        self.n = n
        
    def ave_connect(self):
        total_connect = 0
        i = 0
        for list in self.n.values():
            connect = len(list)
            total_connect = total_connect + connect
            i += 1
        ave_connect = total_connect/i
        return ave_connect
    
    def max_connect(self):
        max = 0
        i = 0
        x = 0
        for list in self.n.values():
            connect = len(list)
            i += 1
            if connect >= max:
                max = connect 
                max_key = i   #max_key represents the serial number of the key
            else:
                pass
        for key in self.n: #Print the corresponding key according to the serial number, I think there is another better way
            x += 1
            if x == max_key:
                KEY = key
            else:
                pass
        return max,KEY
    
    def min_connect(self):
        min = 1000
        i = 0
        x = 0
        for list in self.n.values():
            connect = len(list)
            i += 1
            if connect < min:
                min = connect 
                min_key = i   #min_key represents the serial number of the key
            else:
                pass
        for key in self.n: #Print the corresponding key according to the serial number, I think there is another better way
            x += 1
            if x == min_key:
                KEY = key
            else:
                pass
        return min,KEY
    
    def disconnect(self):
        x = 0
        for k in self.n:
            value_list = self.n[k]
            for value in value_list:
                list = self.n[value]
                if list.count(k) == 1:
                    continue
                else:
                    print('{} and {} have a problematic neighbourhood relationship, the dictionary has asymmetry'.format(k,value))
                    x = 1
        if x == 0:
            print('There are no asymmetries in that dictionary')

graph = Graph(node)

#1
Average_connectivity = graph.ave_connect()
print('The average connectivity is ',Average_connectivity)

#2
Maximum_connectivity = graph.max_connect()[0]
Maximum_object = graph.max_connect()[1]
print('The maximum connectivity is {} and the responding object number is {}'.format(Maximum_connectivity,Maximum_object))

#3
Minimum_connectivity = graph.min_connect()[0]
Minimum_object = graph.min_connect()[1]
print('The minimum connectivity is {} and the responding object number is {}'.format(Minimum_connectivity,Minimum_object))

#4
graph.disconnect()


# In[ ]:





class Graph:
    def __init__(self, path):
        data = []
        with open(path, 'r') as f:
            for line in f:
                data.append(line.strip('\n').split(' '))
        dictionary = {}
        num = 1
        while num < len(data):
            id = data[num][0]
            value = [val for val in data[num + 1]]
            dictionary.update({id: value})
            num = num + 2
        self.Node = dictionary
    def summary(self):
        num_neighbors = 0
        Max_con = 0
        Min_con = 1000000000
        dis_con=[]
        for node in self.Node:
            num_neighbors += len(self.Node[node])
            num_node = len(self.Node[node])
            if num_node > Max_con:
                Max_con = num_node
            if num_node < Min_con:
                Min_con=num_node
            if self.Node[node]==0:
                while i < len(self.Node[node]):
                    dis_con[i]=node
                    i=i+1
                    break
            else:
                dis_con='There are no islands'
        average_con = num_neighbors / len(self.Node)
        gal_summary = {}
        gal_summary['Average_connectivity'] = average_con
        gal_summary['Maximum_connectivity'] = Max_con
        gal_summary['Minimum_connectivity'] = Min_con
        gal_summary['Disconnected_nodes'] = dis_con
        return gal_summary

if __name__ == '__main__':

    my_gal = Graph("E:\PTUA\PTUA\Lab04\Lab\Lab04-1.gal")
    print(my_gal.Node)
    print(my_gal.summary())


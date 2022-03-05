class Graph():
    class Node():
        def __init__(self, path):
            self.path = path
            file = open(self.path,"r")
            gal = file.read()
            result_1 = {}
            gal = gal.splitlines()
            for i in range(1, len(gal), 2):
                id = gal[i].split(' ')[0]
                value = gal[i+1].split(' ')
                result_1[id] = []
                result_1[id] = value
            self.result = result_1
        
        def avg_connectivity(self):
            num = {}
            for i, value in self.result.items():
                num[i] = len(value)
            avg = sum(num.values()) / len(num)
            return avg
        
        def max_connectivity(self):
            num = {}
            for i, value in self.result.items():
                num[i] = len(value)
            maximum = max(num.values())
            key = []
            for i,value in num.items():
                if value == maximum:
                    key.append(i)
            return maximum, key
        
        def min_connectivity(self):
            num = {}
            for i, value in self.result.items():
                num[i] = len(value)
            df = []
            for value in num.values():
                if value > 0:
                    df.append(value)
            minimum = min(df)
            key = []
            for i,value in num.items():
                if value == minimum:
                    key.append(i)
            return minimum, key
        
        def disconnected_nodes(self):
            test = []
            for id in self.result:
                for value in self.result[id]:
                    if id in self.result[value]:
                        pass
                    else:
                        test.append([id,value])
            if test == []:
                return "There are no islands."
            else:
                return test


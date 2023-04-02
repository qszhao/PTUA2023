from statistics import mean

class adjacency:
    def __init__(self,dic1,dic2):
        self.dic1 = dic1
        self.dic2 = dic2

    def average_len(self):
        Average_connectivity = mean([len(v) for k, v in self.dic1.items()])
        return Average_connectivity


    def max_len(self):
        max_length = max([len(v) for k, v in self.dic1.items()])
        return max_length
    
    def max_key_value(self):
        max_length = max([len(v) for k, v in self.dic1.items()])
        max_list = {k:v for k, v in self.dic1.items() if len(v) == max_length}
        return max_list


    def min_len(self):
        min_length = min([len(v) for k, v in self.dic1.items()])
        return min_length

    def min_key_value(self):
        min_length = min([len(v) for k, v in self.dic1.items()])
        min_list = {k:v for k, v in self.dic1.items() if len(v) == min_length}
        return min_list

    def island(self):
        for i in self.dic2.keys():
            if i == 0:
                test = 0
                return("Specific node objects:", self.dic2[0])
                break
            else:
                test = 1

        if test == 1:
            return("There are no islands.")

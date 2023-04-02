class GalValue:
    def __init__(self, dic1):
        if type(dic1) != dict:
            raise TypeError("Input is not a dictionary.")
        self.dic1 = dic1
        self.dic2 = {}

    def ValueLen(self):
        self.dic2 = {}
        for i in self.dic1:
            key = len(self.dic1[i])
            if key not in self.dic2:
                self.dic2[key] = []
            self.dic2[key].append(i)

        return self.dic2

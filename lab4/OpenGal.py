class OpenGal:
    def __init__(self,name,dictionary):
        self.name = name
        self.dictionary = dictionary
        
    def open(self):
        listing = open(self.name, "r")
        listline = listing.readlines()
        count = len(open(self.name,'r').readlines())
        
        n = 1
        m = 1
        self.dictionary = {}
        while n < count:
            listline1 = listline[n].replace("\n", "").replace("\r", "")
            array = listline1.split(' ')
            if n % 2 != 0:
                self.dictionary[int(array[0])] = 0
            n += 1

        while m < count:
            listline2 = listline[m].replace("\n", "").replace("\r", "")
            array = listline2.split(' ')
            str1 = ','.join(array)
            result = list(map(int, str1.split(',')))
            if m%2 == 0:
                self.dictionary[m/2] = result
            m += 1
        return(self.dictionary)

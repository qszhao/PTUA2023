def readgal(path):
   data = []
   with open (path,'r') as f:
       for line in f:
           data.append(line.strip('\n').split(' '))
   return data
def spatial_Unit_dic(gal):
    dictionary={}
    num=1
    while num < len(gal):
        id=gal[num][0]
        #print(id)
        value=[val for val in data[num + 1]]
        #print(value)
        dictionary.update({id:value})
        num=num+2
    return dictionary
def dic_histogram(dic):
    neighbor_num=[]
    dictionary = {}
    for id in dic:
        neighbor_num.append(len(dic[id]))
    #print(neighbor_num)
    sm=set(neighbor_num)
    for val in sm:
        dictionary.update({val:neighbor_num.count(val)})
    return dictionary
def dic_asymmetries(dic):
    for key in dic:
        print(key, dic[key])
        for neighbor in dic[key]:
            print(key, ' says ', neighbor, 'is a neighbor')
            if key in dic[neighbor]:
                print('ok')
            else:
                print('not ok')
                print('because ', neighbor, ' says that ', key, 'is not a neighbor')
Path="E:\PTUA\PTUA\Lab04\Lab\Lab04-1.gal"
data=readgal(Path)
test1=spatial_Unit_dic(data)
print(test1)
test2=dic_histogram(test1)
print(test2)
test3=dic_asymmetries(test1)




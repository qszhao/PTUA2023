gal = open("C:/Users/Pluma/PTUA2021/Lab04/Lab04-1.gal")
gal_list = []
for line in gal:
    gal_list.append(line.split())
gal_list = gal_list[1:]
print(gal_list)

id_list = []
neighbors_list = []
for i, element in enumerate(gal_list):
    if i%2 == 0:
        id_list.append(element);
    else:
        neighbors_list.append(element)
print(id_list)
print(neighbors_list)

id_list_0 = []
for x in id_list:
    id_list_0.append(x[0])
print(id_list_0)

gal_dict = {}
i = 0
while i <= 48:
    gal_dict[id_list_0[i]] = neighbors_list[i]
    i += 1
print(gal_dict)
    
class gal_search():
    def __init__(self, gal_dict, gal_id = "1"):
        self.gal_dict = gal_dict
        self.gal_id = gal_id
        
    
    def function1(self, gal_id): 
#I still have a problem of the specified argument "gal_id", that although I put it in the specific function (e.g., test.function1) and specify it, the function will still use my original/default argument (i.e., gal_id = "1" even if I say gal_id = "5" in test.function1), so if I want to search for a new id I have to call the "test" function one more time. 
        search_dict01 = {}
        search_dict01[self.gal_id] = gal_dict[self.gal_id]
        print(search_dict01)
        
    def function2(self, gal_id):
        search_dict02 = {}
        neighbors_list = []
        for i in gal_dict[self.gal_id]:
            neighbors_list.append(i)
        number_of_neighbors = len(neighbors_list)
        search_dict02[number_of_neighbors] = gal_dict[self.gal_id]
        print(search_dict02)
    
    def function3(self):
        for i, element in self.gal_dict.items():
            for y in element:
                if i in self.gal_dict[y]:
                    continue
                else:
                    print(i, y)
                    print("there are asymmetries")
                    break

test = gal_search(gal_dict = gal_dict)
test.function1(gal_id = "5")
test.function2(gal_id = "5")
test.function3()




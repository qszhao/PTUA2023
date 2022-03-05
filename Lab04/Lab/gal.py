def transform_gal_1(path):
    result_1 = {}
    file = open(path,"r")
    gal = file.read()
    gal = gal.splitlines()
    for i in range(1, len(gal), 2):
        id = gal[i].split(' ')[0]
        value = gal[i+1].split(' ')
        result_1[id] = []
        result_1[id] = value
    return result_1


def transform_gal_2(path):
# transform_gal_1(path)
    result_1 = {}
    file = open(path,"r")
    gal = file.read()
    gal = gal.splitlines()
    for i in range(1, len(gal), 2):
        id = gal[i].split(' ')[0]
        value = gal[i+1].split(' ')
        result_1[id] = []
        result_1[id] = value
        
# new part
    result_2 = {}
    num = {}
    for id, value in result_1.items():
        num[id] = len(value)
    for id, value in result_1.items():
        result_2[len(value)] = []
        for i, n in num.items():
            if n == len(value):
                result_2[len(value)].append(i)
            else:
                pass
    return result_2


def asymmetries(path):
# transform_gal_1(path)
    result_1 = {}
    file = open(path,"r")
    gal = file.read()
    gal = gal.splitlines()
    for i in range(1, len(gal), 2):
        id = gal[i].split(' ')[0]
        value = gal[i+1].split(' ')
        result_1[id] = []
        result_1[id] = value

# new part
    test = []
    for id in result_1:
        for value in result_1[id]:
            if id in result_1[value]:
                pass
            else:
                test.append([id,value])
    if test == []:
        print("There is no asymmetries.")
    else:
        print("Asymmetries exists in %s" %test)


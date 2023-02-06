
f = open("Lab04-1.gal", "r")

flines = f.readlines() 
flines = flines[1: ]



linelist = [] 
for x in flines:
  line = x[ :-1].split(' ') 
  print(line)
  linelist.append(line)



h = {}
for i,li in enumerate(linelist): 
    if i%2 == 0:
        id = li[0] 
        h[id]=[] 
    else:
        h[id]=li 


# ### 2. Take a gal dictionary from 1 and return a second dictionary that has the histogram for the neighbor cardinalities. In the second dictionary, the key is the number of neighbors and the value is the list of ids that have key neighbors. It is up to you if you want to draw the histogram. 


list1=[]
for i, li in enumerate(linelist):
    if i%2 == 0:
        list1.append(li)

h1 = {}
for i,li in enumerate(list1):
    id1 = int(li[1])
    value = int(li[0]) 
    if id1 not in h1:
        id1 = int(li[1])
        h1[id1]=[]
    h1[id1].append(value) 

    
# ### 3. Take a gal dictionary from 1 and test if there are any asymmetries. An asymmetry occurs when i says j is a neighbor of i, but j does not say i is a neighbor of j.

for id in h:
    for neighbor in h[id]: 
        print(id,' says ',neighbor, 'is a neighbor')
        if id in h[neighbor]: 
            print('Yes')
        else:
            print('No')
            print('because ', neighbor, ' says that ', id, 'is not a neighbor')
            
#An asymmetry occurs because 9 is 21's neighbor but 21 is not 9's neighbor.


#!/usr/bin/env python
# coding: utf-8

# In[255]:


def question1(f):
    from pandas.core.frame import DataFrame
    with open(f) as file:
        list = file.readlines()
    for i in range(1,len(list)):
        list[i]=list[i].strip('\n')
        list[i]=str(list[i])
        list[i]=list[i].split()
    for i in range(1,len(list)):
        list[i-1]=list[i]
    del list[len(list)-1]
    listcp=list
    list=DataFrame(list)
    for i in range(0,len(listcp),2):
        c={list.at[i,0]:listcp[i+1]}
        d.update(c)
    return d
question1('Lab04-1.gal')


# In[221]:


def question2(f):
    from pandas.core.frame import DataFrame
    with open(f) as file:
        list = file.readlines()
    for i in range(1,len(list)):
        list[i]=list[i].strip('\n')
        list[i]=str(list[i])
        list[i]=list[i].split()
    for i in range(1,len(list)):
        list[i-1]=list[i]
    del list[len(list)-1]
    listcp=list
    list=DataFrame(list)
    nnum=[]
    for i in range(0,len(listcp),2):
        if int(list.at[i,1]) not in nnum:
            nnum.append(int(list.at[i,1]))
    c={}
    for num in nnum:
        for i in range(0,len(listcp),2):
            if int(list.at[i,1])==num:
                c[num]=c.get(num,[])+[int(list.at[i,0])]
    return c
question2('Lab04-1.gal')


# In[266]:


def question3(f): 
    from pandas.core.frame import DataFrame
    with open(f) as file:
        list = file.readlines()
    for i in range(1,len(list)):
        list[i]=list[i].strip('\n')
        list[i]=str(list[i])
        list[i]=list[i].split()
    for i in range(1,len(list)):
        list[i-1]=list[i]
    del list[len(list)-1]
    listcp=list
    list=DataFrame(list)
    for i in range(0,len(listcp),2):
        c={list.at[i,0]:listcp[i+1]}
        d.update(c)
    for key in d:
        for i in d:
            if i in d[key]:
                if key not in d[i]:
                    print(key,"and",i,"are asymmetries")
                    test=False
    if test:
        print("No problem!")
question3('Lab04-1.gal')


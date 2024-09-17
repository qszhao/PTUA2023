#!/usr/bin/env python
# coding: utf-8

# In[29]:


#1
#f = open("G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal", "r")
with open('G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal', mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # 读取文件
    try:
        lines = lines[1:] # 只读取第一行之后的内容
        f.close()             # 关闭文件
    except:
        pass

dic = {}
i=1
for line in lines:
    
    #line1
    if i%2 == 1:      
        list1 = line[:-1].split(' ')
        key = list1[0]
        num = int(list1[1])
        i = i+1
    #line2
    elif i%2 == 0:
        list2 = line[:-1].split(' ')
        dic[key] = list2
        i = i+1
print(dic)


# In[30]:


#2
#f = open("G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal", "r")
with open('G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal', mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # 读取文件
    try:
        lines = lines[1:] # 只读取第一行之后的内容
        f.close()             # 关闭文件
    except:
        pass

dic = {}
i=1
for line in lines:
    
    #line1
    if i%2 == 1:      
        list1 = line[:-1].split(' ')
        key = list1[0]
        num = int(list1[1])
        i = i+1
    #line2
    elif i%2 == 0:
        list2 = line[:-1].split(' ')
        dic[num] = list2
        i = i+1
print(dic)


# In[39]:


#3
#f = open("G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal", "r")
with open('G:\\my_project\PTUA2023\Lab04\Lab\Lab04-1.gal', mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # 读取文件
    try:
        lines = lines[1:] # 只读取第一行之后的内容
        f.close()             # 关闭文件
    except:
        pass

dic = {}
i=1
for line in lines:
    
    #line1
    if i%2 == 1:      
        list1 = line[:-1].split(' ')
        key = list1[0]
        num = int(list1[1])
        i = i+1
    #line2
    elif i%2 == 0:
        list2 = line[:-1].split(' ')
        dic[key] = list2
        i = i+1
#print(dic)
#The code above is to get the dictionary of question 1.

x = 0
for k in dic:
    value_list = dic[k]
    for value in value_list:
        #judge if the list corresponding to 'value' contains 'k'
        list = dic[value]
        if list.count(k) == 1:
            continue
        else:
            print('{} and {} have a problematic neighbourhood relationship, the dictionary has asymmetry'.format(k,value))
            x = 1
if x == 0:
    print('There are no asymmetries in that dictionary')


# In[ ]:





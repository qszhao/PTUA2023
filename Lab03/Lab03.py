#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# We’ve seen that n = 42 is legal. What about 42 = n?


# In[10]:


42 = n 


# In[ ]:


# How about x = y = 1?


# In[19]:


x = y = 1 


# In[20]:


# In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?


# In[21]:


# What if you put a period at the end of a statement?


# In[22]:


# In math notation you can multiply x and y like this: x y. What happens if you try that in Python?


# In[23]:


# The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?


# In[24]:


pi = 3.1415926535897932
r = 5
4.0/3.0*pi*r**3 


# In[ ]:


# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?


# In[17]:


24.95*0.6*60+0.75*(60-1)+3


# In[ ]:


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?


# In[16]:


start = (6*60+52)*60
easy = (8*60+15)*2
fast = (7*60+12)*3
finish_hour = (start + easy + fast)/(60*60.0)
finish_floored = (start + easy + fast)//(60*60)  
finish_minute  = (finish_hour - finish_floored)*60
print ('Finish time was %d:%d' % (finish_hour,finish_minute))


# In[ ]:





# In[ ]:





# In[ ]:





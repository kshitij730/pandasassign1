#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series."""


# In[2]:


pip install pandas


# In[1]:


l1 = [4,8,15,16,23,42]


# In[2]:


l1


# In[5]:


import pandas as pd
data = [4,8,15,16,23,42]
df = pd.Series(data)
print(df)


# In[6]:


"""Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it."""


# In[8]:


import pandas as pd
data1 = ["kshitij", 23, 23.45, True, [2,3,4,5], (4,5,6), 23+45j]
df = pd.Series(data1)
print(df.dtype)


# In[1]:


"""Q3. Create a Pandas DataFrame that contains the following data:

Then, print the DataFrame."""


# In[11]:


import pandas as pd
data3 = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
df = pd.DataFrame(data3)


# In[12]:


print(df)


# In[13]:


"""What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example."""


# In[15]:


import pandas as pd
data3 = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
df = pd.DataFrame(data3)
df1 = pd.Series(data3)


# In[16]:


print(df)
print(df1)


# In[17]:


"""What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
you give an example of when you might use one of these functions?"""


# In[18]:


import pandas as pd
data3 = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
df = pd.DataFrame(data3)
print(df)


# In[19]:


df.head(1)


# In[20]:


df.tail(2)


# In[21]:


df.columns


# In[22]:


df['Name']


# In[ ]:





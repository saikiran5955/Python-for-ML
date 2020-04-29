#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


df=pd.read_csv("C:\\Users\\SaiKiran\\Downloads\\read_csv\\read_csv\\data.csv")


# In[10]:


pwd


# In[15]:


df.head()


# In[16]:


df1=pd.read_excel("C:\\Users\\SaiKiran\\Downloads\\read_csv\\read_csv\\data.xlsx")


# In[17]:


df1.head()


# In[23]:


df2=pd.read_csv("C:\\Users\\SaiKiran\\Downloads\\dataframes\\dataframes\\data.csv")


# In[24]:


df2.head()


# In[26]:


df2.shape


# In[27]:


#bottom 5 rows
df2.tail()


# In[28]:


df2.tail(6)


# In[29]:


df2.columns


# In[30]:


df2['ID']


# In[31]:


df2[['ID','Cancer_Type']]


# In[36]:


df2.iloc[:,1:5]


# df

# In[38]:


df2[df2['Cancer_Type']==4]


# In[39]:


df3=pd.read_csv("C:\\Users\\SaiKiran\\Downloads\\data_python_csv\\data_python.csv")


# In[41]:


df3.iloc[:,3:5]


# ### 

# In[43]:


df3.loc[:,['Dependents','Education']]


# In[45]:


df3.iloc[5:]


# In[46]:


df3['Gender']


# In[ ]:





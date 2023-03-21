#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# In[39]:


dataset = pd.read_csv("final_dataset.csv")
dataset.head(3)


# In[40]:


dataset.columns


# In[41]:


x = dataset.iloc[:,:-1]
y = dataset["Selling_Price"]


# In[42]:


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=39)


# In[43]:


rfr = RandomForestRegressor()


# In[44]:


rfr.fit(x_train.values,y_train)


# In[45]:


rfr.predict([[90,2,1,2014,5.59,27000]])


# In[46]:


import pickle


# In[47]:


p = open("car.txt","wb")
pickle.dump(rfr,p)
p.close()


# In[ ]:





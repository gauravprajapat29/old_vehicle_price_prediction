#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[78]:


dataset = pd.read_csv("car data.csv")
dataset.head(3)


# In[121]:


(dataset["Car_Name"].sort_values()).unique()


# In[122]:


(dataset["Year"].sort_values()).unique()


# In[123]:


(dataset["Fuel_Type"].sort_values()).unique()


# In[124]:


(dataset["Transmission"].sort_values()).unique()


# In[ ]:





# In[ ]:





# In[79]:


dataset.shape


# In[80]:


dataset.info()


# In[81]:


dataset.drop(columns=["Owner"],inplace=True)


# In[82]:


dataset.drop(columns=["Selling_type"],inplace=True)


# In[83]:


dataset.head(2)


# In[84]:


dataset.columns


# In[85]:


obj_col = dataset.select_dtypes(include=["object"]).keys()


# In[86]:


input_data = dataset[['Car_Name', 'Year', 'Present_Price', 'Driven_kms','Fuel_Type', 'Transmission']]


# In[87]:


output_data = dataset["Selling_Price"]


# In[88]:


from sklearn.preprocessing import OneHotEncoder,LabelEncoder


# In[89]:


def encoding(x,c):
    le = LabelEncoder()
    le.fit(x)
    p = le.transform(x)
    t = pd.DataFrame(p,columns=[c])
    return t


# In[90]:


tu = []
for i in obj_col:
    tu.append(encoding(dataset[[i]],i))


# In[91]:


tu = tuple(tu)


# In[92]:


encode_data = pd.concat(tu,axis=1)


# In[93]:


encode_data


# In[94]:


int_data = input_data.select_dtypes(include=["int64","float64"])


# In[95]:


int_data


# In[96]:


new_data = pd.concat((encode_data,int_data,output_data),axis=1)


# In[97]:


new_data.head(2)


# In[98]:


sns.boxplot(new_data["Selling_Price"])


# In[99]:


q1 = new_data["Selling_Price"].quantile(0.25)
q3 = new_data["Selling_Price"].quantile(0.75)


# In[100]:


min_data = q1-1.5*(q3-q1)
max_data = q3+1.5*(q3-q1)


# In[101]:


new_data.describe()


# In[102]:


final_dataset = new_data[new_data["Selling_Price"]<max_data]


# In[103]:


final_dataset.to_csv("final_dataset.csv",index=False)


# In[ ]:





# In[104]:


x = new_data.iloc[:,:-1]
y = new_data.iloc[:,-1]


# In[105]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


# In[106]:


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=39)


# In[107]:


lr = LinearRegression()
dt = DecisionTreeRegressor()
svr = SVR()
rfr = RandomForestRegressor()
knn = KNeighborsRegressor()


# In[108]:


lr.fit(x_train,y_train)
dt.fit(x_train,y_train)
svr.fit(x_train,y_train)
rfr.fit(x_train,y_train)
knn.fit(x_train,y_train)


# In[109]:


lr.score(x_train,y_train),lr.score(x_test,y_test)


# In[110]:


dt.score(x_train,y_train),dt.score(x_test,y_test)


# In[111]:


svr.score(x_train,y_train),svr.score(x_test,y_test)


# In[112]:


rfr.score(x_train,y_train),rfr.score(x_test,y_test)


# In[113]:


knn.score(x_train,y_train),knn.score(x_test,y_test)


# In[ ]:





# In[114]:


t1,t2,t3,t4,t5 = [],[],[],[],[]


# In[115]:


for i in range(1,50):
    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=i)
    lr.fit(x_train,y_train)
    dt.fit(x_train,y_train)
    svr.fit(x_train,y_train)
    rfr.fit(x_train,y_train)
    knn.fit(x_train,y_train)
    t1.append((lr.score(x_train,y_train),lr.score(x_test,y_test)))
    t2.append((dt.score(x_train,y_train),dt.score(x_test,y_test)))
    t3.append((svr.score(x_train,y_train),svr.score(x_test,y_test)))
    t4.append((rfr.score(x_train,y_train),rfr.score(x_test,y_test)))
    t5.append((knn.score(x_train,y_train),knn.score(x_test,y_test)))


# In[ ]:





# In[ ]:





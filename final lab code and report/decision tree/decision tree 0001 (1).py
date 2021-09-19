#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import tree
from sklearn import metrics,model_selection,preprocessing
from IPython.display import Image,display
import matplotlib.pyplot as plt,pydotplus


# In[2]:


data=pd.read_csv("prity12.csv")
data.head()


# In[3]:


data.info()


# # DataPreprocessing 

# In[4]:


df=data
df=df.drop(['Model'],axis=1)


# In[5]:


df.Engine=pd.Categorical(df.Engine)
df['EngineCode']=df.Engine.cat.codes

df['SC/Turbo']=pd.Categorical(df['SC/Turbo'])
df['SC/Turbo_code']=df['SC/Turbo'].cat.codes

df.Weight=pd.Categorical(df.Weight)
df['weight_Code']=df.Weight.cat.codes

df['Fuel Economy']=pd.Categorical(df['Fuel Economy'])
df['Fuel_Economy_code']=df['Fuel Economy'].cat.codes

df.Fast=pd.Categorical(df.Fast)
df['Fast_code']=df.Fast.cat.codes


# In[6]:


df.info()


# In[7]:


df.columns


# In[8]:


df_new=df.drop(['Engine', 'SC/Turbo', 'Weight', 'Fuel Economy', 'Fast'],axis=1)
df_new.head()


# # Train and Test data for the model

# In[9]:


X=df_new.drop(['Fast_code'],axis=1)
Y=df['Fast_code']
X.shape,Y.shape


# In[10]:


df_test=df_new.sample(n=5)
x_test=df_test.drop(['Fast_code'],axis=1)
y_test=df_test['Fast_code']


# In[11]:


model_tree=tree.DecisionTreeClassifier()
model_tree.fit(X,Y)


# In[12]:


y_pred=model_tree.predict(x_test)


# In[13]:


print(y_pred)
y_test


# # Metrics Evaluation

# In[14]:


wrong_pred=(y_test != y_pred).sum()
print("Total Wrongly predicted = {}".format(wrong_pred))

accuracy=metrics.accuracy_score(y_test,y_pred)
print("Accuracy of this model = {:.3f}".format(accuracy))


# # Graphical view of the tree 

# In[15]:


ddata=tree.export_graphviz(model_tree,out_file=None,filled=True,rounded=True,
                          feature_names=['Engine','SC/Turbo','weight','Fuel Economy'],
                          class_names=['YES','NO'])
graph=pydotplus.graph_from_dot_data(ddata)
display(Image(graph.create_png()))


# In[16]:


import os

os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"


# In[17]:


ddata=tree.export_graphviz(model_tree,out_file=None,filled=True,rounded=True,
                          feature_names=['Engine','SC/Turbo','weight','Fuel Economy'],
                          class_names=['YES','NO'])
graph=pydotplus.graph_from_dot_data(ddata)
display(Image(graph.create_png()))


# # Save Model

# In[37]:


import pickle 
  
# Save the trained model as a pickle string. 
model_file="model.bkp"
pickle.dump(model_tree, open(model_file, 'wb')) 

#loading the model
loaded_model=pickle.load(open(model_file, 'rb'))
loaded_model.predict(x_test)


# In[36]:





# In[ ]:





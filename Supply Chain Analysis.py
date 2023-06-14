#!/usr/bin/env python
# coding: utf-8

# **Vedant Modak**
#   | BE(IT) undergrad @ PES Modern College of Engineering,Pune.

# **Supply Chain Analysis**

# **Importing necessary libraries**

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[25]:


df=pd.read_csv('F:\Data Analytics\Portfolio\Projects\Project - 4 (Supply Chain)\Port_data.csv')


# In[26]:


df.head()


# In[27]:


df.tail()


# In[28]:


df.shape


# In[29]:


df.info()


# **Cleaning the datatset**

# In[30]:


df = df.drop_duplicates()


# In[31]:


df.isnull().sum()


# In[32]:


df.describe()


# In[33]:


df['UN Code'] = df['UN Code']. replace(np. nan, 0)


# In[34]:


df.dropna()


# In[35]:


df.isnull().sum()


# **Removing Outliers**

# In[36]:


sns.boxplot(df['Vessels in Port'])


# In[37]:


sns.boxplot(df['Expected Arrivals'])


# In[38]:


def remove_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    threshold = 1.5 * IQR
    outlier_mask = (column < Q1 - threshold) | (column > Q3 + threshold)
    return column[~outlier_mask]


# In[39]:


col_name = ['Vessels in Port', 'Expected Arrivals']
for col in col_name:
    df[col] = remove_outliers(df[col])


# In[40]:


plt.figure(figsize=(10, 6)) 

for col in col_name:
    sns.boxplot(data=df[col])
    plt.title(col)
    plt.show()


# **Visualizations**

# **Top 10 Country-wise count**

# In[41]:


ItemCount = df["Country"].value_counts().nlargest(10)
print("Top 10 Countries Wise Count \n")
print(ItemCount)
sns.set_context("talk",font_scale=1)
plt.figure(figsize=(22,6))
sns.countplot(df['Country'],order = df['Country'].value_counts().nlargest(10).index)
plt.title('Top 10 Countries Wise Count \n')
plt.ylabel('Total Count')
plt.xlabel('Country Name')


# **Top 15 Country wise vessel count**

# In[58]:


Vessel_count = df.groupby(['Country'])['Vessels in Port'].sum().nlargest(15)
print("Total Vessel count of Top 15 Countries\n")
print(Vessel_count)
plt.figure(figsize=(22,12))
GraphData=df.groupby(['Country'])['Vessels in Port'].sum().nlargest(15)
GraphData.plot(kind='bar')
plt.ylabel('Vessels in Port')
plt.xlabel('Country Name')


# In[60]:


ItemCount_2 = df["Area Global"].value_counts()
print("Global Area Count \n")
print(ItemCount_2)
sns.set_context("talk",font_scale=1)
plt.figure(figsize=(22,22))
sns.countplot(df['Country'],order = df['Country'].value_counts().index)
plt.title('Global Ara Count \n')
plt.ylabel('Total Count')
plt.xlabel('Area Name')


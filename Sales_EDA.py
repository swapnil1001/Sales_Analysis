#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #mathematical use arrays
import pandas as pd # dataframework
import matplotlib.pyplot as plt #visualization data
import seaborn as sns


# In[2]:


df = pd.read_csv('Sales Data.csv',encoding = 'unicode_escape')
#to avoid encoding error, use 'unicode escape'


# In[3]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'], axis=1,inplace=True)


# In[4]:


#drop null values
df.dropna(inplace=True)


# In[10]:


ax=sns.countplot(x= 'Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[8]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot (x= 'Gender',y='Amount' , data=sales_gen )


# Observation 1 : Above graphs states that the most of the buyers are female  and even the purchasing power of female is more than male

# In[12]:


ax=sns.countplot(data= df, x= 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[13]:


#Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group', y='Amount',data=sales_age)


# In[14]:


#total number of orders from top 10 states
sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='State',y='Orders')


# In[15]:


#total amount/sales from top 10 states
sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='State',y='Amount')


# Observation 2: Above graphs states that most of the orders and total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively.

# In[17]:


ax = sns.countplot(data = df, x= 'Marital_Status')

sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data=sales_state, x='Marital_Status',y='Amount',hue='Gender')


# Observation 3 : Above graphs states that most of the buyers are married women and they have also high purchasing power.

# In[18]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data = df, x= 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[19]:


sales_state = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Occupation',y='Amount')


#  Observation 4 : Above graphs state that most of the buyers are working in IT,Healthcare Sector and Aviation

# In[20]:


sns.set(rc={'figure.figsize':(30,5)})

ax = sns.countplot(data = df, x= 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


sales_state = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_Category',y='Amount')


# Observation 5 : Above graphs states that most of the sold products are from Food, Clothing & Apparel and Electronics & Gadget

# In[22]:


#top 10 most sold products
sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_ID',y='Orders')


# From all the previous observations we can conclude the below statement for the dataset.

# Conclusion:
#     
# Married Woman age group 26-35 yrs from UP,Maharastra & Karnataka working in IT, Healthcare and Aviation are more likely to buy products from food, clothing & apparels and electronics& gadgets. ID's of the top most products sold are P00265242,P00110942 and P00237542.

# In[ ]:





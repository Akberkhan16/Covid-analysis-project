#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd


# # Importing dataset using pandas

# In[50]:


df =pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')
df.head()


# # High Level Data Understanding

# # a. Find no of Rows & Columns in dataset

# In[51]:


# Number of Rows and Columns in dataset
df.shape


# # b. Data types of columns

# In[52]:


# Data types of Columns
df.dtypes


# # c. Info & Describe of data in dataframe
# 

# In[53]:


df.describe()


# In[54]:


df.info()


# # Low Level Data Understanding

# # a. Find count of unique values in location column.

# In[55]:


# Count of unique values in location Columns
df.nunique()


# # b. Find which continent has maximum frequency using values counts.

# In[56]:


df['continent'].value_counts()


# # c. Find maximum & mean value in 'total_cases'.

# In[57]:


df['total_cases'].max()


# In[58]:


df['total_cases'].mean()


# # d. Find 25%,50% & 75% quartile value in 'total_deaths'.

# In[59]:


df['total_deaths'].describe()


# # e. Find which continent has maximum 'human_development_index'.

# In[60]:


df[df['human_development_index']==max(df['human_development_index'])]['continent'] 


# # f. Find which continent has minimum 'gdp_per_capita'.

# In[61]:


df[df['gdp_per_capita']==min(df['gdp_per_capita'])]['continent'].min()


# # 4. Filter the dataframe with only this columns
# ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] and update the data frame.
# 

# In[62]:


df_filter = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita']]


# In[63]:


df_filter


# # 5. Data Cleaning
#  a. Remove all duplicates observations
# 

# In[64]:


df.drop_duplicates()


# ### b. Find missing values in all columns

# In[65]:


df.isnull().sum()


# # c. Remove all observations where continent column value is missing
# 

# In[66]:


df.dropnasubset=('continent')


# # d. Fill all missing values with 0

# In[67]:


df.fillna(0)


# # 6. Date time format :
#  a. Convert date column in datetime format using 
# pandas.to_datetime
# 

# In[68]:


df['date']= pd.to_datetime(df['date'])
df.dtypes


# # b. Create new column month after extracting month data from date column.

# In[69]:


df['month'] =pd.DatetimeIndex(df['date']).month 


# In[70]:


df.head()


# # 7. Data Aggregation:
#  a. Find max value in all columns using groupby function on 
# 'continent'
#  column

# In[71]:


df2 = df.groupby(['continent']).max()


# In[72]:


df2


# # b. Store the result in a new dataframe named 'df_groupby'.
# (Use df_groupby dataframe for all further analysis)

# In[73]:


df_groupby = pd.DataFrame(df2)


# In[74]:


df_groupby


# # 8. Feature Engineering :
#  a. Create a new feature 'total_deaths_to_total_cases' by ratio of
#  'total_deaths' column to 'total_cases'
# 

# In[75]:


df['ratio'] = df['total_deaths']/df['total_cases']


# In[76]:


# Url.head()
df['ratio'].value_counts()


# # 9. Data Visualization :

# # a. perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn distplot

# In[77]:


import seaborn as sns


# In[78]:


sns.distplot(df['gdp_per_capita'],kde = False, color = 'red',bins=10)


# # df_groupby dataset

# In[79]:


df_groupby


# # b. plot a pairplot of df_groupby dataset 

# In[ ]:


sns.pairplot(df_groupby)


# # c. plot a sactter plot of 'total_cases' & 'gdp_pre_capita' 

# In[80]:


sns.relplot(x="gdp_per_capita", y="total_cases", data=df)


# # d. plot a bar plot of 'continent' column with 'total_cases'

# In[81]:


sns.barplot(x="continent", y="total_cases", data=df)


# # 10. saving df_groupby dataFrame in local drive using pandas.to_csv

# In[82]:


df_groupby.to_csv('csv_file')


# In[83]:


df_groupby


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





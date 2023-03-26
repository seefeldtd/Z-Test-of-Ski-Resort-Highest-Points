#!/usr/bin/env python
# coding: utf-8

# # Simple Z-test

# In[1]:


import pandas as pd
df = pd.read_csv('D://DataSets//ski_resorts.csv', encoding='cp1252')
df.head(5)


# ## Compare the average highest point of French ski resorts and Italian Resorts

# In[2]:


height = df[['Country', 'Highest point']]


# # Two-tailed Z-Test
# 
# ## H0: The mean highest points between the two countries are equal
# ## H1: The mean highest points between the two countries are different
# ### alpha = .05

# In[3]:


fra = height.query('Country == "France"')['Highest point']
ita = height.query('Country == "Italy"')['Highest point']

height.groupby('Country').describe()


# In[4]:


import seaborn as sns

sns.distplot(fra)
sns.distplot(ita)


# ## Below calculations are for normality. 
# 
# ### Shapito-Wilkes Test:
# #### P-values > 0.05. Therefore, we cannot reject that the distribution is normally distributed.
# 
# ### Skewness:
# #### P-values > 0.05 suggest we cannot reject null hypothesis that the distrpution is normal for fra and ita.
# 
# ### Kurtosis:
# #### P-values suggest we cannot reject null hypothesis that the distrpution is normal for fra and ita.
# 
# #### We do not have to transform the data for normality!
# 
# 

# In[10]:


import scipy.stats as stats
from scipy.stats import kurtosistest
from statsmodels.stats.weightstats import ztest as ztest

print("fra Shapiro result: ", stats.shapiro(fra), "\nita Shapiro result: ", stats.shapiro(ita))


# In[6]:


print("fra Skewness result: ", stats.skewtest(fra), "\nita Skewness result: ", stats.skewtest(ita))


# In[7]:


print("fra Kurtosis result: ", kurtosistest(fra),"\nita Kustosis result: ", kurtosistest(ita))


# ## Calculate Z-Test Statistic
# 
# ### P-value>0.05 suggests we cannot reject H0, the means are equal

# In[12]:


# variance between groups is not ewqul, therefore equal_var is false

print("Z-Test result: ", ztest(fra, ita, value =0))


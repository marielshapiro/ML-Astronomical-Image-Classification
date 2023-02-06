#!/usr/bin/env python
# coding: utf-8

# In[1]:


## for data
import pandas as pd
import numpy as np
## for plotting
import matplotlib.pyplot as plt
import seaborn as sns
## for statistical tests
import scipy
import statsmodels.formula.api as smf
import statsmodels.api as sm
## for machine learning
from sklearn import model_selection, preprocessing, feature_selection, ensemble, linear_model, metrics, decomposition
## for explainer
from lime import lime_tabular
import seaborn as sns


# In[2]:


df = pd.read_csv('training_set.csv')
df.head()


# In[4]:


lightcurve_615 = df.loc[(df['object_id'] == 615)]
g = sns.FacetGrid(lightcurve_615, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())
#do this with other objects


# In[6]:


lightcurve_713 = df.loc[(df['object_id'] == 713)]
g = sns.FacetGrid(lightcurve_713, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())
#do this with other objects


# In[10]:


df['object_id'].unique()


# In[11]:


lightcurve_730 = df.loc[(df['object_id'] == 730)]
g = sns.FacetGrid(lightcurve_730, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())


# In[12]:


lightcurve_130762946 = df.loc[(df['object_id'] == 130762946)]
g = sns.FacetGrid(lightcurve_130762946, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())


# In[13]:


lightcurve_130772921 = df.loc[(df['object_id'] == 130772921)]
g = sns.FacetGrid(lightcurve_130772921, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())


# In[14]:


lightcurve_130779836 = df.loc[(df['object_id'] == 130779836)]
g = sns.FacetGrid(lightcurve_130779836, col='passband', col_wrap=3)
g = (g.map(plt.scatter,"mjd","flux", s = 10).add_legend())


# In[ ]:





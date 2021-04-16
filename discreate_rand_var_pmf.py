#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy.random import choice


def count_frequencies(data,relative=False):
    counter={}
    for element in data:
        if element not in counter:
            counter[element]=1
        else:
            counter[element]=counter[element]+1
    if relative:
        for element in counter:
            counter[element]=counter[element]/len(data)
    return counter


# In[5]:


from numpy.random import binomial
binomial(10,0.3)


# In[7]:


from scipy.stats import binom


# In[10]:


sample=binomial(10,0.3,size=1000)
X=binom(100,0.3)
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
x=np.arange(0,10,0.1)
n=10
p=0.5
sample=binomial(n,p,size=10000)
X=binom(n,p)
freqs=count_frequencies(sample,relative=True)
plt.plot(x,X.pmf(x),color='red')
plt.bar(list(freqs.keys()),list(freqs.values()))


# In[ ]:





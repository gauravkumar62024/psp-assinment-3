#!/usr/bin/env python
# coding: utf-8

# In[1]:


#generating continuous random variable and comparing with pdf in histogram.

from numpy.random import uniform
uniform(low=-2,high=2,size=10)
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


sample=uniform(low=-2,high=2,size=100)
plt.hist(sample,density=True)
import scipy.stats
X=scipy.stats.uniform(-2,4)
X.pdf(1.5)
import numpy as np
x=np.linspace(-3,3,1000)
plt.plot(x,X.pdf(x))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# kaksi normaalijakaumaa

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import ipywidgets as widgets

def verenpaine_interaktiivisesti():
    interactive_plot = widgets.interactive(verenpaineet, mu1=widgets.FloatSlider(value=135, min=100, max=200, step=5, description = "$\mu_1$"),
                                           variance1=widgets.FloatSlider(value=30, min=10, max=100, step=5, description = "$\sigma_1$"), 
                                           mu2=widgets.FloatSlider(value=145, min=100, max=200, step=5, description = "$\mu_2$"),
                                           variance2=widgets.FloatSlider(value=40, min=10, max=100, step=5, description = "$\sigma_2$"))                        
    return interactive_plot


def verenpaineet(mu1,mu2,variance1,variance2):
    x = np.linspace(100, 200, 100)
    sigma1 = math.sqrt(variance1)
    sigma2 = math.sqrt(variance2)
    plt.plot(x, stats.norm.pdf(x, mu1, sigma1),color="red")
    plt.plot(x, stats.norm.pdf(x, mu2, sigma2),color="green")
    plt.xlabel("Verenpaine")
    plt.show()

interaktiivinen_graafi = verenpaine_interaktiivisesti()
interaktiivinen_graafi


# In[ ]:





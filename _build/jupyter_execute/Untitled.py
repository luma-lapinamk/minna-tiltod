#!/usr/bin/env python
# coding: utf-8

# In[1]:



import matplotlib.pyplot as plt
import numpy as np
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
    prob_density1 = 1/(sigma1*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu1)/sigma1)**2)
    prob_density2 = 1/(sigma2*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu2)/sigma2)**2)
    plt.plot(x, prob_density1, color="red")
    plt.plot(x, prob_density2, color="green")
    plt.xlabel("Verenpaine")
    plt.show()

interaktiivinen_graafi = verenpaine_interaktiivisesti()
interaktiivinen_graafi


# In[ ]:





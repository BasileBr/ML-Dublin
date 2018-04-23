# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:43:12 2018

@author: Basile Bruhat
"""


import plotly
import plotly.graph_objs


import numpy as np


def DisplayGraph(features,nomfichier):
    if features.type == continu:
        
        if features.card >= 10:
            py.plot(features.val)
        else:
            ploty.graph_objs.Bar(features.val)
    else:
        go.bar(features.val)


x = np.random.randn(500)
data = [go.Histogram(x=x)]

py.iplot(data, filename='basic histogram')

'''

import plotly
"""from plotly.graph_objs import Scatter, Layout"""
import plotly.graph_objs

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.plot({
    "data": [plotly.graph_objs.Bar(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})
    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:43:12 2018

@author: Basile Bruhat
"""
from collections import Counter

import pandas as pd
import plotly as ply


class View:   
       
    def graph_continuous(self):
        'raw = self.get_continuous()'
        df = pd.read_csv("./results/E-DQR-continuous.csv")
        dc = pd.read_csv("./results/continuous-features.csv")
        'print(df)'
        size = df.shape 
        data = {col: list(df[col]) for col in df.columns}
        data_continuous = {col: list(dc[col]) for col in dc.columns}
        
        for i in range(0,size[0]):
            feature = data["Feature name"][i]
            
            if data["Card"][i] >=10:

                 ply.offline.plot({
                         "data": [ply.graph_objs.Histogram(x=data_continuous[feature])],
                         "layout": ply.graph_objs.Layout(
                                 title="Histogram of feature :" + feature + " for cardinality >=10"
                                 )
                 }, filename="./results/%s.html" %feature)
                         
            else:
                tab_value = Counter(data_continuous[feature])
                val = []
                kley = []
                for cle, valeur in tab_value.items():
#                    print("La clé {} contient la valeur {}.".format(cle, valeur))
                    val.append(valeur)
                    kley.append(cle)
                print(cle,valeur)
# =============================================================================
#                 tab_value = Counter(data_continuous[feature])
#                 print(tab_value.keys())
# =============================================================================
                
                ply.offline.plot({
                        "data": [ply.graph_objs.Bar(x=kley, y=val)],
                        "layout": ply.graph_objs.Layout(
                                    title="Bar plot for feature :" + feature + "for cardinality <10"
                                )
                }, filename="./results/%s.html" % feature)
                        
    def graph_categorical(self):
            
        df = pd.read_csv("./results/E-DQR-categorical.csv");
        dc = pd.read_csv("./results/categorical-features.csv");
        size = df.shape;
        
        data = {col: list(df[col]) for col in df.columns}
        data_categorical = {col: list(dc[col]) for col in dc.columns}
        
        for i in range(0,size[0]):
            feature = data["Feature name"][i]
            tab_value = Counter(data_categorical[feature])
            val = []
            kley = []
            for cle, valeur in tab_value.items():
                
                val.append(valeur)
                kley.append(cle)
    
            
            ply.offline.plot({
                    "data": [
                            ply.graph_objs.Bar(
                                    x=kley,
                                    y=val
                                    )
                            ],
                    "layout": ply.graph_objs.Layout(
                            title="Bar plot for feature :" + feature + "for categorical"
                            )
                    }, filename="./results/%s.html" % feature)
        
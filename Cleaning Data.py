# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:44:57 2017

@author: Sabs
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("dataset.csv")
standardize = StandardScaler().fit(data)
rescaledX = standardize.transform(data)
final = rescaledX.dropna(axis=0,how='any')
print final
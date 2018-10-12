# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:39:47 2017

@author: Sabs
"""

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import time

t0 = time.clock()

data = pd.read_csv("dataset.csv")
cleaned = data.dropna(axis=0, how="any")

y = cleaned.iloc[:,-1]
y = np.ravel(y)

X = cleaned.iloc[:,0:142]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

num_trees = 300
model = AdaBoostClassifier(n_estimators=num_trees, random_state=0)
model.fit(X_train, y_train)

predicted = model.predict(X_test)
print
print 'confusion matrix is: '
print metrics.confusion_matrix(y_test, predicted)
print 

score = metrics.accuracy_score(y_test, predicted)

t1 = time.clock()
t_total = t1 - t0

print 'score is: ', score
print
print 'Total run time is: ', t_total
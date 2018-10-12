# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:17:01 2017

@author: Sabs
"""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
import time

t0 = time.clock()

data = pd.read_csv("dataset.csv")
cleaned = data.dropna(axis=0, how="any")

y = cleaned.iloc[:,-1]
y = np.ravel(y)         #flatten y into a 1-D array

X = cleaned.iloc[:,0:142]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)

predicted = model.predict(X_test)
print
print 'confusion matrix is: '
print metrics.confusion_matrix(y_test, predicted)
print 

scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)

t1 = time.clock()
t_total = t1 - t0

print '10-fold Cross Validation scores are: '
print scores
print
print 'mean score is: ', scores.mean()
print
print 'Total run time is: ', t_total


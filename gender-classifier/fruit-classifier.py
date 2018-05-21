#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:06:57 2018

@author: subham
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 12:32:24 2017
machinelearning
@author: Subham Singh
"""
   #importing sciktlearn
from sklearn import tree
   #datasets
features= [[140,1],[130,1],[132,1],[135,1],[150,0],[170,0],[175,0],[172,0]]
   #here we use 1 for apple and 0 for oranges
labels = ['apple','apple','apple','apple','orange','orange','orange','orange'] 
   #building a classifier 
clf = tree.DecisionTreeClassifier() 
   #classifier object for finding patterns by training
clf = clf.fit(features,labels)
   #predicting the fruits by shape and weight
print (clf.predict([[172.2,0]]))
print (clf.predict([[120,1]]))
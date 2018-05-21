#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:17:19 2018

@author: subham
"""

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

gnb = gnb.fit(X, Y)

prediction = gnb.predict([[100, 70, 43]])

print (prediction)
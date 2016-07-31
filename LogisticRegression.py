#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os
import operator
import numpy as np
from numpy import loadtxt
import sklearn
from sklearn import linear_model

#rootdir = os.getcwd()
#os.chdir(rootdir/'featurefiles')
genres = ['folk', 'reggae', 'punk', 'metal', 'classical', 'electronica', 'hip hop','rock', 'r&b', 'pop','jazz']
genre_code = {'folk': 1, 'reggae': 2, 'punk': 3, 'metal': 4, 'classical': 5, 'electronica': 6, 'hip hop': 7, 'rock': 8, 'r&b': 9, 'pop': 10 , 'jazz' :11}

data = loadtxt('LR_FeatureFile.txt')
#	print data
labels = loadtxt('LR_LabelFile.txt')
#	print labels
clf = sklearn.linear_model.LogisticRegression(tol=0.0001, fit_intercept=True, intercept_scaling=1, solver='liblinear', max_iter=500, multi_class='ovr')
clf.fit(data, labels)
testdata = loadtxt('LR_TestFile.txt')
h = clf.predict(testdata)
print h
exit()

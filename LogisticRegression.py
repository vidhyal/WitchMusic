#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os
import operator
import numpy as np
from numpy import loadtxt
import sklearn
from sklearn import linear_model
from BalanceData import *
from sklearn.metrics import *
from sklearn.grid_search import GridSearchCV

ootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'LogisticRegressionOut.txt'),'w+')

train_features, train_labels, test_features, test_labels, test_keys = GetData()
#print len(train_features)
#input ("wait")
model = sklearn.linear_model.LogisticRegression(tol=0.00001, fit_intercept=True, intercept_scaling=1, solver='newton-cg',max_iter=150000,  multi_class='ovr')

#gs = GridSearchCV(model, param_grid={
#    'solver': ['newton-cg','liblinear','lbfgs', 'sag'],
#    'tol':[0.00001, 0.0001],
#    'C':[0.2, 0.5, 0.80]  #[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#       })
gs = model

gs.fit(train_features, train_labels)
#print gs.best_params_

#model.fit(train_features, train_labels)
#testdata = loadtxt('LR_TestFile.txt')
pred = gs.predict(test_features)
predictProb = gs.predict_proba(test_features)
train_acc = (gs.score(train_features, train_labels))
line = str(train_acc )+"\n"
#print train_acc
fout.write(line)



for key in range(len(test_keys)):
    line = test_keys[key]+"\t"
    for f in range(len(predictProb[key])):
      line +="%i:%f\t" % (f+1 , predictProb[key][f])
    line += "\n"
    fout.write(line)
fout.close()
 
fout = open(os.path.join(newdir,'LogisticRegressionMat.txt'),'w+')     
accuracy = accuracy_score(test_labels, pred)
confMat= confusion_matrix(test_labels, pred)
print confMat
result = '\n Accuracy of Logistic Regression = '
result+= '%f' %float(accuracy) + '\n \n'
print result

np.savetxt(fout,confMat, fmt="%5d")
line =str(accuracy)+ "\n"
fout.write(line)
fout.close()

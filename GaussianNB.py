#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

#This file implements the scikit version of Gaussian Naive Bayes classification for our data set. It calls the GetData function of the BalanceData module to obtain the training features and labels and testing features, labels and keys. It then calls the fit method on the Gaussian Naive Bayes model (which does not take any paramaters) to fit the model to the training features and labels available. The test features are tested on the fitted model to predict the labels for test features which are later used to obtain the test accuracy and confusion matrix. This module also calls the predict_proba method of the model to get per track, the probability of it being in a particular class. This predicted probability per track is stored in the file GaussianNBOut which shall be later be used by the combine method.  



import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import *
from BalanceData import *



rootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'GaussianNBOut.txt'),'w+')

train_features, train_labels, test_features, test_labels, test_keys = GetData() 

model = GaussianNB()
model.fit(train_features, train_labels)
pred = model.predict(test_features)
predictProb = model.predict_proba(test_features)
train_acc = (model.score(train_features, train_labels))
line = str(train_acc )+"\n"
train = ' Training Accuracy of Gaussian Naive Bayes = ' + line
print train
fout.write(line)



for key in range(len(test_keys)):
    line2 = test_keys[key]+"\t"
    for f in range(len(predictProb[key])):
      line2 +="%i:%f\t" % (f+1 , predictProb[key][f])
    line2 += "\n"
    fout.write(line2)
fout.close()
    
    
accuracy = accuracy_score(test_labels, pred)
print confusion_matrix(test_labels, pred)
result = '\n Testing Accuracy of Gaussian Naive Bayes = '
result+= '%f' %float(accuracy) + '\n \n'
print result




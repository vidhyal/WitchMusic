#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import *
from BalanceData import *



rootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'GaussOut'),'w+')

train_features, train_labels, test_features, test_labels, test_keys = GetData() 

model = GaussianNB()
model.fit(train_features, train_labels)
pred = model.predict(test_features)
predictProb = model.predict_proba(test_features)
train_acc = (model.score(train_features, train_labels))
line = str(train_acc )+"\n"
print train_acc
fout.write(line)



for key in range(len(test_keys)):
    line = test_keys[key]+"\t"
    for f in range(len(predictProb[key])):
      line +="%i:%f\t" % (f+1 , predictProb[key][f])
    line += "\n"
    fout.write(line)
fout.close()
    
    
accuracy = accuracy_score(test_labels, pred)
print confusion_matrix(test_labels, pred)

print accuracy


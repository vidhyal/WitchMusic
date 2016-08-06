#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

from sklearn import tree
from BalanceData import *
from sklearn.metrics import *

rootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'DecisionTreeOut.txt'),'w+')

train_features, train_labels, test_features, test_labels, test_keys = GetData()
model = tree.DecisionTreeClassifier()
model = model.fit(train_features, train_labels)
pred = model.predict(test_features)


predictProb = model.predict_proba(test_features)
train_acc = (model.score(train_features, train_labels))
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
result = '\n Accuracy of Decision Tree  = '
result+= '%f' %float(accuracy) + '\n \n'
print result

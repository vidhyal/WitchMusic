#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.


# This module contains the code to combine the classification results from the various models used as defined by the list 
# models. The combination is done using the formula as given in the following paper - 
# http://dl.acm.org/citation.cfm?id=2348480

from BalanceData import *
from constants import *
from sklearn.metrics import *


def getMaxLabel(prob):
    maxVal =0
    maxIndex =0
    for index in prob:
        if prob[index] >maxVal:
            maxVal = prob[index]
            maxIndex = index
    return maxIndex

rootdir = os.getcwd()
indir = os.path.join(rootdir,'sklearnTry')


models =["LogisticRegression","DecisionTree", "NeuralNets",  "GaussianNB"]
fout = {}
temp = {}
for model in models:
    str = model +'Out.txt'
    fin = open(os.path.join(indir,str),'r')
    conf = float(fin.readline().split("\n")[0])
    unprocessed_data = fin.readlines()
    iterlines = iter(unprocessed_data)    
    for line in iterlines:
        split_line = line.split('\t')
        track = split_line[0]
        prob = {}
        for element in split_line[1:-1]:
            prob[element.split(':')[0]] = float(element.split(':')[1])* conf

        if track in temp:
            earlyProb = temp[track]
            for i in prob:
                earlyProb[i] += prob[i]
            temp[track]= earlyProb

        else:
            temp[track] = prob
    fin.close()    

train_features, train_labels, test_features, test_labels, test_keys = GetData()
predict ={}
label = {}

for track in temp:
    labelIndex = int(getMaxLabel(temp[track])) -1
    
    predict[track] = genres[labelIndex]
    
ootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'CombineOut.txt'),'w+') 
pred =[]
for key in range(len(test_keys)):
    line = test_keys[key]#  key, 
    line += "\t" +test_labels[key] 
    line +="\t" +predict[test_keys[key]] +"\n"
    fout.write(line)
    pred.append(predict[test_keys[key]])
fout.close()
accuracy = accuracy_score(test_labels, pred)
print confusion_matrix(test_labels, pred)
result = '\n Testing Accuracy of Combine Method = '
result+= '%f' %float(accuracy) + '\n \n'
print result

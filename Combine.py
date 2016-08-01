#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

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


models =["NeuralNets", "GaussianNB"]
fout = {}
temp = {}
for model in models:
    str = model +'Out.txt'
    fin = open(os.path.join(indir,str),'r')
    conf = float(fin.readline().split("\n")[0])
    unprocessed_data = fin.readlines()
    iterlines = iter(unprocessed_data)    
    #next(iterlines)
    for line in iterlines:
        split_line = line.split('\t')
        track = split_line[0]
       # print track
        #input ("wait")
        prob = {}
        for element in split_line[2:-1]:
#            print element.split(':')[0]
#            print element.split(':')[1]
            prob[element.split(':')[0]] = float(element.split(':')[1])* conf
        earlyprob = {}
        if track in temp:
            earlyProb = temp[track]
            for i in prob:
                earlyProb[i] += prob[i]
        else:
            temp[track] = prob
    fin.close()    

train_features, train_labels, test_features, test_labels, test_keys = GetData()
predict ={}
label = {}
#for key in range(len(test_keys)):
#    label[test_keys[key]] = test_labels[key]

for track in temp:
    labelIndex = int(getMaxLabel(temp[track])) -1
    #print labelIndex
    predict[track] = genres[labelIndex]

pred =[]
for key in range(len(test_keys)):
    pred.append(predict[test_keys[key]])

accuracy = accuracy_score(test_labels, pred)
print confusion_matrix(test_labels, pred)
print accuracy    


#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

from BalanceData import *
from constants import *
from sklearn.metrics import *


def getMaxLabel(prob):
    maxVal =0
    maxIndex =0
    for index in prob:
        #print index
        if prob[index] >maxVal:
            #print maxVal, prob[index]
            maxVal = prob[index]
            maxIndex = index
            #print maxVal, maxIndex

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
    #next(iterlines)
    for line in iterlines:
        split_line = line.split('\t')
        track = split_line[0]
       # print track
        #input ("wait")
        prob = {}
        for element in split_line[1:-1]:
#            print element.split(':')[0]
#            print element.split(':')[1]
            prob[element.split(':')[0]] = float(element.split(':')[1])* conf
            #print prob[element.split(':')[0]], element.split(':')[1], conf
        
        if track in temp:
            earlyProb = temp[track]
            #print earlyProb, track
            for i in prob:
                earlyProb[i] += prob[i]
                #print earlyProb[i], prob[i]
            temp[track]= earlyProb
            #print temp[track]
            
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
    
    predict[track] = genres[labelIndex]
    #print track, predict[track], labelIndex

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
result = '\n Accuracy of Combine Method = '
result+= '%f' %float(accuracy) + '\n \n'
print result

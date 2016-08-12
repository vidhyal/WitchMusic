#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import numpy as np
from sklearn import svm
from sklearn.metrics import *
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from BalanceData import *
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV


cParam = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
kernels = [ "rbf", "sigmoid"]
kFold =10


def ShuffleTrainFeatures(feats, labs):
    tempArr =  np.c_[feats.reshape(len(feats),-1), labs.reshape(len(labs), -1)]
    np.random.shuffle(tempArr)
    a2 = tempArr[:,:feats.size//len(feats)].reshape(feats.shape)
    b2 = tempArr[:,feats.size//len(feats):].reshape(labs.shape)
    
    return a2, b2


def runkFoldCrossValidation(features, labels, model):
    #scores = {}
    scores =[]
    kf = KFold(len(features), kFold	, shuffle=True)

    for k, (train, test) in enumerate(kf):
        model.C = cParam[k]
        model.fit(features[train], labels[train])
        score = model.score(features[test], labels[test])
#        print (k, model.C, score)
        scores.append(score)
    


    plt.figure(figsize=(4, 3))
    plt.semilogx(cParam, scores)
    # plot error lines showing +/- std. errors of the scores
    plt.semilogx(cParam, np.array(scores) + np.array(scores).std() / np.sqrt(len(features)),
                 'b--')
    plt.semilogx(cParam, np.array(scores) - np.array(scores).std() / np.sqrt(len(features)),
                 'b--')
    plt.ylabel('CV score')
    plt.xlabel('alpha')
    plt.axhline(np.max(scores), linestyle='--', color='.5')
    index, val = getMaxIndex(scores)
    return index
   


def runkFoldCrossValidationModel(features, labels, model):
    #scores = {}
    
    kernel_Score = []
    finModels =[]
    for kernel in kernels:
        
        model.kernel = kernel
        scores =[]
	kf = KFold(len(features), kFold	, shuffle=True)
	models = {}
        
	for k, (train, test) in enumerate(kf):
		models[k] = model
		models[k].C = cParam[k]

		models[k].fit(features[train], labels[train])
                #print "here"
		score = models[k].score(features[test], labels[test])
#		print (k, models[k].C, score)
		scores.append(score)
	index, val = getMaxIndex(scores)
        finModels.append(models[index])
        kernel_Score.append(val)
    kernelInd, Val = getMaxIndex(kernel_Score)
#    print kernel[kernelInd]
    return finModels[kernelInd], Val 
	#return models[index], val
     

def getMaxIndex(scores):
    maxVal =0
    maxIndex = 0
    for c in range(len(scores)):
      if maxVal < scores[c]:
          maxVal = scores[c]
          maxIndex = c
    print maxIndex
    return maxIndex, maxVal



rootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'SVMOut.txt'),'w+')

train_features, train_labels, test_features, test_labels, test_keys = GetData() 
train_features, train_labels = ShuffleTrainFeatures(train_features, train_labels)

<<<<<<< HEAD
model1 = svm.SVC(decision_function_shape ='ovo')
=======
model = svm.SVC(decision_function_shape ='ovr', probability=True)
>>>>>>> refs/remotes/origin/master
#c = runkFoldCrossValidation(train_features, train_labels, model)
#model, score = runkFoldCrossValidationModel(train_features, train_labels, model)
#c =0.8
#model.set_params( C = c)

gs = GridSearchCV(model1, param_grid={
    'C' :[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9],
    'kernel':['rbf','sigmoid']
       })
model = gs
model.fit(train_features, train_labels)
#print model
pred = model.predict(test_features)
predictProb = model.predict_proba(test_features)
train_acc = (model.score(train_features, train_labels))


#line = str(score) +"\n"
line = str(train_acc )+"\n"
train = ' Training Accuracy of SVM = ' + line
print train
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
result = '\n Testing Accuracy of SVM = '
result+= '%f' %float(accuracy) + '\n \n'
print result

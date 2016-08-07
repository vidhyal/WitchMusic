#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

from sklearn.feature_selection import *
from BalanceData import *
import numpy as np

def NormalizeFeatures(features, means, stdDev):
    features = features - means
    for i in range(len(stdDev)):
        if stdDev[i]==0:
            stdDev[i] = 0.000001
        print i , stdDev[i]*stdDev[i]
    features /= stdDev

    return features

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')

features, labels = LoadData('out_2.txt')
feature_list =[]
label_list =[]
for key in features:
    #print key
    feature_list.append(features[key])
    label_list.append(labels[key])
#print feature_list
X, y = np.asarray(feature_list), np.asarray(label_list)
#print X.shape, y.shape

means = np.mean(X, axis = 0)
  
stdDev = np.std(X, axis = 0)
X = NormalizeFeatures(X, means, stdDev)


#print y
#train_features, train_labels, test_features, test_labels, test_keys = GetData()
sel = VarianceThreshold(threshold=(1.0)) #SelectKBest(chi2, k=10)    #.fit_transform(feature_list, label_list)  #VarianceThreshold(threshold=(.7 * (1 - .7)))
features_aux = sel.fit_transform(X) #sel.fit_transform(X,y) #
indices = sel.get_support(True)
print indices
new_features={}
for key in features:
    feature = features[key]
    new_feature = []
    for index in indices:
        new_feature.append(feature[index])
    new_features[key] = new_feature
    



fout = open(os.path.join(newdir,'out_3.txt'), 'w+')
#labelout = open(os.path.join(newdir,'labelout.txt'), 'w+')
for key in new_features:
    line = key
    #lab = key
    feature = new_features[key]
    for s in feature:
        line+= " %f" %float(s)
    line+="\n"
    fout.write(line)

    #label = labels[key]
    #lab+= "\t" +label
    #lab+= "\n"
    #labelout.write(lab)
    #print feature, label

fout.close()


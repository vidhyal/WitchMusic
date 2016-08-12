#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

#This module normalizes the features extracted by the FeatureExtract module to belong within the range -1.0 to 1.0. From the all the features available, this module then selects only those features that have a variance higher than that denoted as parameter to the VarianceThreshold call and creates a feature file with these.
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

    feature_list.append(features[key])
    label_list.append(labels[key])

X, y = np.asarray(feature_list), np.asarray(label_list)


means = np.mean(X, axis = 0)
  
stdDev = np.std(X, axis = 0)
X = NormalizeFeatures(X, means, stdDev)


sel = VarianceThreshold(threshold=(0.9)) #SelectKBest(chi2, k=10)    #.fit_transform(feature_list, label_list)  #VarianceThreshold(threshold=(.7 * (1 - .7)))
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

for key in new_features:
    line = key
    #lab = key
    feature = new_features[key]
    for s in feature:
        line+= " %f" %float(s)
    line+="\n"
    fout.write(line)

fout.close()


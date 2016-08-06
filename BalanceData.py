#Copyright (c) 2016 Vidhya, Nandini



#This file contains methods for pre-processing data. It assumes that those and only those tracks are in the feature file whose labels have been described in the labels file.


import os
import numpy as np
import operator
from constants import *
from sklearn.preprocessing import StandardScaler
FIX_DEV = 0.00000001

#get the current working directory and reach the directory that contains the feature files and label files.

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')


# This method opens the file containing the feature vector defined by the variable "featureFile", reads the feature vector into the dictionary "features" with key being the track id. It then opens the labels file (assumed to be "labelout.txt") and creates a dictionary "labels" with the track id as key. It then returns both these dictionaries.

def LoadData(featureFile):
    data_file = open(os.path.join(newdir,featureFile),'r')
    unprocessed_data = data_file.readlines()
    labels ={}
    features ={}
    for line in unprocessed_data:
        feature_vector = []
        split_line = line.split(' ')
        for element in split_line[1:-1]:
            feature_vector.append(float(element))
        track_id = split_line[0]
        features[track_id] = feature_vector
    data_file.close()

    label_file = open(os.path.join(newdir,'labelout.txt'),'r')
    label_data = label_file.readlines()
    for line in label_data:
        split_line = line.split('\t')
        track_id = split_line[0]
        if track_id in features:
            labels[split_line[0]] = split_line[1].split('\n')[0]
    label_file.close()

    return features, labels



#This method sorts data according to the genres and splits tracks of each genre into 1/x for testing and the rest for training.
def BalanceData(features, labels):
    x = 3
   
    count =0
    genreFeat={}
    numList ={}
    testFeat = {}
    trainFeat ={}
    genreTestFeat ={}
    for genre in genres:
        delKey =[]
        feature_list =[]
        test_list =[]
        subcount=0
        for key in features:
            if labels[key] == genre:
                delKey.append(key)
                subcount=subcount+1
        fout.close()
        count = count+ subcount
        if subcount != 0:
            for key in delKey[subcount/x:]:
                trainFeat[key] = features[key]
                trainFeat[key].append(key)
                feature_list.append(trainFeat[key])
            genreFeat[genre] = feature_list
            for key in delKey[:subcount/x]:
                testFeat[key] = features[key]
                testFeat[key].append(key)
                test_list.append(testFeat[key])
            genreTestFeat[genre] = test_list

            for key in delKey:       
                del features[key]

    return genreFeat, count, genreTestFeat


#This method returns numpy arrays of the fetaures, labels and the keys for the feats dictionary passed in. This dictionary has as keys the genres and as values,a list of feature vectors whose last element is the track id.
def ConvertToArrays(feats):
    features =[]
    labels = []
    keys = []
    for genre in feats:
        for f in feats[genre]:
            features.append(f[:-1])
            keys.append(f[-1])
            labels.append(genre)
    return np.asarray(features), np.asarray(labels), np.asarray(keys)

# This method loads the data, splits the data into training and test sets and converts the training and test features, labels and keys into arrays. It then normalizes the training set and the test set using the training set features. Finally it returns the training fetaures and labels and the test fetaures, labels and keys (for use in combination step).
def GetData():
    features, labels =LoadData('out_3.txt')
    genreFeat, count, genreTestFeat = BalanceData(features, labels)
    train_features, train_labels, train_keys = ConvertToArrays(genreFeat)
    test_features, test_labels, test_keys = ConvertToArrays(genreTestFeat)
    scaler = StandardScaler()
    scaler.fit(train_features)
    train_features= scaler.transform(train_features)
    test_features = scaler.transform(test_features)
    return train_features, train_labels, test_features, test_labels, test_keys

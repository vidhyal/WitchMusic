#Copyright (c) 2016 Vidhya, Nandini

import os
import numpy as np
import operator
from constants import *
FIX_DEV = 0.00000001

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')


def LoadData():
    data_file = open(os.path.join(newdir,'out_2.txt'),'r')

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
        #print (track_id)
        if track_id in features:
            labels[split_line[0]] = split_line[1].split('\n')[0]

    label_file.close()

    for key in features:
        
        feature = features[key]
        label = labels[key]
       # print feature, label
    return features, labels

def writeToFile(key,feature,fp):
    fp1 = open(fp,'a')
    line = key
    for s in feature:
        line+= " %f" %float(s)
    line+="\n"
    fp1.write(line)

def BalanceData(features, labels):
    
    if not os.path.exists('train'):
        os.makedirs('train')
    traindir = os.path.join(rootdir,'train')
    if not os.path.exists('test'):
        os.makedirs('test')
    testdir = os.path.join(rootdir,'test')
   
    count =0
    testFile = open(os.path.join(testdir,'testFile'),'w+')
    genreFeat={}
    numList ={}
    testFeat = {}
    trainFeat ={}
    genreTestFeat ={}
    for genre in genres:
        str1 = genre+'.txt'
        fout = open(os.path.join(traindir,str1),'w+')        
        #print fout
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
        numList[genre] = subcount/2
        if subcount != 0:
            for key in delKey[:subcount/2]:
                trainFeat[key] = features[key]
                trainFeat[key].append(key)
                feature_list.append(trainFeat[key])
                #writeToFile(key, features[key], os.path.join(traindir,str1))
            genreFeat[genre] = feature_list
            for key in delKey[subcount/2:]:
                testFeat[key] = features[key]
                testFeat[key].append(key)
                test_list.append(testFeat[key])
                #writeToFile(key,features[key], os.path.join(testdir,'testFile'))
            genreTestFeat[genre] = test_list
            for key in delKey:       
                del features[key]
    return genreFeat, numList, count, genreTestFeat

def ConvertToArrays(feats):
    features =[]
    labels = []
    keys = []
    for genre in feats:
        #print genre
        for f in feats[genre]:
            features.append(f[:-1])
            keys.append(f[-1])
            #print features
            #input("press enter")
            labels.append(genre)
    return np.asarray(features), np.asarray(labels), np.asarray(keys)


def GetData():
    features, labels =LoadData()
    genreFeat,countGenre, count, genreTestFeat = BalanceData(features, labels)
    train_features, train_labels, train_keys = ConvertToArrays(genreFeat)
    test_features, test_labels, test_keys = ConvertToArrays(genreTestFeat)
    return train_features, train_labels, test_features, test_labels, test_keys

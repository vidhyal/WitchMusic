#Copyright (c) 2016 Vidhya, Nandini

import os
import numpy as np
import operator
FIX_DEV = 0.00000001

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')
genres = ['Pop_Rock', 'Electronic', 'Religious', 'Reggae', 'Country', 'Latin', 'RnB', 'Comedy_Spoken','International', 'Folk', 'Blues', 'New Age', 'Easy_Listening', 'Jazz', 'Vocal', 'Rap', 'Children']

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
    for genre in genres:
        str1 = genre+'.txt'
        fout = open(os.path.join(traindir,str1),'w+')        
        delKey =[]
        feature_list =[]
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
                feature_list.append(features[key])
            genreFeat[genre] = feature_list
            for key in delKey[subcount/2:]:
                testFeat[key] = features[key]
            for key in delKey:       
                del features[key]

    
    return genreFeat, numList, count, testFeat

def PrintToFile(means_0, name, filename):
  data_file = file(filename,'a')
  data_file.write(name+"\n")
  for s in range(len(means_0)):
    data_file.write('%18s ' %means_0[s])
  data_file.write('\n')
  data_file.close()

def gaussian(x, mu, sig):
    if sig==0:
        sig= FIX_DEV

    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def getValue(feature, means, stdDev, prob):
    value = np.log(prob)
    for s in range(len(feature)):
        value += np.log(gaussian(feature[s],means[s],stdDev[s]))
    return value
    
def TestData(features, labels, means, stdDev, prob):
    n = len(genres)

    Matrix = np.zeros(shape=(n,n)).astype('int') #(n,n)

    for key1 in features:
        val ={}
        for genre in genres:
            if prob[genre] != 0:
                val[genre] = getValue(features[key1],means[genre], stdDev[genre], prob[genre])
        jnd = genres.index(max(val.iteritems(), key=operator.itemgetter(1))[0])
        ind = genres.index(labels[key1])
        Matrix[ind][jnd] += 1
    print Matrix

def main():
    features, labels =LoadData()
    genreFeat,countGenre, count, testFeat = BalanceData(features, labels)
    mean_gn ={}
    stdDev_gn = {}
    prob ={}
    for genre in genres:
        train_feat = np.asarray(genreFeat[genre])
        mean_gn[genre] = np.mean(train_feat, axis=0)
        stdDev_gn[genre] = np.std(train_feat, axis =0)
        prob[genre]= float(countGenre[genre])/count
        
    TestData(testFeat, labels, mean_gn, stdDev_gn, prob)
    

if __name__ == "__main__":
  main()



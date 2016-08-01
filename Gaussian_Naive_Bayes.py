#Copyright (c) 2016 Vidhya, Nandini

import os
import numpy as np
import operator
from constants import *
from BalanceData import *
FIX_DEV = 0.00000001

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')




def writeToFile(key,feature,fp):
    fp1 = open(fp,'a')
    line = key
    for s in feature:
        line+= " %f" %float(s)
    line+="\n"
    fp1.write(line)

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
        #print sig
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def getValue(feature, means, stdDev, prob):
    value = np.log(prob)
    for s in range(len(feature)):
        value += np.log(gaussian(feature[s],means[s],stdDev[s]))
    return value
    
def TestData(genreFeat, means, stdDev, prob):
    n = len(genres)
    Matrix = np.zeros(shape=(n,n)).astype('int') #(n,n)
    features, labels, keys = ConvertToArrays(genreFeat)
    count =0
    for key1 in range(len(features)):
        val = {}
        for genre in genres:
            if prob[genre] != 0:
                val[genre] = getValue(features[key1],means[genre], stdDev[genre], prob[genre])
        lab = max(val.iteritems(), key=operator.itemgetter(1))[0]
        jnd = genres.index(lab)
        ind = genres.index(labels[key1])
        Matrix[ind][jnd] += 1
            
    print Matrix
    print findAccuracy(Matrix)

def findAccuracy(Matrix):
    total =0
    accurate =0
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            total +=1
            if i==j:
                accurate +=1
    return (float(float(accurate))/total)
            
            

def main():
    features, labels =LoadData()
    genreFeat,countGenre, count, genreTestFeat = BalanceData(features, labels)
    #writeProb = file("prob.txt",'w')
    mean_gn ={}
    stdDev_gn = {}
    prob ={}
    for genre in genres:
        train_feat = np.asarray(np.delete(genreFeat[genre], -1, axis=1))
        train_feat = train_feat.astype(np.float)
        #print train_feat
        #input("press enter")
        mean_gn[genre] = np.mean(train_feat, axis=0)
        #print genre, mean_gn
        stdDev_gn[genre] = np.std(train_feat, axis =0)
        #PrintToFile(mean_gn, "means_"+genre, "Gaussian_parameters.txt")
        #PrintToFile(stdDev_gn, "stdDev_"+genre, "Gaussian_parameters.txt")
        prob[genre]= float(countGenre[genre])/count
        #print prob
        #writeProb.write("genre= "+ genre+"\tcount= %5f\n" %(prob))
    #writeProb.close()
    TestData(genreTestFeat, mean_gn, stdDev_gn, prob)
    

if __name__ == "__main__":
  main()



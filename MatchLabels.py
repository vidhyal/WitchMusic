#Copyright (c) 2016 Vidhya, Nandini

import os

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')

data_file = open(os.path.join(newdir,'out_1.txt'),'r')

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


label_file = open(os.path.join(newdir,'labels.txt'),'r')
label_data = label_file.readlines()

for line in label_data:
    split_line = line.split('\t')
    track_id = split_line[0]
    #print (track_id)
    if track_id in features:
        labels[split_line[0]] = split_line[1].split('\n')[0]

delKey = []
for key in features:
    if key not in labels:
        #print key
        delKey.append(key)

for key in delKey:
    del features[key]

fout = open(os.path.join(newdir,'out_2.txt'), 'w+')
labelout = open(os.path.join(newdir,'labelout.txt'), 'w+')
for key in features:
    line = key
    lab = key
    feature = features[key]
    for s in feature:
        line+= " %f" %float(s)
    line+="\n"
    fout.write(line)

    label = labels[key]
    lab+= "\t" +label
    lab+= "\n"
    labelout.write(lab)
    #print feature, label

fout.close()
labelout.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

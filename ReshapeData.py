#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os
import operator

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'featurefiles')

genre_code = {'folk': 1, 'reggae': 2, 'punk': 3, 'metal': 4, 'classical': 5, 'electronica': 6, 'hip hop': 7, 'rock': 8, 'r&b': 9, 'pop': 10 , 'jazz' :11}

data_file = open(os.path.join(newdir,'out_2.txt'),'r')
data = data_file.readlines()
FeatureFile = open(os.path.join(newdir,'LR_FeatureFile.txt'),'w+')
for line in data:
	vector = '1.00' + '\t'
	feature_vector = []
	split_line = line.split(' ')
	track_id = split_line[0]
	for element in split_line[1:]:
		vector+= '%f' %float(element) + '\t'
	vector+= '\n'
	FeatureFile.write(vector)
FeatureFile.close()
data_file.close()

label_file = open(os.path.join(newdir,'labelout.txt'),'r')
label_data = label_file.readlines()
LabelFile = open(os.path.join(newdir,'LR_LabelFile.txt'),'w+')
for line in label_data:
	split_line = line.split('\t')
	raw_label = str(split_line[1:])
	track_label = raw_label[2:-4]
	label_code = genre_code[track_label]
	LabelFile_line = str(label_code) + '\n'
	LabelFile.write(LabelFile_line)
LabelFile.close()
label_file.close()
exit()

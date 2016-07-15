#Copyright (c) 2016 Vidhya, Nandini

import os
import h5py
import tables 

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'data')
fout = open('out2.txt', 'w+')

field_vector = ['tempo','loudness', 'danceability', 'end_of_fade_in','key_confidence','mode_confidence']

for subdir, dirs, files in os.walk(newdir):
    #print subdir
    for file in files:
        f = tables.openFile(os.path.join(subdir,file),'r')
        feature_vector =[]
	track = f.root.analysis.songs.cols.track_id[0]
        line = track
        for s in range(len(field_vector)):
            field = 'f.root.analysis.songs.cols.'+field_vector[s]+'[0]'
            line+= " %f " %(float(eval(field)))
        line+="\n"
        fout.write(line)
        f.close()
fout.close()

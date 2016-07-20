#Copyright (c) 2016 Vidhya, Nandini

import os
import h5py
import tables 

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'data')
 
if not os.path.exists('featurefiles'):
    os.makedirs('featurefiles')
outdir = os.path.join(rootdir,'featurefiles')
fout = open(os.path.join(outdir,'label_1.txt'), 'w+')


genres = ['electronica', 'hip hop','rock', 'r&b', 'pop','jazz']

for subdir, dirs, files in os.walk(newdir):

    for file in files:
        f = tables.openFile(os.path.join(subdir,file),'r')
        track = f.root.analysis.songs.cols.track_id[0]
        line = track
        freq = f.root.metadata.artist_terms_freq
        genre = f.root.metadata.artist_terms
        max = 0 
        maxNum = 0
        
        if len(freq)>0:
            for s in range(len(freq)):
                if (max < freq[s] and (genre[s] in genres)):
                    max = freq[s]
                    maxNum =s
            if genre[maxNum] in genres:
                line+= '\t'+f.root.metadata.artist_terms[maxNum]
                line+="\n"
                fout.write(line)
        f.close()
fout.close()

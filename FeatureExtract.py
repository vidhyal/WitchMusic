#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.


#This file extracts features for each track (in the format of hdf5 files) in the recursive subdirectories of teh directory "data". 
import os
import h5py
import tables
import numpy as np 

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'data')

#define the destination file to store fetaure vectors

if not os.path.exists('featurefiles'):
    os.makedirs('featurefiles')
outdir = os.path.join(rootdir,'featurefiles')
fout = open(os.path.join(outdir,'out_1.txt'), 'w+')

#The fields to be selected from the data files available.
field_vector = ['tempo','loudness', 'danceability', 'end_of_fade_in','key_confidence','mode_confidence']
TIMBRE = True
BEATS = False # This is because not all of teh tracks had this feature defined and this resulted in an exception
PITCHES = True
SEGLOUD = True #False


# This method returns 2 features per column of the feature denoted by field, i.e. the average and variance of the feature along that column.
def getFieldLine(f, field, line):
    vals = eval('f.root.analysis.' +field)
    vals = np.asarray(vals)
    if not vals.size:
        print "empty array"
    for k in np.average(vals, axis=0):
	line += " %f" %float(k)
    for k in np.var(vals, axis=0):
	line += " %f" %float(k)
    #print timbre
    #input ("wait")
    return line

#This method returns the same as the getFieldLine method but for features that have just one column
def getField(f, field):
    vals = eval('f.root.analysis.' +field)
    vals = np.asarray(vals)
    return np.average(vals, axis=0), np.var(vals, axis=0, ddof=0.000001)

#This is the main method of this python file. It recurses through all the subdirectories of the data directory, opens each of teh data file, extracts features from that fiel, writes the feature vector to an output file and closes the data file.
for subdir, dirs, files in os.walk(newdir):
    #print subdir
    for file in files:
        f = tables.openFile(os.path.join(subdir,file),'r')
   	feature_vector =[]
	track = f.root.analysis.songs.cols.track_id[0]
        line = track
        for s in range(len(field_vector)):
            field = 'f.root.analysis.songs.cols.'+field_vector[s]+'[0]'
            line+= " %f" %(float(eval(field)))
        if TIMBRE:
                line = getFieldLine(f, 'segments_timbre', line)
        if BEATS:
            beats_av, beats_var = getField(f, 'beats_confidence')
            line += " %f" %float(beats_av)
            line += " %f" %float(beats_var)
        if PITCHES:
            line = getFieldLine(f, 'segments_pitches', line)
        if SEGLOUD:
            beats_av, beats_var = getField(f, 'segments_loudness_max')
            line += " %f" %float(beats_av)
            line += " %f" %float(beats_var)
        line+="\n"
        fout.write(line)
        f.close()
fout.close()


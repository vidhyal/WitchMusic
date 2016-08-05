#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os
import h5py
import tables
import numpy as np 

rootdir = os.getcwd()
newdir = os.path.join(rootdir,'data')
 
if not os.path.exists('featurefiles'):
    os.makedirs('featurefiles')
outdir = os.path.join(rootdir,'featurefiles')
fout = open(os.path.join(outdir,'out_1.txt'), 'w+')

field_vector = ['tempo','loudness', 'danceability', 'end_of_fade_in','key','mode', 'time_signature']
TIMBRE = True
BEATS = False #True
PITCHES = True
SEGLOUD = True #False

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

def getField(f, field):
    beats = eval('f.root.analysis.' +field)
    beats = np.asarray(beats)
    return np.average(beats, axis=0), np.var(beats, axis=0, ddof=0.000001)

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
		#timbre = getTimbre(f)
		#for k in np.average(timbre, axis=0):
		 #   line += " %f" %float(k)
		#for k in np.var(timbre, axis=0):
		 #   line += " %f" %float(k)
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


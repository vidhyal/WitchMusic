Copyright (c) 2016 Vidhya, Nandini

# WitchMusic
Music Genre Classification. Implementation of various machine learning algorithms to predict the genre of a given music track.

## Contributors:
Nandini Khanwalkar

Email: nandini2@pdx.edu

Vidhya Lakshmi Venkatarama

Email: vidhyal@pdx.edu

## License
The MIT License. See the LICENSE file for details.

## Dataset

MSD dataset: http://labrosa.ee.columbia.edu/millionsong/

##Approach

Machine Learning

## Work Environment

Ubuntu 16.04

# About WitchMusic

In this project, we have implemented multiple machine learning algorithms, such as Gaussian Naive Bayes, Logistic Reggression, Support Vector Machines and Neural Networks, to predict the genre of a given soundtrack. The dataset we used for this is The Million Song Dataset, which is a freely-available collection of audio features and metadata for a million contemporary popular music tracks. This dataset is provided by The Echo Nest and contains the feature analysis and metadata for the songs. The dataset does not contain any audio tracks but only the derived features from each track. The dataset can be downloaded from http://labrosa.ee.columbia.edu/millionsong/ or by clicking [here](http://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset). However, for the purpose of this project we'd be using a subset of this dataset consisting of 10,000 songs, which can also be downloaded from the above webpage or by clicking [here](http://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset#subset).

If you'd like to check out the results, follow the instructions given below :-

1. Make sure your system has all of the following software/packages required and enough disk space -

	a. Python 2.7.11

	b. Python packages: pytables, h5py, scipy, numpy, scikit-learn, scikit-neuralnetwork, python-matplotlib

2. Extract the folder "data" from the dataset and store it in the current working directory

3. Download this project, extract all the files in your current working directory

4. Execute the file AutoRun.py

## How it works :
The AutoRun starts with executing the 'FeatureExtract' which opens each of the h5 files and extracts required features and saves them, corresponding to their track id, in a text file. 'Labelling' extracts the genre labels of the tracks and stores them in another file. 'MatchLabels', 'ReshapeData' and 'Feature_Selection' preprocess the data to fit the machine learning models. Afterwards the aforementioned algorithms are implemented to train the models and test them against a set of track features. The output tells the accuracy of each implemented model.

##Bibliography

http://www.tagtraum.com/msd_genre_datasets.html

http://www.ee.columbia.edu/~dliang/files/FINAL.pdf

http://www.tagtraum.com/download/schreiber_msdgenre_ismir2015.pdf

##References

http://openclassroom.stanford.edu/MainFolder/CoursePage.php?course=MachineLearning

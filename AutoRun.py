#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

import os

os.system("python FeatureExtract.py")
os.system("python Labelling.py")
os.system("python MatchLabels.py")
os.system("python Feature_Selection.py")
os.system("python GaussianScikit.py")
os.system("python LogisticRegression.py")
os.system("python DecisionTree.py")
os.system("python SVM.py")
os.system("python NeuralNets.py")
os.system("python Combine.py")

exit()

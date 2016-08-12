#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.


#This file implements the scikit version of Multi Layer Perceptron classifier for our data set. It calls the GetData function of the BalanceData module to obtain the training features and labels and testing features, labels and keys. Then it does a grid search on the testing data to obtain optimum paramters for the training data using cross validation. It then calls the fit method on the Multi Layer Perceptron to fit the classifier to the training features and labels available. The test features are tested on the fitted model to predict the labels for test features which are later used to obtain the test accuracy and confusion matrix. This module also calls the predict_proba method of the model to get per track, the probability of it being in a particular class. This predicted probability per track is stored in teh file NeuralNetsOut which shall be later be used by the combine method.  
#This implementation ues only 1 hidden layer

from sknn.mlp import MultiLayerPerceptron, Classifier, Layer
from BalanceData import *
from constants import *
from sklearn.metrics import *
from sklearn.grid_search import GridSearchCV




eta = 0.001
iters =45

rootdir = os.getcwd()
if not os.path.exists('sklearnTry'):
        os.makedirs('sklearnTry')
newdir = os.path.join(rootdir,'sklearnTry')
fout = open(os.path.join(newdir,'NeuralNetsOut.txt'),'w+')


train_features, train_labels, test_features, test_labels, test_keys = GetData()

model = Classifier(layers=[Layer("Sigmoid", units=50), Layer("Softmax")], learning_rate = eta, n_iter = iters, weight_decay = 0.00001, warning = None) #MPLClassifier(alpha = 1e-05, hidden_layer_sizes= (15,), epsilon = 1e-08)

gs = GridSearchCV(model, param_grid={
    'learning_rate': [ 0.005, 0.001, 0.0002],
    'hidden0__units': [8, 25, 40, 45, 50],
    'hidden0__type': ["Rectifier", "Sigmoid", "Tanh", "ExpLin"],
    'weight_decay':[0.00001, 0.001, 0.0001],
    'output__type':["Sigmoid", "Softmax"]
       })
gs.fit(train_features, train_labels)
pred = gs.predict(test_features)
predictProb = gs.predict_proba(test_features)

train_acc = (gs.score(train_features, train_labels))
line = str(train_acc )+"\n"
train = ' Training Accuracy of Neural Network = ' + line
print train
fout.write(line)


for key in range(len(test_keys)):
    line = test_keys[key]+"\t"
    for f in range(len(predictProb[key])):
      line +="%i:%f\t" % (f+1 , predictProb[key][f])
    line += "\n"
    fout.write(line)
fout.close()
    
    
accuracy = accuracy_score(test_labels, pred)
print confusion_matrix(test_labels, pred)
result = '\n Testing Accuracy of Neural Network  = '
result+= '%f' %float(accuracy) + '\n \n'
print result


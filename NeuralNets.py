#Copyright (c) 2016 Vidhya, Nandini
#Following code is available for use under MIT license. Please see the LICENSE file for details.

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

#means = np.mean(train_features, axis = 0)
  
#stdDev = np.std(train_features, axis = 0)
#train_features = NormalizeFeatures(train_features, means, stdDev)
#test_features = NormalizeFeatures(test_features, means, stdDev)


model = Classifier(layers=[Layer("Sigmoid", units=50), Layer("Softmax")], learning_rate = eta, n_iter = iters, weight_decay = 0.00001, warning = None) #MPLClassifier(alpha = 1e-05, hidden_layer_sizes= (15,), epsilon = 1e-08)

gs = model
gs.fit(train_features, train_labels)
pred = gs.predict(test_features)
predictProb = gs.predict_proba(test_features)

train_acc = (gs.score(train_features, train_labels))
line = str(train_acc )+"\n"
#print train_acc
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
result = '\n Accuracy of NeuralNets = '
result+= '%f' %float(accuracy) + '\n \n'
print result


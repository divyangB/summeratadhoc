#!/usr/bin/python3

import time
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

#loading iris data
iris=load_iris()
#dir(iris)

fl_names= iris.target_names

#print features of iris

fl_features= iris.feature_names

#loading flower features data

fl_feature_data= iris.data

#print(fl_feature_data)

iris.target

setosa=iris.target[0:50]
versicolor= iris.target[51:100]
virginia= iris.target[101:150]


#training data
train_setosa= setosa[0:49]
train_versi=versicolor[101:149]
train_virgin= virginia[51:99]


#test data
test_setosa= setosa[50]
test_virgin= virginia[100]
test_versi=versicolor[150]





#training dataset
x= [[0],[1],[2]]
output= ["setosa","versi","virginia"]

algo1 = tree.DecisionTreeClassifier()
algo2 = tree.DecisionTreeClassifier()
algo3 = tree.DecisionTreeClassifier()


trained=algo.fit(x,output)

#now predicting

final= trained.predict([0])

#train_setosa.size
'''
#plotting total 
plt.xlabel("Setosa")
plt.ylabel("Versicolor")
plt.title("IRIS flowers")
x1= fl_feature_data[0:50]
y1= fl_feature_data[50:100]
z1= fl_feature_data[100:]

plt.scatter(x1,y1,label="setosa_versi",marker="o")
plt.scatter(z1,x1,label="virgin_setosa",marker="*")
plt.scatter(y1,z1,label="ver_virgin",marker="x")
plt.legend()
plt.show()
'''

print(final)
plt.scatter(x,y)
plt.show()

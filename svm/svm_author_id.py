#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(kernel="rbf",C=10000.0)
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test,pred)
print(acc)
print("10th: ", pred[10])
print("26th: ",  pred[26])
print("50th: ",  pred[50])
count = 0
for i in range(1,1700):
	if pred[i] == 1:
		count+=1
print count
#########################################################




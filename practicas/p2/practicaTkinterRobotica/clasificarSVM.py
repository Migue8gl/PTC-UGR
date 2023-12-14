#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:55:07 2023

@author: migue8gl
"""

import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=DeprecationWarning)


def scale_data(data):
    means = np.average(data, axis=0)
    std_deviations = np.std(data, axis=0)
    return (data - means) / std_deviations


def read_data(dataset):
    return pd.read_csv(dataset)


def split_data(data):
    x = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return x, y


def train_test_split_data(x, y):
    return train_test_split(x, y, test_size=0.2, random_state=25)


def train_classifier(x_train, y_train, x_test, y_test, kernel):
    svc = SVC(kernel=kernel)
    svc.fit(x_train, y_train)
    return svc.predict(x_test), svc


def evaluate_classifier(y_true, y_pred):
    acc_test = accuracy_score(y_true, y_pred)
    print("Acc_test: (TP+TN)/(T+P)  %0.4f" % acc_test)
    print("Matriz de confusión Filas: verdad Columnas: predicción")
    print(confusion_matrix(y_true, y_pred))
    print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
    print("f1-score es la media entre precisión y recall")
    print(classification_report(y_true, y_pred))


def cross_validate_classifier(clf, x, y):
    scores = cross_val_score(clf, x, y, cv=5)
    print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" %
          (scores.mean(), scores.std() * 2))
    print('\n#----------------------------------------------#\n')


def train(dataset):
    with open('training_results', 'w') as file:
        sys.stdout = file
        data = read_data(dataset)
        x, y = split_data(data)
        x_scaled = scale_data(x)

        for i, data in enumerate([x, x_scaled]):
            if i == 0:
                print('\n------ DATOS SIN ESCALAR ------\n')
            else:
                print('\n------ DATOS ESCALADOS ------\n')
            x_train, x_test, y_train, y_test = train_test_split_data(data, y)

            # Linear SVM
            print("Clasificación con kernel Lineal")
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'linear')
            evaluate_classifier(y_test, y_pred)
            cross_validate_classifier(svc, x_scaled, y)

            # Linear SVM
            print("Clasificación con kernel Polinómico")
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'poly')
            evaluate_classifier(y_test, y_pred)
            cross_validate_classifier(svc, x_scaled, y)

            # Linear SVM
            print("Clasificación con kernel RBF")
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'rbf')
            evaluate_classifier(y_test, y_pred)
            cross_validate_classifier(svc, x_scaled, y)
        sys.stdout = sys.__stdout__

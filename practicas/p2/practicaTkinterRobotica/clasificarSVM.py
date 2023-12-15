#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:55:07 2023

@author: migue8gl
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
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
    feature_names = ['perimeter', 'depth', 'width', 'class']
    return pd.read_csv(dataset, names=feature_names)


def split_data(data):
    x = data.drop('class', axis=1)
    y = data['class']
    return x, y


def train_test_split_data(x, y):
    return train_test_split(x, y, test_size=0.2, random_state=25)


def train_classifier_hyperparameter_search(x_train, y_train, x_test, y_test, kernel, params):
    # Busqueda de parámetros
    svc = SVC(kernel=kernel)
    svc.fit(x_train, y_train)

    # Parámetros a combinar
    param_grid = params

    clf = GridSearchCV(SVC(kernel=kernel, class_weight="balanced"), param_grid)
    clf = clf.fit(x_train, y_train)
    print("Mejor estimador encontrado")
    print(clf.best_estimator_)

    best_svc = clf.best_estimator_
    return best_svc.predict(x_test), best_svc


def train_classifier(x_train, y_train, x_test, y_test, kernel):
    svc = SVC(kernel=kernel)
    svc.fit(x_train, y_train)
    return svc.predict(x_test), svc


def evaluate_classifier(y_true, y_pred):
    acc_test = accuracy_score(y_true, y_pred)
    message = f"Acc_test: (TP+TN)/(T+P)  %0.4f\n" % acc_test
    message += "Matriz de confusión Filas: verdad Columnas: predicción\n"
    message += f"{confusion_matrix(y_true, y_pred)}\n"
    message += "Precision= TP / (TP + FP), Recall= TP / (TP + FN)\n"
    message += "f1-score es la media entre precisión y recall\n"
    message += f"{classification_report(y_true, y_pred)}\n"
    return message


def cross_validate_classifier(clf, x, y):
    scores = cross_val_score(clf, x, y, cv=5)
    message = f"Accuracy 5-cross validation: %0.4f (+/- %0.4f)\n" % (
        scores.mean(), scores.std() * 2)
    message += '#----------------------------------------------#\n'
    return message


def train(dataset):
    message = ""
    with open('training_results', 'w') as file:
        data = read_data(dataset)
        x, y = split_data(data)
        x_scaled = scale_data(x)

        for i, data in enumerate([x, x_scaled]):
            if i == 0:
                message += '\n------ DATOS SIN ESCALAR ------\n'
            else:
                message += '\n------ DATOS ESCALADOS ------\n'
            x_train, x_test, y_train, y_test = train_test_split_data(data, y)

            # Linear SVM
            message += "Clasificación con kernel Lineal\n"
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'linear')
            message += evaluate_classifier(y_test, y_pred)
            message += cross_validate_classifier(svc, data, y)

            # Polinomico SVM
            message += "Clasificación con kernel Polinómico\n"
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'poly')
            message += evaluate_classifier(y_test, y_pred)
            message += cross_validate_classifier(svc, data, y)

            # Radial SVM
            message += "Clasificación con kernel RBF\n"
            y_pred, svc = train_classifier(
                x_train, y_train, x_test, y_test, 'rbf')
            message += evaluate_classifier(y_test, y_pred)
            message += cross_validate_classifier(svc, data, y)

            # El mejor kernel es el de RBF, por lo que hacemos búsqueda de hiperparámetros
            # para ese kernel
            params = {'C': [1, 10, 100, 1000],
                      'gamma': [0.001, 0.005, 0.01, 0.1]}

            message += 'Búsqueda de hiperparámetros para SVM con RBF\n'
            y_pred, best_svc = train_classifier_hyperparameter_search(
                x_train, y_train, x_test, y_test, 'rbf', params)
            message += evaluate_classifier(y_test, y_pred)
            message += cross_validate_classifier(best_svc, data, y)

        # Guardamos el último clasificador (que es el SVM-RBF con búsqueda
        # de hiperparámetros)
        with open("clasificador.pkl", "wb") as archivo:
            pickle.dump(best_svc, archivo)
        file.write(message)

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
from sklearn.model_selection import cross_val_score, GridSearchCV
import pickle
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=DeprecationWarning)


def scale_data(data):
    means = np.average(data, axis=0)
    std_deviations = np.std(data, axis=0)

    with open("scaling_params.pkl", "wb") as params_file:
        pickle.dump(
            {'means': means, 'std_deviations': std_deviations}, params_file)
    return (data - means) / std_deviations


def read_data(dataset):
    feature_names = ['perimeter', 'depth', 'width', 'class']
    return pd.read_csv(dataset, names=feature_names)


def split_data(data):
    x = data.drop('class', axis=1)
    y = data['class']
    return x, y


def train_test_split_data(x, y):
    return train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


def train_classifier(x_train, y_train, x_test, kernel, params=None):
    if params is None:
        svc = SVC(kernel=kernel)
    else:
        clf = GridSearchCV(SVC(kernel=kernel), params)
        clf = clf.fit(x_train, y_train)
        print("Mejor estimador encontrado")
        print(clf.best_estimator_)
        svc = clf.best_estimator_

    svc.fit(x_train, y_train)
    return svc.predict(x_test), svc


def evaluate_classifier(y_true, y_pred):
    acc_test = accuracy_score(y_true, y_pred)
    message = "Acc_test: (TP+TN)/(T+P)  %0.4f\n" % acc_test
    message += "Matriz de confusión Filas: verdad Columnas: predicción\n"
    message += f"{confusion_matrix(y_true, y_pred)}\n"
    message += "Precision= TP / (TP + FP), Recall= TP / (TP + FN)\n"
    message += "f1-score es la media entre precisión y recall\n"
    message += f"{classification_report(y_true, y_pred)}\n"
    return message


def cross_validate_classifier(clf, x, y):
    scores = cross_val_score(clf, x, y, cv=5)
    message = "Accuracy 5-cross validation: %0.4f (+/- %0.4f)\n" % (
        scores.mean(), scores.std() * 2)
    message += '#----------------------------------------------#\n'
    return message, scores.mean()


def train(dataset):
    message = ""
    with open('training_results', 'w') as file:
        data = read_data(dataset)
        x, y = split_data(data)
        x_scaled = scale_data(x)

        for i, data in enumerate([x, x_scaled]):
            if i == 0:
                message += '\n------------ DATOS SIN ESCALAR ------------\n\n'
            else:
                message += '\n------------ DATOS ESCALADOS ------------\n\n'
            x_train, x_test, y_train, y_test = train_test_split(
                data, y, stratify=y)

            kernels = ['linear', 'poly', 'rbf']
            params = {
                'rbf': {'C': [0.1, 1, 10, 100, 1000], 'gamma': [0.001, 0.005, 0.01, 0.1]},
                'linear': {'C': [0.1, 1, 10, 100, 1000]},
                'poly': {'C': [0.1, 1, 10], 'degree': [2, 3]}
            }
            
            best_score = 0

            for kernel in kernels:
                message += f"Clasificación con kernel {kernel}\n"

                y_pred, svc = train_classifier(
                    x_train, y_train, x_test, kernel, params[kernel])
                message += evaluate_classifier(y_test, y_pred)
                msg, score = cross_validate_classifier(svc, data, y)
                message += msg
                
                # Guardamos el mejor clasificador
                if score > best_score:
                    best_score = score
                    best_svc = svc
                    last_msg = '\nMEJOR CLASIFICADOR: {}'.format(kernel)

        # Guardamos el último clasificador
        with open("clasificador.pkl", "wb") as archivo:
            pickle.dump(best_svc, archivo)
        message += last_msg
        file.write(message)

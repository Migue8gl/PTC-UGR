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


def train_classifier(dataset):
    with open('train_classifier_output.txt', 'w') as file:
        # Redirigimos todos los outputs a una salida para leerlos cómodamente
        sys.stdout = file
        # Leemos el csv con los datos en forma de dataframe
        data = pd.read_csv(dataset)

        # Separamos las características de la etiqueta que nos dices a la clase que corresponde
        x = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        
        medias = np.average(x, axis=0) # Media de cada característica
        desv_tipicas = np.std(x, axis=0) # Desviación típica de cada característica
        x = (x - medias) / desv_tipicas # dataset normalizado

        # Dividimos en conjuntos de entrenamiento y de test
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=25)

        print("Clasificación con kernek Lineal")
        svcLineal = SVC(kernel='linear')
        svcLineal.fit(x_train, y_train)

        # Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial
        y_pred = svcLineal.predict(x_test)
        acc_test = accuracy_score(y_test, y_pred)

        print("Acc_test Lineal: (TP+TN)/(T+P)  %0.4f" % acc_test)
        print("Matriz de confusión Filas: verdad Columnas: predicción")
        print(confusion_matrix(y_test, y_pred))
        print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
        print("f1-score es la media entre precisión y recall")
        print(classification_report(y_test, y_pred))

        # Para asegurarnos de que el resultado no depende del conjunto de test elegido
        # tenemos que realizar validación cruzada

        svcLineal2 = SVC(kernel='linear')
        scores = cross_val_score(svcLineal2, x, y, cv=5)

        # Exactitud media con intervalo de confianza del 95%
        print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" %
              (scores.mean(), scores.std() * 2))
        print('\n#----------------------------------------------#\n')

        # ----------------------------------------------------------------------- #

        grado = 3

        print("Clasificación con kernek polinomico de grado ", grado)
        svcPol = SVC(kernel='poly', degree=grado)
        svcPol.fit(x_train, y_train)

        # Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial
        y_pred = svcPol.predict(x_test)
        acc_test = accuracy_score(y_test, y_pred)

        print("Acc_test Polinomico: (TP+TN)/(T+P)  %0.4f" % acc_test)
        print("Matriz de confusión Filas: verdad Columnas: predicción")
        print(confusion_matrix(y_test, y_pred))
        print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
        print("f1-score es la media entre precisión y recall")
        print(classification_report(y_test, y_pred))

        # Para asegurarnos de que el resultado no depende del conjunto de test elegido
        # tenemos que realizar validación cruzada

        svcPol2 = SVC(kernel='poly', degree=grado)
        scores = cross_val_score(svcPol2, x, y, cv=5)

        # Exactitud media con intervalo de confianza del 95%
        print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" %
              (scores.mean(), scores.std() * 2))
        print('\n#----------------------------------------------#\n')

        # ----------------------------------------------------------------------- #

        print("Clasificación con kernek de base radial con C=1 y gamma=auto")

        svcRBF = SVC(kernel='rbf', gamma='auto')
        svcRBF.fit(x_train, y_train)

        # Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial
        y_pred = svcRBF.predict(x_test)
        acc_test = accuracy_score(y_test, y_pred)

        print("Acc_test Polinomico: (TP+TN)/(T+P)  %0.4f" % acc_test)
        print("Matriz de confusión Filas: verdad Columnas: predicción")
        print(confusion_matrix(y_test, y_pred))
        print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
        print("f1-score es la media entre precisión y recall")
        print(classification_report(y_test, y_pred))

        # Para asegurarnos de que el resultado no depende del conjunto de test elegido
        # tenemos que realizar validación cruzada

        svcRBF2 = SVC(kernel='rbf', gamma='auto')
        scores = cross_val_score(svcRBF2, x, y, cv=5)

        # Exactitud media con intervalo de confianza del 95%
        print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" %
              (scores.mean(), scores.std() * 2))
        print('\n#----------------------------------------------#\n')
    sys.stdout = sys.__stdout__

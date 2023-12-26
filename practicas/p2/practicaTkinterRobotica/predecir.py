import time
import vrep
import pickle
import pandas as pd
from agrupar import create_clusters
from caracteristicas import depth, width, perimeter
import matplotlib.pyplot as plt


def read_laser_data(clientID):
    """
    Lee los datos del láser desde V-REP.

    Parámetros:
    - clientID: Identificador de cliente para la conexión con V-REP.

    Devuelve:
    - Lista de listas que contiene las coordenadas (x, y) de los puntos detectados por el láser.
    """
    # Acceder a los datos del láser
    _, datosLaserComp = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_streaming)

    # Tiempo para leer los datos (se llena el buffer)
    time.sleep(1)
    seconds = 0.5

    # Listas para recibir las coordenadas (x y z) de los puntos detectados por el láser
    puntos_x = []
    puntos_y = []
    puntos_z = []

    _, signal_value = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_buffer)
    time.sleep(seconds)

    datos_laser = vrep.simxUnpackFloats(signal_value)
    for indice in range(0, len(datos_laser), 3):
        puntos_x.append(datos_laser[indice+1])
        puntos_y.append(datos_laser[indice+2])
        puntos_z.append(datos_laser[indice])

    # Retornamos los valores leídos
    return [[puntos_x, puntos_y]]


def generate_features(clusters):
    """
    Genera características (features) a partir de los clusters.

    Parámetros:
    - clusters: Lista de clusters.

    Devuelve:
    - Lista de listas con características para cada cluster.
    """
    features = []
    for cluster in clusters:
        features_cluster = [perimeter(cluster), depth(cluster), width(cluster)]
        features.append(features_cluster)
    return features


def predict_data(data):
    """
    Realiza predicciones utilizando un clasificador previamente entrenado.

    Parámetros:
    - data: Datos a predecir.

    Devuelve:
    - Predicciones.
    """
    # Pasamos a DataFrame
    feature_names = ['perimeter', 'depth', 'width']
    df = pd.DataFrame(data, columns=feature_names)
    
    with open('scaling_params.pkl', 'rb') as params_file:
        scaling_params = pickle.load(params_file)
        means = scaling_params['means']
        std_deviations = scaling_params['std_deviations']
        
    data = (df - means) / std_deviations

    # Cargamos el clasificador
    with open('clasificador.pkl', 'rb') as file:
        classifier = pickle.load(file)
        predictions = classifier.predict(data)
    return predictions


def visualize_clusters(clusters, predictions, plot_name='prediccion/Predictions'):
    """
    Visualiza los clusters y sus predicciones.

    Parámetros:
    - clusters: Lista de clusters.
    - predictions: Predicciones asociadas a cada cluster.
    - plot_name: Nombre del archivo de la visualización (opcional).
    """
    plt.figure(figsize=(7, 5))
    for i, cluster in enumerate(clusters):
        color = 'red' if predictions[i] == 1 else 'blue'
        cluster_x, cluster_y = zip(*cluster)
        plt.scatter(cluster_x, cluster_y, c=color, s=10)

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Visualización de Clusters')
    plt.savefig(plot_name)


def predict(clientID, parameters):
    """
    Realiza la predicción de clusters utilizando datos del láser y visualiza los resultados.

    Parámetros:
    - clientID: Identificador de cliente para la conexión con V-REP.
    - parameters: Parámetros de agrupamiento.

    No devuelve nada, pero guarda una visualización de los clusters con las predicciones.
    """
    # Leemos los datos del láser
    data = read_laser_data(clientID)

    # Creamos los clusters
    clusters = create_clusters(data, parameters.get_min_points(),
                               parameters.get_max_points(), parameters.get_distance_threshold())

    # Obtenemos características por cada cluster
    data = generate_features(clusters)

    # Hacemos las predicciones
    predictions = predict_data(data)

    # Ploteamos las predicciones
    visualize_clusters(clusters, predictions)

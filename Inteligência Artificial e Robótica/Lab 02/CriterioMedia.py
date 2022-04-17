import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff


def criterio_media():
    data, meta = arff.loadarff('./CriterioMedia.arff')

    attributes = meta.names()
    data_value = np.asarray(data)

    percFalta = np.asarray(data['PercFalta']).reshape(-1, 1)
    notas = np.asarray(data['Nota']).reshape(-1, 1)
    features = np.concatenate((notas, percFalta), axis=1)
    target = data['resultado']

    Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

    plt.figure(figsize=(10, 6.5))
    tree.plot_tree(Arvore, feature_names=['Notas', 'PercFalta'], class_names=['Aprovado', 'Reprovado'],
                   filled=True, rounded=True)
    plt.show()

    fig, ax = plt.subplots(figsize=(25, 10))
    metrics.plot_confusion_matrix(Arvore, features, target, display_labels=['Aprovado', 'Reprovado'], values_format='d',
                                  ax=ax)
    plt.show()

criterio_media()
from sklearn import datasets
from sklearn.model_selection import train_test_split
#- Es la clase de Máquinas de Vector de Soporte de scikit-learn.
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Cargar conjunto de datos
iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target  # Usamos solo las dos primeras características para visualización

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar modelo SVM
svm_model = SVC(kernel='linear', C=1)
#Mediante el kernel nos ayuda a separar, es usado para los vectores
svm_model.fit(X_train, y_train)

# Predicción y evaluación
accuracy = svm_model.score(X_test, y_test)
print(f'Precisión del modelo: {accuracy:.2f}')

# Visualizar el límite de decisión
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    #(meshgrid) que cubren el espacio de características.
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.3)
    #Asigna colores a los puntos según su categoría
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.title('SVM - Límite de decisión')
    plt.show()

plot_decision_boundary(svm_model, X_train, y_train)

#Estas maquinas vectores sirven para predecir y entenar un modelo que tiene la ayuda de la libreria matplor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir en conjunto de entrenamiento y prueba
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, test_size=0.2, random_state=1)

# Crear el modelo ensemble con Random Forest
bosque = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=3, random_state=1)
bosque.fit(X_ent, y_ent)

# Evaluación del modelo
print("Precisión en conjunto de entrenamiento: {:.2f}".format(bosque.score(X_ent, y_ent)))
print("Precisión en conjunto de prueba: {:.2f}".format(bosque.score(X_pru, y_pru)))

# Identificar características más importantes
importantes = bosque.feature_importances_
indices = np.argsort(importantes)[::-1]
nombres = [iris.feature_names[i] for i in indices]

# Visualización de importancia de características
plt.title("Importancia de Características - Random Forest")
plt.bar(range(X.shape[1]), importantes[indices])
plt.xticks(range(X.shape[1]), nombres, rotation=90)
plt.show()


plt.title("Importancia de Características - Random Forest")
plt.bar(range(X.shape[1]), importantes[indices])
plt.xticks(range(X.shape[1]), nombres, rotation=90)

# Agregar precisión del modelo como texto en la gráfica
plt.text(0.5, max(importantes), f'Precisión entrenamiento: {bosque.score(X_ent, y_ent):.2f}', fontsize=12, color='red')
plt.text(0.5, max(importantes) * 0.9, f'Precisión prueba: {bosque.score(X_pru, y_pru):.2f}', fontsize=12, color='blue')

plt.show()
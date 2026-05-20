import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Cargar el conjunto de datos de ejemplo (Iris)
data = load_iris()
X = data.data
y = data.target

# Aplicar PCA y reducir a 2 component es principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Graficar los resultados
plt.figure(figsize=(8, 6))
for i, label in enumerate(data.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=label)

plt.xlabel("Primer Componente Principal")
plt.ylabel("Segundo Componente Principal")
plt.title("Análisis de Componentes Principales (PCA)")
plt.legend()
plt.grid()
plt.show()
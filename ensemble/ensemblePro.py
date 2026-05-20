from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir en conjunto de entrenamiento y prueba
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, test_size=0.2, random_state=1)

# Modelos individuales
clf1 = LogisticRegression(max_iter=200, random_state=1)
clf2 = DecisionTreeClassifier(random_state=1)
clf3 = SVC(probability=True, random_state=1)
clf4 = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, random_state=1)

# Entrenar clf4 antes de acceder a feature_importances_
clf4.fit(X_ent, y_ent)  # <- Agrega esta línea aquí

importantes = clf4.feature_importances_
indices = np.argsort(importantes)[::-1]
nombres = [iris.feature_names[i] for i in indices]

# Crear ensemble con VotingClassifier
ensemble = VotingClassifier(estimators=[
    ('lr', clf1), 
    ('dt', clf2), 
    ('svc', clf3),
    ('rf', clf4)  # Se incorpora el Random Forest
], voting='soft')

# Entrenar ensemble
ensemble.fit(X_ent, y_ent)

# Evaluación del modelo
y_pred = ensemble.predict(X_pru)
print("Precisión del ensemble:", accuracy_score(y_pru, y_pred))

# Identificar características más importantes desde Random Forest
importantes = clf4.feature_importances_
indices = np.argsort(importantes)[::-1]
nombres = [iris.feature_names[i] for i in indices]

# Visualización de importancia de características
plt.title("Importancia de Características - Random Forest dentro del Ensemble")
plt.bar(range(X.shape[1]), importantes[indices])
plt.xticks(range(X.shape[1]), nombres, rotation=90)

# Agregar precisión del modelo como texto en la gráfica
plt.text(0.5, max(importantes), f'Precisión ensemble: {accuracy_score(y_pru, y_pred):.2f}', fontsize=12, color='red')

plt.show()


print(clf4)
print(hasattr(clf4, "feature_importances_"))
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


df = pd.read_csv("D:\\kobe-\\Documents\\8A ISC\\Mineria de datos\\alimentos (5).csv")

# 2. Definir las variables predictoras (X) y la variable objetivo (y)
X = df.drop("Precio_Alimento", axis=1)  # Precio_Alimento como predictor
y = df["Id_tipo_alim"]  # Variable objetivo (1 = bebida, 2 = platillo)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


modelo = DecisionTreeClassifier(criterion='gini', max_depth=3)
modelo.fit(X_train, y_train)


print("Precisión en el conjunto de entrenamiento: {:.2f}".format(modelo.score(X_train, y_train)))
print("Precisión en el conjunto de prueba: {:.2f}".format(modelo.score(X_test, y_test)))

plt.figure(figsize=(12, 8))
plot_tree(modelo, 
          feature_names=X.columns, 
          class_names=["Bebida", "Platillo"], 
          filled=True)
plt.title("Árbol de Decisión - Clasificación de Alimentos")
plt.show()
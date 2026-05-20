from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

#Carga los datos
iris=datasets.load_iris()
X = iris.data[:, [0,1]]
y = iris.target

#Dividir datos
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, test_size=0.2, random_state=1)

#Entrena el modelo
arbol = DecisionTreeClassifier(criterion='gini', max_depth=3)
arbol.fit(X_ent, y_ent)

# Evaluar desempeño
print("Exactitud del conjnto de entrenamiento: {:.2f}".format(arbol.score(X_ent,y_ent)))
print("Exactitud del conjnto de prueba: {:.2f}".format(arbol.score(X_pru, y_pru)))

# visualizar arbol de decision 
plt.figure(figsize=(12,6))
plot_tree(arbol, feature_names=['sepal length', 'sepal width'],
          class_names= iris.target_names,filled=True)
plt.title("Arbol de decision")
plt.savefig("arbol_de_decision.png") #Guaradar el arbol en imagen
plt.show

plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
for color, i, target in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(X_ent[y_ent==i, 0], X_ent[y_ent==i, 1], color=color, label=target)

xlim = plt.xlim()
ylim = plt.ylim()

xx, yy  = np.meshgrid(np.linspace(*xlim,num = 200),
                      np.linspace(*ylim, num= 200))
Z = arbol.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx,yy,Z, alpha=0.3, cmap='Set2')

plt.legend(loc='best')
plt.xlabel('longitud del sepalo', fontsize=12)
plt.xlabel('ancho del sepalo', fontsize=12)
plt.title("Regiones de decision - arbol de decision")
plt.savefig("regiones_decision.png")
plt.show()
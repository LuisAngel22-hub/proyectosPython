from sklearn.tree import DecisionTreeClassifier
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = datasets.load_iris()

X = iris.data
print("valores de X")

y = iris.target
print("valores de Y")

X_ent, X_pru, y_ent, y_pru = train_test_split(X,y,test_size=0.2, random_state=1)
print("\nvalores de X_ent")
print(X_ent)
print("\nvalores de Y_ent")
print(y_ent)
print("\nvalores de X_pru")
print(X_pru)
print("\nvalores de Y_pru")
print(y_pru)


arbol=DecisionTreeClassifier(criterion = 'gini', max_depth= 3)
arbol.fit(X_ent, y_ent)

print("conjunto de entrensamineto {:.2f}".format(arbol.score(X_ent,y_ent)))
print("conjunto de prueba {:.2f}".format(arbol.score(X_pru,y_pru)))

plt.figure(figsize=(12,8))
plot_tree(arbol, feature_names= iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("arbol del desicion del iris")
plt.show()


#datos importantes 
importantes = arbol.feature_importances_

indices = np.argsort(importantes) [::-1]

nombres=[iris.feature_names[i] for i in indices]
plt.title("Caracteristicas Importantes")
plt.bar(range(X.shape[1]), importantes[indices])
plt.xticks(range(X.shape[1]), nombres, rotation=90)
plt.show()

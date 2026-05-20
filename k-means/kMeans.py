import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans

datos=load_breast_cancer()
#Devuelve las caracteristicas mas importantes
print(datos.feature_names)

df=pd.DataFrame(datos.data,columns=datos.feature_names)
df["target"]=datos.target
#zip cra tuplas con mean radius y mean perimeter y list crea una lista con las tuplas
#y se obtiene un array con numpy

X=np.array(list(zip(df['mean radius'],df['mean perimeter'])))

#Creamos un objeto clasificador
knn= KMeans(n_clusters=2)
knn.fit(X)

#Obtenemos y mostramoslos 2 centroides donde cada uno es un array 31 valores
centroides= knn.cluster_centers_
print(centroides)

#Obtenemos y  mostramos el cluster al que pertenece cada punto
etiquetas = knn.labels_
print(etiquetas)


muestra=[[20,140]]
pred=knn.predict(muestra)
print("muestra", muestra,"se encuentra en el cluster: ", pred)

#hacemos una grafica con los datos
import matplotlib.pyplot as plt
c=['r','y']
colors = [c[i]for i in etiquetas]
plt.scatter(df['mean radius'], df['mean perimeter'], c=colors, s=20)
plt.scatter(centroides[:,0], centroides[:,1], marker='*', s=100, c='black')
plt.scatter(muestra[0][0], muestra[0][1], marker='o', s=100, c='green', edgecolor='black')
plt.xlabel("mean radius")
plt.ylabel("mean perimeter")
plt.show()  
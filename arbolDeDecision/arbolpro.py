import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin/"
import os
print(os.path.exists("D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/arbol.dot"))



X = np.array([['No','Bajo'],
             ['Si','Medio'],
             ['Si','Alto'],
             ['No','Alto'],
             ['Si','Bajo'],
             ['No','Bajo'],
             ['No','Medio'],
             ['Si','Alto'],
             ['No','Alto'],
             ['No','Bajo'],
             ])

y = [0,1,1,1,1,0,0,1,1,0]

from sklearn.preprocessing import LabelEncoder # LaberEncoder se utiliza para convertir etiquetas categóricas en valores numéricos
le = LabelEncoder()
X[:,0]= le.fit_transform (X[:,0]) #fit_transform Entrena el escalador a partir de los datos que se le pasen como argumento,
                                  #y transforma éstos devolviendo un array NumPy con los datos transformados
X[:,1]= le.fit_transform (X [:,1])
arbol=DecisionTreeClassifier(criterion = 'gini', max_depth= 3, random_state=1) #mide la impureza del nodo (es puro cuando todos los registros pertenecen a la misma clase)
arbol.fit(X,y)

prueba = np.array(['Si', 'Bajo'])
prueba_cod= le.fit_transform(prueba)
prediccion= arbol.predict(prueba_cod.reshape(1,-1))
print("Prediccción: ", prediccion[0])

from sklearn import tree
dot = tree.export_graphviz(arbol, feature_names= ['Tiene_casa', 'Ingreso anual'],
                            class_names= ['Aprobado', 'No aprobado'], out_file='arbol.dot')

import sys
 
sys.path.append("C:/Program Files (x86)/Graphviz/bin/dot.exe")
from graphviz import Source 

ruta_dot = "D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/arbol.dot"  # Ruta del archivo DOT

try:
    with open(ruta_dot, "r", encoding="utf-8") as archivo:
        contenido_dot = archivo.read()  # Leer el contenido del archivo DOT

    # Crear el gráfico desde el contenido DOT
    graph = Source(contenido_dot)
    
    # Mostrar el gráfico (esto abre la imagen generada automáticamente)
    graph.view()

    # Guardar la imagen en formato PNG
    graph.render("arbol", format="png")
    print("Imagen del árbol guardada como 'arbol.png'.")

except FileNotFoundError:
    print(f"El archivo {ruta_dot} no existe. Asegúrate de ejecutarlo antes.")
except Exception as e:
    print(f"Error al procesar el archivo DOT: {e}")
    
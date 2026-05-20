import pandas as pd
#se importa y se carga el dataset
from sklearn.datasets import load_breast_cancer
dataset=load_breast_cancer()
print(dataset)
#se convierte a un dataframe de pandas
df= pd.DataFrame(dataset.data, columns = dataset.feature_names)
df['tipo']=dataset.target[df.index]
print("************ conjunto de datos**************")
print(df)
#se obtienen los valores para las variables X e y
X=df.iloc[:,:1]
y=df['tipo'].values
print("Valor de X")
print(X)
print("valor de y")
print(y)

#Parte 2

#se separan los datos en conjuntos de prueba y entrenamiento from sklearn.model _selection import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print("**** X ENTRENAMIENTO \n")
print(X_train)
print("**** X PRUEBA \n")
print(X_test)
print("**** Y ENTRENAMIENTO \n")
print(y_train)
print("**** Y PRUEBA \n")
print(y_test)


from sklearn.linear_model import LogisticRegression
reg = LogisticRegression(max_iter=10000)

reg.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

print("Exactitud {:2f}".format(accuracy_score(y_test, reg.predict(X_test))))
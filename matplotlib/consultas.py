import pandas as pd 
from sklearn.model_selection import train_test_split
df=pd. read_csv("D:/kobe-/Documents/8A ISC/Mineria de datos/data.csv")
X=df. iloc[:, 1:].values
y=df. iloc[:,0].values
print("***** x ")
print (X)
print("** y ")
print (y)
entX, prux, enty, pruy=train_test_split(X,y, test_size=0.2, random_state=100)
print ("*** ENTRENAMIENTO X")
print(entX)
print("***** PRUEBA X")
print (prux)
print("**** ENTRENAMIENTO Y")
print (enty)
print("** PRUEBA Y*")
print (pruy)
#take on me
#lee un archivo muy grande
import pandas as pd
df=pd.read_csv('D:/kobe-/Documents/8A ISC/Mineria de datos/data.csv')
#print(df)
#print(df.head)  imprime lo que hay en la cabeza de las tablas
#print(df.columns)
print(df.iloc[9]) #Obtiene la fila de la posicion 10, ya que tomo 0 como primer indice
print(df.iloc[:10]) #No imprime la decima
print(df.iloc[0:1])#obtiene la cela (0,1)
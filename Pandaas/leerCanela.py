import pandas as pd
df=pd.read_csv('D:/kobe-/Documents/8A ISC/Mineria de datos/ventas.csv')
#Imorimir
print("-------------------------Imprime todo------------------------")
print(df)
print("------------------------Obtiene la fila de la posicion 10-----------------------")
print(df.iloc[9]) #Obtiene la fila de la posicion 10, ya que tomo 0 como primer indice
print("------------------------No imprime la posicion 10--------------")
print(df.iloc[:10]) #No imprime la decima
print("----------------Obtiene la celda (0,1)--------------------------------")
print(df.iloc[0:1])#obtiene la cela (0,1)
print("---------------------------Genera estadisticas descriptivas-----------------")
print(df.describe)
print("------------------------Incluye estadisticas en todas las columnas---------------")
print(df.describe(include="all"))

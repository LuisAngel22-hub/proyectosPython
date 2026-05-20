#dataframe
import pandas as pd
import numpy as np

df1=pd.DataFrame([
['1',1,30],
['2',1,32],
['3',0]],
)
df1.columns=['codigo','credito','edad']
print(df1)
#elimina las filas donde hay valores ausentes. df2=df1.dropna(axis=0) #esta es por defecto
df2=df1.dropna(axis=0)
print(df2)

from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values= np.nan, strategy='mean')
imp=imp.fit(df1.values)
imp_datos=imp.transform(df1.values)
print(imp_datos)

#elimina las COLUMNAS donde hay valores ausentes.
df3=df1.dropna(axis=1) #esta es por defecto
print("COLUMNA/n*")
print(df3)
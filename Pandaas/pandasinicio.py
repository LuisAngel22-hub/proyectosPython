import pandas as pd
misdatos={
    'meses':["enero","febrero","marzo","abril","mayo"],
    'dias':[31,28,31,30,30]

    #El data frame va entre llaves
}
resultado=pd.DataFrame(misdatos)
print(resultado)
numAlumnos={
    'semestre': ["primero","tercero","quinto","septimo"],
    'numero': [25,15,25,40]
}
resultado1=pd.DataFrame(numAlumnos)
print(resultado1)
print("-------------------------------------------------------")


dias=[31,28,31,30]
meses=pd.Series(dias,
index=["enero","febrero","marzo","abril"])
print(meses)
print(meses["marzo"])
print("--------------------------------------------------------")

#a traves del index se muestra 
##MANEJO DE INDICES
ganancias={"enero":35000, "febrero":20350}
miserie=pd.Series(ganancias, index=["enero","febrero"])
print(miserie)
print("---------------------------------------------------------")



df=pd.read_csv('D:/kobe-/Documents/8A ISC/Mineria de datos/meses.csv')
print(df)
#Para leer desde el inicio del archivo
print(df.head(6))
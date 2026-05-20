import numpy as np
vec1=np.array([1,2,3,4,5])
print(vec1)
#DEVUELVE LAS DIMENSIONES
print(vec1.shape)

#Tamaño de la matriz
matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print(matriz.shape)

vec2=np.zeros(4)
print (vec2)
matriz2=np.zeros((2,4))
print (matriz2)

matriz3=np.random.random((2,4))
print(matriz3)

lista1=[5,6,7,8,9,10]
vec3=np.array(lista1)
print(vec3)

print("--------------Genera los 10 primeros numeros--------------------")
nums=np.arange(10)
print(nums)

print("------------------------Generar matrices----------------------")

matrizA=np.array([[8,9,2],[4,11,21],[21,3,6]])
matrizB=np.array([[18,49,21],[4,13,22],[1,13,16]])
print(matrizA)
print(matrizB)

print("-------------------Suma + ---------------------------")
C= matrizA+matrizB
print(C)
print("--------------------------Suma ADD---------------------")
D=np.add(matrizA,matrizB)
print(D)
print("----------------------Resta -  ----------------------------------")
C=matrizA-matrizB
print(C)
print("--------------------------Resta subtract-----------------------")
resta1=np.subtract(matrizA,matrizB)
print(resta1)

print("----------------------Multiplicacion--------------------------")
multi=matrizA*matrizB
print(multi)
multii=np.multiply(matrizA,matrizB)
print(multii)


print("--------------------------Division / ---------------------------------------")
divi=matrizA/matrizB
print(divi)
print("--------------------------Division - divide ---------------------------------------")
divii=np.divide(matrizA,matrizB)
print(divii)
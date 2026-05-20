#suma de dos numeros e imprimir
a=10
b=5
suma= a+b
print("la suma de:", a , "y" , b , "es=", suma)


#Media
media = 95/100
precio= 100*media
pi=12.1416
var1=precio/pi
resultado=round(var1,2)
print("media: ", media)
print('Precio: ', precio)
print('pi',pi,'Resultado: ', resultado)

#indica tipo
tipo=type(pi)
print(tipo)

#\ caracteres de escape para concatenar un caracter especial
#\n salto de linea

nombre="CHETE ES MENSO"
saludo= "mal dia"
print("\'nombre'")

#Rebanadas

palabra="Elpepe"
letras=palabra [2:4]
print(letras)
letras=palabra [:2]
print(letras)
letras=palabra [2:]
print(letras)

#
num_naturales=[0,1,2,3,4,5,6,7,8,9]
num_naturales[:3]
vocales=['a','e','i','o','u']
print(num_naturales)
print(vocales)

#Agregar elementos a una lista, un solo elemento
vocales.append('b')
print(vocales)

#while con serie fibonacci
numero1,numero2=0,1
while numero1<1000:
    print(numero1)
    numero1,numero2=numero2, numero1+numero2

#funcion jimbo

x= int(input("Ingresa tu fockin edad:"))
if x<0:
    x=0
    print('edad no valida')
elif x==0:
    print('No existe esa edad')
elif x >= 1 and x<18:
    print('eres menor de edad')
else:
    print ('Eres mayor de super edad')


#continue sirve para indicar sentencia en while al entra a un bucle if

print('while con sentencia continue')
print('=========================')
vari=10
while (vari>0):
    vari -=1
    if vari== 4:
        print('entra en el continue y la vari es ' + str(vari))
        continue
    print('Hola mundo')


#conjuntos
c1=set([2,4,6,8])
print(c1)
c2=set([1,3,5,7])
print(c2)
c2.add(9)
print(c2)
c2.add(11)
print(c2)
c2.remove(5)

c1.add(9)
print("conjubto 1: ",c1)
print("conjunto 2: ",c2)
c3=c1.intersection(c2)
print("intersección del c1 y c2: ", c3)
c3=c1.union(c2)
print("unión del c1 y c2: ",c3)
c3=c1.difference(c2)
print("diferencia del c1 y c2: ",c3)

#Funciones en python
#def


#def solicitud()
    #m=int(input("ingresa un numero: "))
    #return n


#def facto():
    #n=solicitud()
    #print("El factorial de", n, "es: " factorial(n))


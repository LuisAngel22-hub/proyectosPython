#Se usa el analisis
import numpy
from statistics import mode
datos = [33,55,33,22,11,76,75,32,33]
mediana = numpy.median(datos)
print('la mediana es: ',mediana)
media=numpy.mean(datos)
print('la media es: ', media)
moda= mode(datos)
print("la moda es: ",moda)
maximo=numpy.max(datos)
print('el valor es maximo es:', maximo)
minimo=numpy.min(datos)
print('el valor minimo es: ', minimo)
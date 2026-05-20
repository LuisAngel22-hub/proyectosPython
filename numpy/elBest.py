#Hola
#Escribe el f para las cadenas

import statistics
import numpy
#Guarda los daotos
def guardar_datos(archivo):
    with open(archivo, 'a') as f:
        while True:
            try:
                dato = float(input("Ingrese un número: "))
                #lee el dato y se guarda
                f.write(f"{dato}\n")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
            #Pide al usuario si desea agregar otro numero xdddd
            continuar = input("¿Desea agregar otro número? (s/n): ").strip().lower()
            if continuar != 's':
                break

def leer_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            datos = [float(line.strip()) for line in f.readlines()]
        return datos
    except FileNotFoundError:
        print("El archivo no existe aún.")
        return []
    except ValueError:
        print("El archivo contiene datos no válidos.")
        return []

def calcular_estadisticas(datos):
    if not datos:
        print("No hay datos para calcular estadísticas.")
        return
    minimo= numpy.max(datos)
    maximo= numpy.min(datos)
    media = statistics.mean(datos)
    mediana = statistics.median(datos)
    try:
        moda = statistics.mode(datos)
    except statistics.StatisticsError:
        moda = "No hay moda única"
    
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Minimo: {minimo} ")
    print(f"Máximo: {maximo}")

archivo = "datos.txt"
guardar_datos(archivo)
datos = leer_datos(archivo)
calcular_estadisticas(datos)

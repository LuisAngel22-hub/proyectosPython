import statistics
import numpy

# Función para guardar valores en un archivo txt
def guardar_en_archivo(valores, archivo="valores.txt"):
    with open(archivo, "w") as f:
        for valor in valores:
            f.write(f"{valor}\n")

# Función para cargar valores desde un archivo txt
def cargar_desde_archivo(archivo="valores.txt"):
    try:
        with open(archivo, "r") as f:
            valores = []
            for linea in f:
                try:
                    valores.append(float(linea.strip()))  # Intentar convertir a float
                except ValueError:
                    print(f"Valor inválido en el archivo ignorado: '{linea.strip()}'")
            return valores
    except FileNotFoundError:
        return []

def mostrar_menu(media, mediana, moda, maximo, minimo, matriz):
    print("\nMatriz actual de valores:", matriz)
    print(f"Media: {media:.3f}, Mediana: {mediana}, Moda: {moda}, Máximo: {maximo}, Mínimo: {minimo}")
    print("\nOpciones para sustituir el valor erróneo:")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print("4. Máximo")
    print("5. Mínimo")
    print("6. No corregir")
    opcion = input("Elige una opción (1-6): ")
    
    if opcion == "1":
        return media
    elif opcion == "2":
        return mediana
    elif opcion == "3":
        return moda
    elif opcion == "4":
        return maximo
    elif opcion == "5":
        return minimo
    elif opcion == "6":
        return None
    else:
        print("Opción inválida. No se corregirá el valor.")
        return None

def solicitar_valores():
    valores = cargar_desde_archivo()  # Cargar valores previos
    print("Valores actuales en el archivo:", valores)
    
    while True:
        entrada = input(f"Ingresa un valor (actual tamaño: {len(valores)}): ")
        try:
            valores.append(float(entrada))
        except ValueError:
            print(f"Se detectó una entrada inválida: '{entrada}'. Terminando el ciclo...")
            media, mediana, moda, maximo, minimo = calcular_estadisticas(valores)
            sustituto = mostrar_menu(media, mediana, moda, maximo, minimo, valores)
            if sustituto is not None:
                valores.append(sustituto)
            break
        guardar_en_archivo(valores)  # Guardar valores actualizados
    
    return valores

def calcular_estadisticas(valores):
    if valores:
        moda = statistics.mode(valores) if len(valores) > 0 else None
        media = round(statistics.mean(valores), 3)  # Redondear a 3 decimales
        mediana = statistics.median(valores)
        maximo = numpy.max(valores)
        minimo = numpy.min(valores)
        return media, mediana, moda, maximo, minimo
    return None, None, None, None, None

def main():
    while True:
        valores = solicitar_valores()
        print("\nValores ingresados:", valores)
        
        try:
            valores_numericos = [float(v) for v in valores]  # Filtrar solo valores numéricos
        except ValueError:
            valores_numericos = []
        
        media, mediana, moda, maximo, minimo = calcular_estadisticas(valores_numericos)
        print(f"\nResultados actuales:")
        print(f"Media: {media:.3f}, Mediana: {mediana}, Moda: {moda}, Máximo: {maximo}, Mínimo: {minimo}")
        
        if input("\n¿Quieres seguir ingresando valores? (s/n): ").lower() != 's':
            break

main()
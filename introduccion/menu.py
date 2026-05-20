def suma_numeros():
    a = 10
    b = 5
    suma = a + b
    print("La suma de:", a, "y", b, "es =", suma)


def calcular_media():
    media = 95 / 100
    precio = 100 * media
    pi = 12.1416
    var1 = precio / pi
    resultado = round(var1, 2)
    print("Media:", media)
    print("Precio:", precio)
    print("Pi:", pi)
    print("Resultado:", resultado)


def tipo_de_dato():
    pi = 12.1416
    tipo = type(pi)
    print("El tipo de dato de pi es:", tipo)


def caracteres_escape():
    nombre = "CHETE ES MENSO"
    print("'nombre'")  # Caracter especial con \'


def rebanadas():
    palabra = "Elpepe"
    print("2:4 ->", palabra[2:4])
    print(":2 ->", palabra[:2])
    print("2: ->", palabra[2:])


def listas():
    num_naturales = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    vocales = ['a', 'e', 'i', 'o', 'u']
    vocales.append('b')
    print("Números naturales:", num_naturales)
    print("Vocales:", vocales)


def fibonacci():
    numero1, numero2 = 0, 1
    print("Serie Fibonacci:")
    while numero1 < 1000:
        print(numero1)
        numero1, numero2 = numero2, numero1 + numero2


def jimbo():
    x = int(input("Ingresa tu edad: "))
    if x < 0:
        x = 0
        print("Edad no válida")
    elif x == 0:
        print("No existe esa edad")
    elif x >= 1 and x < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")


def conjuntos():
    c1 = set([2, 4, 6, 8])
    c2 = set([1, 3, 5, 7])
    c2.add(9)
    c2.add(11)
    c2.remove(5)

    c1.add(9)
    print("Conjunto 1:", c1)
    print("Conjunto 2:", c2)
    print("Intersección:", c1.intersection(c2))
    print("Unión:", c1.union(c2))
    print("Diferencia:", c1.difference(c2))


def continuar():
    print("While con sentencia continue:")
    vari = 10
    while vari > 0:
        vari -= 1
        if vari == 4:
            print("Entra en el continue, vari es:", vari)
            continue
        print("Hola mundo")


def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Suma de dos números")
        print("2. Calcular media")
        print("3. While con sentencia continue")
        print("4. Fibonacci")
        print("5. Calcular edad")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            suma_numeros()
        elif opcion == "2":
            calcular_media()
        elif opcion == "3":
            continuar()
        elif opcion == "4":
            fibonacci()
        elif opcion == "5":
            jimbo()
        elif opcion == "0":
            print("Todo listo puajaja")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar el menú
menu()

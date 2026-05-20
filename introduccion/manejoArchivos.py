#Lee y muestra todo el contenido del archivo
with open (r"D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/hola.py","r") as archivo:
    contenido= archivo.read()
    print(contenido)


f=open (r"D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/menu.py","r")
linea=f.readlines()

print(linea[2:])
f.close();

for lineaArc in open (r"D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/menu.py","r"):
    print(lineaArc)
f.close();
#escritura en archivo
lineaEscritura=open (r"D:/kobe-/Documents/8A ISC/Mineria de datos/ejercicios python/menu.py","w")
line=input("Ingrese su nombre: ")
lineaEscritura.write(line)
lineaEscritura.close()


import matplotlib.pyplot as plt

# Crear datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Crear gráfico de línea
plt.plot(x, y)

# Añadir títulos y etiquetas
plt.title('Título del Gráfico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar gráfico
plt.show()
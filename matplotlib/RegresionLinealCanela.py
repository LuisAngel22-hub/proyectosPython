import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el CSV
df = pd.read_csv("D:/kobe-/Documents/8A ISC/Mineria de datos/ventas.csv")

# Ver columnas
print("Columnas:", df.columns.tolist())

nombres = df["Fecha_Vent"]
cantidades = df["Cant_Pagar"]

# Configuración general

x = np.arange(len(nombres))
m, b = np.polyfit(x, cantidades, 1)  
plt.plot(x, cantidades, 'o', label="Datos") 
plt.plot(x, m * x + b, '-', label="Regresión")  
plt.xticks(x, nombres, rotation=90)  
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.title("Gráfica de Ventas en canela")
plt.legend()

plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot") #Se aplican los estilos de las graficas

# Cargar el archivo CSV
archivo = "D:/kobe-/Documents/8A ISC/Mineria de datos/ventas.csv"
ventas_df = pd.read_csv(archivo)

# Asegurarse de que la columna de fechas esté en el formato correcto
ventas_df["Fecha_Vent"] = pd.to_datetime(ventas_df["Fecha_Vent"])

# Agrupar por fecha y sumar la cantidad pagada por día
ventas_por_dia = ventas_df.groupby("Fecha_Vent")["Cant_Pagar"].sum()

# Crear la gráfica
plt.figure(figsize=(5, 5))
#Tipo de grafica en este caso es solo linea
plt.plot(ventas_por_dia.index, ventas_por_dia.values, 'g-o', label="Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Ventas (pesos)")
plt.title("Crecimiento de Ventas en el Tiempo")
plt.xticks(rotation=45)
plt.legend() #Muestra una leyenda
plt.tight_layout()
plt.show() #Imprime la grafica

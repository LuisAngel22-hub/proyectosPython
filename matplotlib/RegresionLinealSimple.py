import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(0)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100,1)


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=10)

modelo= LinearRegression()

modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

print("interseccion (b):", modelo.intercept_)
print ("pendiente (m): ", modelo.coef_)

plt.scatter(x,y, color="red",label="Datos reales")
plt.plot(x_test, y_pred, color="green", linewidth=2, label="Linea de regresion")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("Regresion Lineal Simple - Luis Angel")
plt.legend()
plt.show()
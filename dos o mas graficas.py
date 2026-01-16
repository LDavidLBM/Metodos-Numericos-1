#Graficar la funcion x² y x+1
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)

plt.plot(x, x+1, label="x+1")
plt.plot(x, x**2, label="x²")
#El plt.plot sirve para poder hacer mas graficas, entre mas plot mas graficas

plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Dos Graficas")
plt.grid()
plt.show()
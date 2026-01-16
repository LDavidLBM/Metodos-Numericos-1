#Graficar la funcion exponencial
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
y=x**2

plt.plot(x,y)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de f(x)=exp(x)")
plt.grid()
plt.show()
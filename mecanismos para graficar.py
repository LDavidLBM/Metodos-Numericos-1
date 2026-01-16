#Graficar la funcion exponencial
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
y=np.sin(x) #Despues de este púnto pones la funcion que quieres graficar

plt.plot(x,y)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de f(x)=exp(x)")
plt.grid()

plt.savefig("sin.png", dpi=300) #El ".png" sirve para poder guardar en imagen y ".pdf" para guardar en pdf, y el "dpi" es para ver que tnanta resoluciuon necesitas
plt.show()
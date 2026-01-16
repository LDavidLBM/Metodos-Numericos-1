#Graficar la funcion x² y x+1
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)

plt.plot(x, x+1,
         color="red",
         linestyle="dotted",
         linewidth=2.3,
         label="x+1")
plt.plot(x, x²,
          color="blue",
         linestyle="dashdot",
         linewidth=2, 
         label="x²")


plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Dos Graficas")
plt.grid()
plt.show()



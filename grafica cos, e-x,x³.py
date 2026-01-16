#Graficar la funcion cosx, e-²,x³
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)

plt.plot(x, np.cos(x),
         color="green",
         linestyle="-.",
         linewidth=2,
         label="cos(x)")
plt.plot(x, np.exp(-x),
         color="orange",
         linestyle="--",
         linewidth=2,
         label="exp(-x)")
plt.plot(x, x**3,
         color="blue",
         linestyle=":",
         linewidth=2,
         label="x³")


plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("cos(x),e-x,x³")
plt.grid()
plt.savefig("cosx, e-x,x³.png")
plt.show()

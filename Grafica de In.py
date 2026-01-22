import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_log(x ,n):
    sum=0
    for k in range(1,n+1):
        sum=sum+(-1)**(k+1)*(x-1)**k/k
    return sum
x=np.linspace(0.1,2,100)

plt.figure(figsize=(8,8))

plt.plot(x,np.log(x),label=r"$In$",linewidth=1)

for n in [1,2,4,8,16]:
    plt.plot(x,taylor_log(x,n), label=f"Taylor de grado {n}", linewidth=1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafica de la logar")
plt.legend()
plt.grid()
plt.show()
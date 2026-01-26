import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_fun(x ,n):
    sum=0
    for k in range(1,n+1):
        sum=sum+(-1)**(k//2) * x**(2*k)
    return sum

x0=-0.25
valor_exacto=1/(1 + x0**2)
suma=0

print("="*78)
print(f"{'n':^10} | {'Aprox f(x)':^22} | {'Error Abs':^18} | {'Error Rel':^18}")
print("="*78)

for n in range(4):
    collar=(-1)**n * x0**(2*n)
    suma+=collar
    error_abs=abs(valor_exacto-suma)
    error_real=error_abs/valor_exacto

    print(f"{n:^10} | {suma:^22.10f} | {error_abs:^18.10f} | {error_real:^18.10f}")

print("="*78)

x=np.linspace(-2,2,100)
plt.figure(figsize=(8,8))

plt.plot(x, 1/(1+x**2), label=r"$Funcion$", linewidth=1, color='black')

for n in [1,2,4]:
    y = taylor_fun(x,n)
    plt.plot(x, y, label=f"Taylor de grado {n}", linewidth=1, linestyle='--')
print("Valor real: ", valor_exacto)
print("Aproximacion: ", suma)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafica de la funcion")
plt.legend()
plt.grid()
plt.show()
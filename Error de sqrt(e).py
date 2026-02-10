import matplotlib.pyplot as plt
import math

x=0.5
valor_real=math.exp(x)

sum=0
n_valores=[]
error_relativo=[]

print("="*70)
print(f"{'n':^10} | {'Aprox e^x':^15} | {'Error Relativo':^15} | {'Valor Real':^15}")
print("="*70)

sum=0
for n in range(20):
    sum=sum+x**n/math.factorial(n)
    error_abs=abs(valor_real-sum)
    error_rel=error_abs/valor_real if valor_real != 0 else 0
    n_valores.append(n)
    error_relativo.append(error_rel)
    print(f"{n:^10} | {sum:^15.8f} | {error_rel:^15.8f} | {valor_real:^15.8f}")

    if error_rel<1e-3:
        break

print("="*70)
print("Valor real: ", valor_real)

plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n (Grado del polinomio de Taylor)")
plt.ylabel("Error Relativo")
plt.title("Convergencia de la Aproximación de raiz de e con Taylor")
plt.show()
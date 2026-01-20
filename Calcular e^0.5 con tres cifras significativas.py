import math
import matplotlib.pyplot as plt

#parametros
x=0.5
valor_exacto=math.exp(x)

#variables
sum=0
n_valores=[]
error_relativo=[]

#Encabezado tabla
print("="*60)
print(f"{'n':^10} | {'Aprox e^x':^14} | {'Error Abs':^14} | {'Error Real':^14}")
print("="*60)

#Serie de Taylor
sum=0

for n in range(20):
    sum=sum+x**n/math.factorial(n)
    error_abs=abs(valor_exacto-sum)
    error_real=error_abs/valor_exacto
    
    n_valores.append(n)
    error_relativo.append(error_real)
    print(f"{n:^10} | {sum:^14.8f} | {error_abs:^14.8f} | {error_real:^14.8f}")
    
    if error_real<0.5e-8: #A{} igual se puede poner como 0.005
        break
print("="*60)

#Grafica del error relativo
plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n (Grado del polinomio)")
plt.ylabel("Error relativo")
plt.title("COnvergencia de la serie de Taylor e^x en 0.5")
plt.show()
plt.legend()

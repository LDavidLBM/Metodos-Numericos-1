import math
valor_exacto = math.sqrt(2)
a=0.5
x=1.0
h=(x - a)/(1 + a) 
sumatoria=0

print("="*80)
print(f"{'n':^10} | {'Aprox sqrt(2)':^22} | {'Error Abs':^18} | {'Error Rel':^18}")
print("="*80)


for n in range(30):
    coef=1
    for k in range(n):
        coef*=(0.5 - k)
    coef/=math.factorial(n)
    collar=coef * h**n
    sumatoria+=collar
    aproximacion=math.sqrt(1 + a) * sumatoria
    error_abs=abs(valor_exacto - aproximacion)
    error_real=error_abs / valor_exacto

    print(f"{n:^10} | {aproximacion:^22.10f} | {error_abs:^18.10f} | {error_real:^18.10f}")


    if error_real<0.5e-3:
        break

print("="*80)
print("Valor real: ", valor_exacto)
print("Aproximacion: ", sumatoria)
print("="*78)

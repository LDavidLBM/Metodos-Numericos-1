#Inciso a)
import math
valor_exacto=math.pi
sumatoria=0
sumar=0
suma=0
x=0.5

print("="*66)
print(f"{'n':^10} | {'Aprox pi con leibniz':^19} | {'Error Abs':^14} | {'Error Real':^14}")
print("="*66)

for n in range(20):
    collar=(-1)**n/(2*n+1)
    sumatoria=sumatoria+collar
    aprox_pi=4*sumatoria
    error_abs=abs(valor_exacto-aprox_pi)
    error_real=error_abs/valor_exacto
    print(f"{n:^10} | {aprox_pi:^19.8f} | {error_abs:^14.8f} | {error_real:^14.8f}")

    if error_real<0.5e-8:
        break
print("="*66)
print("Valor real: ", valor_exacto)
print("Aproximacion: ", sumatoria)
print("="*78)

#Incisio b)
print("="*66)
print(f"{'n':^10} | {'Aprox pi con taylor':^19} | {'Error Abs':^14} | {'Error Real':^14}")
print("="*66)

for n in range(20):
    mano=(-1)**n*x**(2*n+1)/(2*n+1)
    suma=suma+mano
    aprox_pi2=4*suma
    error_abs=abs(valor_exacto-aprox_pi2)
    error_real=error_abs/valor_exacto
    print(f"{n:^10} | {aprox_pi2:^19.8f} | {error_abs:^14.8f} | {error_real:^14.8f}")
    
    if error_real<0.5e-8:
        break
print("="*66)
print("Valor real: ", valor_exacto)
print("Aproximacion: ", suma)
print("="*78)


#Inciso c)
print("="*66)
print(f"{'n':^10} | {'Aprox pi con Ramanujan':^19} | {'Error Abs':^14} | {'Error Real':^14}")
print("="*66)

for n in range(20):
    valor=(math.factorial(4*n) * (1103 + 26390*n)) / (math.factorial(n)**4 * 396**(4*n))
    sumar=sumar+valor
    aprox_pi3=1/(sumar*(2*math.sqrt(2)/9801))
    error_abs=abs(valor_exacto-aprox_pi3)
    error_real=error_abs/valor_exacto
    print(f"{n:^10} | {aprox_pi3:^22.8f} | {error_abs:^14.8f} | {error_real:^14.8f}")

    if error_real<0.5e-8:
        break
print("="*66)
print("Valor real: ", valor_exacto)
print("Aproximacion: ", aprox_pi3)
print("="*78)
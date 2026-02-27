import math
fun=input("Ingrese la funcion que desea evaluar: ")

def f(x):
    return eval(fun, {"x":x, "math":math})

a, b = map(float, input("Ingrese los intervalos a evauluar: ").split(","))
iter=int(input("Ingrese el numero de iteraciones que desea realizar: "))

print(f"{'n':^4} | {'a':^15} | {'b':^15} | {'raiz':^15} | {'fraiz':^15} |")
print("-"*74)

fa=f(a)
fb=f(b)

if fa*fb<0:
    for n in range(iter):
        raiz=(a+b)/2
        fraiz=f(raiz)
        print(f"{n+1:^4} | {a:^15.8f} | {b:^15.8f} | {raiz:^15.8f} | {fraiz:^15.8f} |")
        if fraiz==0:
            break
        if fa*fraiz<0:
            b=raiz
        else:
            a=raiz
    print(f"La raiz es: {raiz}")
else:
    print("La funacion debe tener signos opuestos al evaluar en los intervalos")
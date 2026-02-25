import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def biseccion(f,a,b,n_iter):

    if f(a)*f(b)>0:
        raise ValueError("f(a) y f(b) deben tener signos diferentes")
    
    #Punto medio inicial y lista de puntos medios
    p_anterior=(a+b)/2
    puntos_medios=[]

    #Nombre de los valores de la tabla
    print("n   |    a   |   b  |    p   |   f(p)    |    error relativo")
    print("-"*65)

    #ciclo principal de la biseccion
    for n in range(1, n_iter+1):
        #calcula el punto medio del intervalo actual
        p=(a+b)/2

        #Ver si f(p)=0
        if f(p)==0:
            print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f}" 
                  f"{f(p):11.2e} {'0.00e+00':>13}")
            
            print("La raiz execta fue encontrada")
            break
        #Calcula el error relativo
        error_rel=abs((p-p_anterior)/p)
        #Guarda los puntos medio
        puntos_medios.append(p)

        #Imprime la fila corespondiente
        print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f}" 
              f"{f(p):11.2e} {error_rel:13.2e}")

        #En que intervalo esta la raiz
        if f(a)*f(b)>0:
            a=p
        else:
            b=p
        
        p_anterior=p

    #Regresa la ultima aproximacion y todos los puntos medios
    return p, puntos_medios

''''Ejemplo:'''
#Definimos la funcion
def f(x):
    return 2*x**3-x**2+x-1

#Definimos los intervalos e iteraciones
a=0
b=1
n_inter=20

#Tolerancia
epsilon=1e-6

#Invocamos el metodo de biseccion
raiz, puntos=biseccion(f, a, b, n_inter)

#Muestra la aproximacion final
print(f"Aproximacion a la raiz desoues de {n_inter} iteraciones: {raiz}")

#------------------------------------------------------------------------------------------------
#GRAFICA Y ANIMACION DE LA CONVERGENCIA
#------------------------------------------------------------------------------------------------

#Genera puntos para dibujar la funcion
"""x=[a+i*(b-a)/400 for i in range(401)]
y=[f(xi)for xi in x]

#Crea la figura y los ejes
fig, ax= plt.subplots()

#Dibuja la funcion f(x)
ax.plot(x, y, label="f(x)")

#Dibuja el eje x
ax.axhline(0, color="black")

#Configura los limites del grafico
ax.set_xlim(a,b)
ax.set_ylim(min(y), max(y))

#Etiquetas y titulo
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Convergencia del Método de Biseccion")

#Objeto gráfico para los puntos medios (inicialmente vacío)
puntos_plot,=ax.plot([], [], 'ro', label="Puntos medios")

#Marca la raiz final
ax.plot(raiz, 0, 'ko', label="Raiz aproximada")

#Muestra la leyenda
ax.legend()

#--------------------------------------------------------------------------------------------------
#Función que actualiza la animación
#--------------------------------------------------------------------------------------------------
def actualizar(frame):
    x_data=puntos[:frame + 1]
    #Puntos medios hasta el frame actual
    y_data=[0]*(frame + 1)
    #Todos sobre el eje x
    puntos_plot.set_data(x, x_data, y_data)
    return puntos_plot,

#Crea la animacion
anim=FuncAnimation(fig,actualizar, frames=len(puntos), interval=500, repeat=False)

#Muestra la animacion
plt.show()"""
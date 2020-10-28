import random
import os
import numpy as np

def exponential(x):
    time =  np.log(np.random.uniform()) *-1

    return time/x


def c_star(lista, lista2):
    n = 0
    d = 0
    x_bar = sum(lista) / len(lista)
    y_bar = sum(lista2) / len(lista2)

    for i in range(0, len(lista)):
        n = n + (lista[i] - x_bar) * (lista2[i] - y_bar)
        d = d + pow(lista[i]-y_bar, 2)

    return -1*(n/d)



def get_uniform():

    x = random.uniform(0, 1)

    return x


#parte 1
x_var = exponential(1)
y_var = exponential(1)
print("antiteticas", (x_var + y_var) / 2)


#parte 2
def control(n):
    vi = 0
    lista_x = []
    lista_y = []

    for i in range(n):
        v = np.random.random(size=1)
        lista_x.append(np.sqrt(1-v**2))
        lista_y.append(v**2)
    
    c = float(c_star(lista_x, lista_y))
    #print("c*", c)

    for i in range(n):
        vi = vi+(lista_x[i] + c*(lista_y[i] - 0.5))    

    return vi/n


print(control(1000))
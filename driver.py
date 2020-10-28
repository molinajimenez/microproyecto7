import random
import sys
import numpy as np
import matplotlib.pyplot as plt

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
suma = x_var + y_var
print("Valor esperado por antiteticas es: ", suma / 2)


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

    
    
    return vi[0]/n

print("variables de control es: ", control(int(sys.argv[1])))
#parte 3
def strati(values_list): 
	print("rango 0 a 1:")
	ev = 0
	for i in range(len(values_list[0:10])):
		ev = ev + (i/10)*(values_list[i])
	print("valor esperado es: ", ev)

	ev = 0
	print("rango 1 a 3:")
	for i in range(len(values_list[10:30])):
		ev = ev + (i+10)*(values_list[i+10])
	print("valor esperado es: ", ev/10)

	ev = 0
	print("rango 3 a infinito:")
	for i in range(len(values_list[30:])):
		ev = ev + (i+30)*(values_list[i+30])
	print("valor esperado es: ", ev/10000)


x_values =[]
y_values =[]
for i in range(1,int(sys.argv[1])):
	x_values.append(i)
	y_values.append(exponential(i))

strati(values_list = y_values)

plt.plot(y_values)
plt.savefig('books_read.png')


#parte 4
def parte4(length):
    exp_x = []
    exp_y = []
     
    for x in range(length):
        x = np.random.random(size=1)
        exp_x.append(exponential(x))
        y = np.random.random(size=1)
        exp_y.append(exponential(1/y))

    positivas = 0
    for i in range(0, len(exp_x)):
        if exp_x[i] * exp_y[i] <= 3:
            positivas = positivas + 1 
    
    return positivas/len(exp_x)
     

print("La eficiencia de este algoritmo para estimar P(XY<=3) es: ",parte4(int(sys.argv[1])))
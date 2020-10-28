import math
import random
import numpy as np
import matplotlib.pyplot as plt

#parte 3
def exponential(x):
    time =  np.log(np.random.uniform()) *-1

    return time/x


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
for i in range(1,10000):
	x_values.append(i)
	y_values.append(exponential(i))

strati(values_list = y_values)

plt.plot(y_values)
plt.savefig('books_read.png')

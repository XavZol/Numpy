import numpy as np
import pandas as pd 
import time 


array1 = np.array([1, 2, 3])
print(array1)

array2 = np.array([[0], [10], [20], [30]])
print(array2)

broadcast_suma = array2 + array1 # broadcasting, se suman cada elemento de array1 a cada fila de array2
print(broadcast_suma)

broadcast_mult = array2 * array1 # broadcasting, se multiplican cada elemento de array1 a cada fila de array2
print(broadcast_mult)

# Funciones Universales
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

resultado = np.add(a, b) # suma elemento a elemento
print(resultado)

#substract, multiply, divide, power, log, exp, sin, cos, tan, etc

resultado2 = np.exp(a)
print(resultado2)

resultado3 = np.log(a)
print(resultado3)

resultado4 = np.log10(a)
print(resultado4)

resultado5 = np.sqrt(a)
print(resultado5)


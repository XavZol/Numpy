import numpy as np
import pandas as pd 
import time 


x = [ 1, 2, 3]
y = [ 4, 5, 6]
z = [ 7, 8, 9]

print(np.concat((x, y, z))) # concatenar arrays concat y concatenate hacen lo mismo, pero concat es mas rapido que concatenate
print(np.concatenate((x, y, z)))

a = [[1, 2], 
        [3, 4]]
b = [[5, 6], 
        [7, 8]]

print(np.concat([a] + [b], axis=1))
print(np.concat([a] + [b], axis=0)) # concatenar con axis=0 es lo mismo que sin axis, pero es mas rapido que con axis=0

array_concat = np.concat([a] + [b], axis=0)
print(np.shape(array_concat))

array_reformado = array_concat.reshape(2, 4) # reformar el array a una nueva forma, en este caso a una matriz de 2 filas y 4 columnas
print(array_reformado)

array_sumado = array_reformado + array_reformado # sumar el array consigo mismo, lo que es lo mismo que multiplicar por 2, pero es mas rapido que multiplicar por 2
print(array_sumado) 

array_mult = array_reformado * array_reformado # multiplicar el array consigo mismo, lo que es lo mismo que elevar al cuadrado, pero es mas rapido que elevar al cuadrado
print(array_mult)

raices = np.sqrt(array_mult) # calcular la raiz cuadrada del array, lo que es lo mismo que elevar al cuadrado y luego sacar la raiz cuadrada, pero es mas rapido que elevar al cuadrado y luego sacar la raiz cuadrada
print(raices)
import numpy as np
import pandas as pd 
import time 

array1d = np.array([1, 2, 3, 4, 5])

array2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(array1d[0]) # ingresamos el indice del elemento que queremos mostrar, en este caso el primer elemento del array1d

print(array1d[-1]) # ingresamos el indice del elemento que queremos mostrar, en este caso el ultimo elemento del array1d, el indice -1 hace referencia al ultimo elemento del array

print(array2d[0]) # ingresamos el indice del elemento que queremos mostrar, en este caso el primer elemento del array2d, el resultado es un array de 3 elementos, ya que el primer elemento del array2d es un array de 3 elementos

print(array2d[0, 0]) # ingresamos el indice del elemento que queremos mostrar, en este caso el primer elemento del primer elemento del array2d, el resultado es un numero, ya que el primer elemento del primer elemento del array2d es un numero

print(array2d[1, 2]) # ingresamos el indice del elemento que queremos mostrar, en este caso el tercer elemento del segundo elemento del array2d, el resultado es un numero, ya que el tercer elemento del segundo elemento del array2d es un numero
print(array2d[1] [2]) # lo mismo que la linea anterior, pero con una sintaxis diferente, el resultado es el mismo, ya que el tercer elemento del segundo elemento del array2d es un numero


print(array1d[1:4]) # ingresamos el indice del elemento que queremos mostrar, en este caso los elementos desde el indice 1 hasta el indice 3 del array1d, el resultado es un array de 3 elementos, ya que los elementos desde el indice 1 hasta el indice 3 del array1d son 3 elementos

print(array2d[1, :]) # ingresamos el indice del elemento que queremos mostrar, en este caso todos los elementos del segundo elemento del array2d, el resultado es un array de 3 elementos, ya que todos los elementos del segundo elemento del array2d son 3 elementos

print(array2d[1, 1:3]) # ingresamos el indice del elemento que queremos mostrar, en este caso los elementos desde el indice 1 hasta el indice 2 del segundo elemento del array2d, el resultado es un array de 2 elementos, ya que los elementos desde el indice 1 hasta el indice 2 del segundo elemento del array2d son 2 elementos

print(array2d[: , 1]) # ingresamos el indice del elemento que queremos mostrar, en este caso todos los elementos del segundo elemento de cada elemento del array2d, el resultado es un array de 3 elementos, ya que todos los elementos del segundo elemento de cada elemento del array2d son 3 elementos

print(array2d[:2, :2]) # ingresamos el indice del elemento que queremos mostrar, en este caso los elementos desde el indice 0 hasta el indice 1 de cada elemento del array2d, el resultado es un array de 4 elementos, ya que los elementos desde el indice 0 hasta el indice 1 de cada elemento del array2d son 4 elementos

print(array1d > 3) # ingresamos una condición para filtrar los elementos del array1d, en este caso los elementos mayores que 3, el resultado es un array de booleanos, ya que la comparación devuelve un valor booleano para cada elemento del array1d

print(array2d % 2 == 0) # ingresamos una condición para filtrar los elementos del array2d, en este caso los elementos pares, el resultado es un array de booleanos, ya que la comparación devuelve un valor booleano para cada elemento del array2d
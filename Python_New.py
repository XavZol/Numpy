import numpy as np
import pandas as pd 
import time 

df = pd.DataFrame({
    'Impares' : [1, 3, 5],
    'Pares' : [2, 4, 6]
})

print(df)

array_dp1 = df.values # con el metodo values de un dataframe podemos convertirlo a un array de numpy, el resultado es un array bidimensional con los mismos datos que el dataframe pero sin los indices ni las columnas
print(array_dp1)

arra_n2 = df.to_numpy() # otra forma de convertir un dataframe a un array de numpy, el resultado es el mismo que con el metodo values
print(arra_n2)

print(np.sqrt(df)) # con el metodo sqrt de numpy podemos calcular la raiz cuadrada de cada elemento del dataframe, el resultado es un nuevo dataframe con los mismos indices y columnas pero con los valores transformados

print(np.max(df)) # con el metodo max de numpy podemos calcular el valor maximo de cada columna del dataframe, el resultado es una serie con los mismos indices que el dataframe pero con los valores maximos de cada columna

df_desde_np = pd.DataFrame(array_dp1) #creamos un nuevo dataframe a partir del array creado con el metodo values
print(df_desde_np)

df_desde_np = pd.DataFrame(array_dp1, columns=['Col1', 'Col2']) #creamos un nuevo dataframe a partir del array creado con el metodo values y le asignamos nombres a las columnas
print(df_desde_np)
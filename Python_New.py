import numpy as np
import pandas as pd 
import time 

# nan dato faltante

array = np.array([1, 2, np.nan, 4, 5]) # crear un array con un valor faltante (nan)
print(array)

print(np.isnan(array)) # verificar si hay valores faltantes

print(np.mean(array)) # calcular la media del array, esto dará un resultado nan debido al valor faltante

print(np.nanmean(array)) # calcular la media ignorando el valor faltante

array_con_0 = np.where(np.isnan(array), 0, array) # reemplazar los valores faltantes con 0
print(array_con_0)

promedio = np.nanmean(array) # calcular el promedio del array ignorando los valores faltantes
array_con_promedio = np.where(np.isnan(array), promedio, array) # reemplazar los valores faltantes con el promedio del array
print(array_con_promedio) 

array_filtrado = array[np.isnan(array)] # filtrar los valores faltantes del array, esto dará un array vacío ya que no se incluyen los valores faltantes
print(array_filtrado)

array_filtrado1 = array[~np.isnan(array)] # filtrar los valores no faltantes del array, esto dará un array con los valores 1, 2, 4 y 5
print(array_filtrado1)
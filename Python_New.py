import numpy as np
import pandas as pd 
import time 

mi_array = np.array([1, 2, 3, 4, 5])
print(mi_array)

print(type(mi_array))

lista_grande = list(range(1000000))
array_grande = np.array(lista_grande)

print(type(lista_grande))
print(type(array_grande))

inicio_lista = time.time() # Inicia el tiempo para la lista
for i in lista_grande: # Itera sobre cada elemento de la lista y lo eleva al cuadrado
    i ** 2 # Eleva al cuadrado cada elemento de la lista
fin_lista = time.time() # Finaliza el tiempo para la lista
print("Tiempo lista: ", fin_lista - inicio_lista) # Imprime el tiempo que tomó iterar sobre la lista y elevar cada elemento al cuadrado

inicio_array = time.time() # Inicia el tiempo para el array
array_grande ** 2
fin_array = time.time() # Finaliza el tiempo para el array
print("Tiempo array: ", fin_array - inicio_array) # Imprime el tiempo que tomó elevar al cuadrado cada elemento del array



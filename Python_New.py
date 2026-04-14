import numpy as np
import pandas as pd 
import time 

ruta = r"C:\Users\javie\OneDrive\Desktop\Excel_DB\medallas.csv"
array = np.genfromtxt(ruta, delimiter=',') # lee el archivo CSV y lo convierte en un array de NumPy, utilizando la coma como delimitador
print(array)

array1 = np.genfromtxt(ruta, delimiter=',', filling_values=0) # hace que los valores vacíos se llenen con 0
print(array1)

array1 = np.genfromtxt(ruta, delimiter=',', filling_values=0, skip_header=1) # hace que se salte la primera fila (cabecera) y los valores vacíos se llenen con 0
print(array1)

array1 = np.genfromtxt(ruta, delimiter=',', filling_values=0, skip_header=1, dtype=int) # hace que se salte la primera fila (cabecera), los valores vacíos se llenen con 0 y los datos se conviertan a enteros
print(array1)

array_ejemplo = np.array([[1, 2, 3], 
                            [4, 5, 6]])
print(array_ejemplo)

ruta2 = r"C:\Users\javie\OneDrive\Desktop\Excel_DB\mis_datos.csv"
np.savetxt(ruta2, array_ejemplo, delimiter=',', fmt='%d') # guarda el array en un archivo CSV, utilizando la coma como delimitador y el formato de enteros)
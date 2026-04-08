import numpy as np
import pandas as pd 

ruta = (r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Ciudades.csv')
df = pd.read_csv(ruta)

mean_population = df['Población'].mean() # Calcular la media de la columna 'Población'
print(f'{mean_population}')

mean_population = np.round(df['Población'].mean()) # Redondear el resultado a un número entero
print(f'{mean_population}')

min_visitors = np.min(df['Visitantes']) # Calcular el valor mínimo de la columna 'Visitantes'
print(f'{min_visitors}')

np.max(df['Visitantes']) # Calcular el valor máximo de la columna 'Visitantes'
print(f'{np.max(df["Visitantes"])}')

print(dir(np)) # Mostrar los métodos disponibles en el módulo numpy



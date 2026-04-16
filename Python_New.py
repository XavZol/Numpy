import numpy as np
import pandas as pd 
import time 

ruta = r"C:\Users\javie\OneDrive\Desktop\Excel_DB\meteo.csv"
df = pd.read_csv(ruta)
print(df)

print(df.head())
print(df.describe())

temperatura = df['Temperatura'].to_numpy(copy=True)
precipitacion = df['Precipitación'].to_numpy(copy=True)
humedad = df['Humedad'].to_numpy(copy=True)

print(temperatura)

# Identificar los datos faltantes en los arrays, y reemplazarlos por el promedio de los valores del repectivo array
temp_nulo = np.isnan(temperatura)
precip_nulo = np.isnan(precipitacion)
humedad_nulo = np.isnan(humedad)

print(temp_nulo)
print(precip_nulo)
print(humedad_nulo)

# Identificar el promedio de cada array, 
temp_promedio = np.nanmean(temperatura)
precip_promedio = np.nanmean(precipitacion)
humedad_promedio = np.nanmean(humedad)

print(temp_promedio)
print(precip_promedio)
print(humedad_promedio)

# Reemplazar los valores nulos con el promedio del array
temperatura[temp_nulo] = temp_promedio 
precipitacion[precip_nulo] = precip_promedio
humedad[humedad_nulo] = humedad_promedio

print(temperatura)
print(precipitacion)
print(humedad)

# Esta otra forma es más eficiente ya que no modifica el array original, sino que crea uno nuevo con los valores corregidos
temp_correg = np.where(np.isnan(temperatura), temp_promedio, temperatura)
print(temp_correg)

#temperatura promedio es lo mismo que temp_promedio, pero con el array corregido, es decir, sin los valores nulos
temp_promedio = np.mean(temperatura)
print(temp_promedio)

# Calcular la suma total de la precipitación, utilizando el array corregido
precipitacion_total = np.sum(precipitacion)
print(precipitacion_total)

# Máxima húmedad registrada
humedad_maxima = np.max(humedad)
print(humedad_maxima)

# Máxima temperatura registrada
temperatura_maxima = np.max(temperatura)
print(temperatura_maxima)

# Registro correspondiente a la temperatura máxima
registro_temp_max = np.where(temperatura == temperatura_maxima)[0][0]
print(registro_temp_max)

# Fecha correspondiente al registro más caluroso
fecha_mas_caluroso = df.iloc[registro_temp_max]['Fecha']
print(fecha_mas_caluroso)


# Fecha más fría
fecha_mas_fria = df.iloc[np.where(temperatura == np.min(temperatura))[0][0]]['Fecha']
print(fecha_mas_fria)

# Exportar los resultados a un nuevo archivo CSV
resultados = pd.DataFrame({
    'Metrica': ['Temperatura Promedio', 'Precipitación Total', 'Húmedad Máxima', 'Día Más Caluroso', 'Día Más Frío'],
    'Valor': [temp_promedio, precipitacion_total, humedad_maxima, fecha_mas_caluroso, fecha_mas_fria]
})

# Guardar los archivos en un nuevo CSV
resultados.to_csv('Resultados análisis metereológico.csv', index=False)
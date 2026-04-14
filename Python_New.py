import numpy as np
import pandas as pd 
import time 

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(array)

print(array.shape)

array_mod = array.reshape(3, 3) #reshape the array to 3 rows and 3 columns
print(array_mod)

array_mod2 = array.reshape(-1, 3) #reshape the array to 3 columns and as many rows as needed (in this case, 3 rows)
print(array_mod2)

array_volteado = array_mod2.transpose() #transpose the array, which means to flip it over its diagonal. The rows become columns and the columns become rows.
print(array_volteado)

array_chat = array_mod.flatten() # flatten the array, which means to convert it into a 1D array. The shape of the array will be (9,) because it has 9 elements.
print(array_chat)

array_ravel = array_mod.ravel() # ravel the array, which means to convert it into a 1D array. The shape of the array will be (9,) because it has 9 elements. The difference between flatten and ravel is that flatten returns a copy of the array, while ravel returns a view of the array. This means that if you modify the ravelled array, it will also modify the original array, while if you modify the flattened array, it will not modify the original array.
print(array_ravel)
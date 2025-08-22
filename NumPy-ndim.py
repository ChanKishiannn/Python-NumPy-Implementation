# Count how many dimentions are on the array

import numpy as np

list1 = np.array([1])                       # 1D array
list2 = np.array([[1],[2]])                 # 2D array
list3 = np.array([[[1]],[[2]],[[3]]])       # 3D array

print(list1.ndim) # Output: 1
print(list2.ndim) # Output: 2
print(list3.ndim) # Output: 3

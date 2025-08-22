import numpy as np

arr = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                [["J","K","L"],["M","N","O"],["P","Q","R"]],
                [["S","T","U"],["V","W","X"],["Y","Z","@"]]])

print(f"The dimension of the array is: {arr.ndim}")
print(f"The structure of the array is: {arr.shape}")

# Multi-Dimensional Indexing: used to access values inside a multi-dimensional array
print(f"The element that is at (2,2,1) is: {arr[2,2,1]}") 
# Explanation:
#   (2,2,1) means → 3rd block (index 2), 3rd row (index 2), and 2nd column (index 1)
#   So it goes: Block → Row → Column

import numpy as np

arr = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                [["J","K","L"],["M","N","O"],["P","Q","R"]],
                [["S","T","U"],["V","W","X"],["Y","Z","@"]]])

word = arr[0, 0, 2] + arr[0,2,1] + arr[0,0,0] + arr[1,1,1]

#Printing the variable "word" that use multi-dimensional indexing to access the letters inside the array
print(word) 

import numpy as np


# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(matrix).type)
print(np.array(matrix).shape)
res = np.array(matrix).flatten()
print(res)


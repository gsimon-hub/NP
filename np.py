import numpy as np

arr1 = np.array(list(range(1, 10)), dtype=int)

arr = np.full((9, 9), np.nan)

# print(arr1.ndim)
# print(arr1)
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(data)
# print(data[:, 2])
# print(data[0:2])

# print(data[0:2, 0:2])
# print(data[0:2, 0:2].flatten())

arr[0, 0] = 9
print(arr)
print(np.setdiff1d(arr1, arr[0:2, 0:2].flatten()))
arr[1, 1] = np.setdiff1d(arr1, arr[0:2, 0:2].flatten())
print(arr)

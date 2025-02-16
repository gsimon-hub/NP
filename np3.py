import numpy as np
import math
import copy
from functools import reduce
from cacl_mtrx import calcMatrix, caclColumn, caclRow, finalGrid

st = set(range(1, 10))
print(st)

arr = np.full((9, 9, 9), np.nan)
arr[0, 1, 0] = 8
arr[1, 0, 0] = 2
arr[1, 3, 0] = 6
arr[1, 8, 0] = 3
arr[2, 1, 0] = 4
arr[2, 2, 0] = 9
arr[2, 3, 0] = 7
arr[2, 6, 0] = 6
arr[3, 1, 0] = 3
arr[3, 3, 0] = 2
arr[3, 4, 0] = 6
arr[3, 6, 0] = 1
arr[4, 3, 0] = 9
arr[4, 7, 0] = 2
arr[4, 8, 0] = 5
arr[5, 2, 0] = 7
arr[5, 4, 0] = 4
arr[6, 1, 0] = 1
arr[6, 4, 0] = 7
arr[6, 6, 0] = 3
arr[7, 1, 0] = 7
arr[7, 5, 0] = 3
arr[7, 6, 0] = 8
arr[8, 3, 0] = 5
# refresh
# arr[1, 1, 0] = 5
# arr[1, 2, 0] = 1
# arr[0, 0, 0] = 7
# arr[0, 2, 0] = 6
# arr[2, 0, 0] = 3
# arr[4, 1, 0] = 6
# arr[5, 6, 0] = 9
# arr[5, 1, 0] = 2
# arr[8, 1, 0] = 9
# arr[8, 2, 0] = 3
# arr[3, 0, 0] = 9
# arr[4, 4, 0] = 3
# arr[0, 3, 0] = 3
# arr[0, 6, 0] = 5
# arr[5, 7, 0] = 3
# arr[2, 4, 0] = 5
# arr[8, 6, 0] = 2
# arr[5, 8, 0] = 6

# append value based on the output, run for the final result
arr[6, 8, 0] = 9
arr[2, 5, 0] = 9

rList = []
rmList = []
cList = []


def fndIndex(str, lst):
    for item in lst:
        if str in item and len(item) > 1:
            # if str in item:
            return lst.index(item)


mList = []

for m in (3, 6, 9):
    for n in (3, 6, 9):
        # 9-matrix
        # print(arr[0:3, 0:3].flatten())
        # matrix = arr[0:3, 0:3].flatten()
        matrix = arr[m - 3 : m, n - 3 : n].flatten()
        mList.append(matrix)
    rmList.append(mList)
    mList = []
# print(np.array(rmList).shape)
# print(rmList[1][2])

for i in range(0, 9):
    # row
    # print(arr[0:1, 0:9].flatten())
    # row = arr[0:1, 0:9].flatten()
    row = arr[i : i + 1, 0:9].flatten()

    # column
    # print(arr[0:9, 0:1].flatten())
    # column = arr[0:9, 0:1].flatten()
    column = arr[0:9, i : i + 1].flatten()
    rList.append(row)
    cList.append(column)

myList = []
result = []
# nList = []
# nRslt = []
for x in range(0, 9):
    l = math.floor(x / 3)
    for y in range(0, 9):
        z = math.floor(y / 3)
        # Union 3 lists, reduce util
        newData = reduce(np.union1d, (rmList[l][z], rList[x], cList[y]))
        # remove np.nan elements from array
        setData = set(newData[np.isfinite(newData)])
        if len(st.difference(setData)) == 1:
            myList.append(st.difference(setData))
        else:
            myList.append({})
        # nList.append(st.difference(setData))
    result.append(myList)
    # nRslt.append(nList)
    myList = []
# newData = reduce(np.union1d, (matrix, row, column))
# setData = set(newData[np.isfinite(newData)])
# print(st.difference(setData))
# print(set(newData[np.isfinite(newData)]))

for i in range(0, 9):
    for b in range(0, 9):
        if arr[i][b][0] > 0:
            result[i][b] = {arr[i][b][0]}
    print(result[i])
    # print(set().union(*result[i]))
    # print(set().union(*result[i]))

mtxMID = []

nn = 1
while not np.array_equiv(np.array(result), np.array(mtxMID)):
    print(f"Running the {nn} times LOOP.")
    mtxMID = copy.deepcopy(result)
    result, nGrid = finalGrid(result)
    # caclRow(nGrid)
    calcMatrix(nGrid)
    caclRow(nGrid)
    caclColumn(nGrid)
    nn = nn + 1
    # print(result)

for i in range(0, 9):
    # print(result[i], "\n", nGrid[i])
    print(nGrid[i])

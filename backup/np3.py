import numpy as np
import math
import copy
from functools import reduce
from .cacl_mtrx import CaclMtrx

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

mList = []
rList = []
rmList = []
cList = []


def fndIndex(str, lst):
    for item in lst:
        if str in item and len(item) > 1:
            # if str in item:
            return lst.index(item)


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
for x in range(0, 9):
    l = math.floor(x / 3)
    for y in range(0, 9):
        z = math.floor(y / 3)
        newData = reduce(np.union1d, (rmList[l][z], rList[x], cList[y]))
        setData = set(newData[np.isfinite(newData)])
        myList.append(st.difference(setData))
    result.append(myList)
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

while not np.array_equiv(np.array(result), np.array(mtxMID)):
    mtxMID = copy.deepcopy(result)
    # process rows
    print("Rows are processing ...")
    for i in range(0, 9):
        tList = [list(item) for item in result[i]]
        unit = [item for sublist in tList for item in sublist]
        # unit.sort()
        # print(unit)
        cnt = [unit.count(x) for x in range(1, 10)]
        # print(cnt)
        for n in range(0, 9):
            if cnt[n] == 1:
                try:
                    z = fndIndex(n + 1, result[i])
                    if z:
                        x, y = i, z
                        print(n + 1, x, y)
                        arr[x][y][0] = n + 1
                        result[x][y] = {n + 1}
                except:
                    pass

    # process column
    print("Columns are processing ...")
    for i in range(0, 9):
        colMedium = [row[i] for row in result]
        colList = [list(item) for item in colMedium]
        unit = [item for sublist in colList for item in sublist]
        cnt = [unit.count(x) for x in range(1, 10)]
        # print(cnt)
        for m in range(0, 9):
            if cnt[m] == 1:
                try:
                    z = fndIndex(m + 1, colMedium)
                    if z:
                        x, y = z, i
                        print(m + 1, x, y)
                        result[x][y] = {m + 1}
                        arr[x][y][0] = m + 1
                except:
                    pass

    # process matrix
    print("Matrix process started ...")
    for m in (3, 6, 9):
        for n in (3, 6, 9):
            matrix = np.array(result)[m - 3 : m, n - 3 : n]
            mtxMedium = [i for s in matrix for i in s]
            mtxList = [list(item) for item in mtxMedium]
            unit = [item for sublist in mtxList for item in sublist]
            cnt = [unit.count(x) for x in range(1, 10)]
            # print(cnt)
            # print(mtxMedium)
            for i in range(0, 9):
                if cnt[i] == 1:
                    try:
                        z = fndIndex(i + 1, mtxMedium)
                        if z:
                            x, y = math.floor(z / 3) + m - 3, z % 3 + n - 3
                            print(i + 1, x, y)
                            result[x][y] = {i + 1}
                            arr[x][y][0] = i + 1
                    except:
                        pass
for i in range(0, 9):
    print(mtxMID[i])

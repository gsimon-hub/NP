import numpy as np
import math
from functools import reduce


def fndIndex(str, lst):
    for item in lst:
        if str in item and len(item) > 1:
            # if str in item:
            return lst.index(item)
        else:
            continue


def getMN(x, y):
    return math.floor(x / 3), math.floor(y / 3)


def remove_from_compre(item, ele):
    try:
        if len(item) > 1:
            item.remove(ele)
    except:
        return item


def caclRow(mtrx):
    print("Rows are processing ...")
    for i in range(0, 9):
        tList = [list(item) for item in mtrx[i]]
        unit = [item for sublist in tList for item in sublist]
        # unit.sort()
        # print(unit)
        cnt = [unit.count(x) for x in range(1, 10)]
        # print(cnt)
        for n in range(0, 9):
            if cnt[n] == 1:
                z = fndIndex(n + 1, mtrx[i])
                if z:
                    x, y = i, z
                    print(n + 1, x, y)
                    a, b = getMN(x, y)
                    mtxList = np.array(mtrx)[a * 3 : (a + 1) * 3, b * 3 : (b + 1) * 3]
                    mtrx[x][y] = {n + 1}
                    [remove_from_compre(item, n + 1) for row in mtxList for item in row]
                    [remove_from_compre(item[y], n + 1) for item in mtrx]
                    # print(
                    #     "relative 9-mtrx\n", [item for row in mtxList for item in row]
                    # )
                    # print("relative column\n", [item[y] for item in mtrx])

    return mtrx


def caclColumn(mtrx):
    # process column
    print("Columns are processing ...")
    for i in range(0, 9):
        colMedium = [row[i] for row in mtrx]
        colList = [list(item) for item in colMedium]
        unit = [item for sublist in colList for item in sublist]
        cnt = [unit.count(x) for x in range(1, 10)]
        # print(cnt)
        for m in range(0, 9):
            if cnt[m] == 1:
                z = fndIndex(m + 1, colMedium)
                if z:
                    x, y = z, i
                    print(m + 1, x, y)
                    a, b = getMN(x, y)
                    mtrx[x][y] = {m + 1}
                    mtxList = np.array(mtrx)[a * 3 : (a + 1) * 3, b * 3 : (b + 1) * 3]
                    [remove_from_compre(item, m + 1) for row in mtxList for item in row]
                    [remove_from_compre(item, m + 1) for item in mtrx[x]]
                    # print(
                    #     "relative 9-mtrx\n", [item for row in mtxList for item in row]
                    # )
                    # print("relative row\n", mtrx[x])


def calcMatrix(mtrx):
    # process matrix
    print("Matrix process started ...")
    for m in (3, 6, 9):
        for n in (3, 6, 9):
            matrix = np.array(mtrx)[m - 3 : m, n - 3 : n]
            mtxMedium = [i for s in matrix for i in s]
            mtxList = [list(item) for item in mtxMedium]
            unit = [item for sublist in mtxList for item in sublist]
            cnt = [unit.count(x) for x in range(1, 10)]
            # print(cnt)
            # print(mtxMedium)
            for i in range(0, 9):
                if cnt[i] == 1:
                    z = fndIndex(i + 1, mtxMedium)
                    if z:
                        x, y = math.floor(z / 3) + m - 3, z % 3 + n - 3
                        print(i + 1, x, y)
                        mtrx[x][y] = {i + 1}
                        # bug fix from m + 1 to i + 1, remove the wrong value
                        [remove_from_compre(item, i + 1) for item in mtrx[x]]
                        # [remove_from_compre(item, i + 1) for item in np.array(mtrx)[:, y : y + 1]]
                        [remove_from_compre(item[y], i + 1) for item in mtrx]
                        # print("relative column\n", [item[y] for item in mtrx])
                        # print("relative row\n", mtrx[x])


def getLst3(mtrx):

    mList = []
    rmList = []
    rList = []
    cList = []
    # 9-grid list
    for m in (3, 6, 9):
        for n in (3, 6, 9):
            matrix = np.array(mtrx)[m - 3 : m, n - 3 : n].flatten().tolist()
            # list of sets move to one list
            lstMtx = [item for set_ in matrix for item in set_]
            mList.append(lstMtx)
        rmList.append(mList)
        mList = []
    # row and column list
    for i in range(0, 9):
        mrow = np.array(mtrx)[i : i + 1, 0:9].flatten().tolist()
        row = [item for set_ in mrow for item in set_]
        mcolumn = np.array(mtrx)[0:9, i : i + 1].flatten().tolist()
        column = [item for set_ in mcolumn for item in set_]
        rList.append(row)
        cList.append(column)

    return rList, cList, rmList


def finalGrid(mtrx):

    grid = []
    myList = []
    nGrd = []
    nList = []
    st = set(range(1, 10))
    lst_3 = getLst3(mtrx)

    for x in range(0, 9):
        l = math.floor(x / 3)
        for y in range(0, 9):
            z = math.floor(y / 3)
            newData = reduce(np.union1d, (lst_3[0][x], lst_3[1][y], lst_3[2][l][z]))
            setData = set(newData)
            if mtrx[x][y] != {}:
                myList.append(mtrx[x][y])
                nList.append(mtrx[x][y])
            else:
                # myList.append(st.difference(setData))
                if len(st.difference(setData)) == 1:
                    myList.append(st.difference(setData))
                else:
                    myList.append({})
                nList.append(st.difference(setData))

        grid.append(myList)
        nGrd.append(nList)
        myList = []
        nList = []

    return grid, nGrd

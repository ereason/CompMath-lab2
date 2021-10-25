# Метод Гауссаю. Схема единствнного деления.
import numpy

def swapRows(matrix,v,i1,i2):
    buff = matrix[i1].copy()
    matrix [i1] = matrix [i2]
    matrix[i2] = buff

    buff = v[i1]
    v[i1] = v[i2]
    v[i2] = buff

def findPositiveItem(matrix,index):
    for i in range(index,len(matrix[index])):
        if matrix[i][index] != 0:
            return i
    return -1

def getResult(matrix,v):
    res = numpy.array([0.0]*len(v))
    for k in range(3 - 1, -1, -1):
        res[k] = (v[k] - sum([matrix[k][j] * res[j] for j in range(k, 3)])) / matrix[k][k]

    return res


def start(matrix,v):
    for col in range(0, len(matrix[0])):
        print(matrix)
        print(v)
        print()
        if matrix[col][col] == 0:
            buff = findPositiveItem(matrix,col)

            if buff == -1:
                continue

            swapRows(matrix,v,col,buff)



        for row in range(col+1, len(matrix)):
            v[row] = v[row] - v[col] * (matrix[row][col] / matrix[col][col])
            matrix[row] = matrix[row] - (matrix[col]) * (matrix[row][col] / matrix[col][col])

    return getResult(matrix,v)



# Итерационные методы. Метод простой итерации Якоби.
import numpy as np


def swapRows(matrix, v, i1, i2):
    buff = matrix[i1].copy()
    matrix[i1] = matrix[i2]
    matrix[i2] = buff
    buff = v[i1]
    v[i1] = v[i2]
    v[i2] = buff


def start(matrix, v, eps):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return ["На диагонали имеется 0 элемент", 0]

    x = [0.0 for i in range(len(v))]
    b = [v[i] / matrix[i][i] for i in range(len(v))]
    a = [[-matrix[i][j] / matrix[i][i] if i != j else 0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    norm = np.linalg.norm(a)
    if norm > 1:
        return ["Норма больше 1, процесс расходится", 0]

    count = 0
    while True:
        xPrev = x.copy()
        for i in range(len(x)):
            sum = 0
            for j in range(len(a[i])):
                sum += a[i][j] * x[j]
            x[i] = b[i] + sum

        d = [x[i] - xPrev[i] for i in range(len(x))]
        count += 1
        if (np.linalg.norm(d) <= eps * (1 - norm) / norm):
            break

    return [x, count]

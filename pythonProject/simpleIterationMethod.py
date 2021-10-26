#Итерационные методы. Метод простой итерации Якоби.
import numpy as np

def start(matrix,v):
    x = np.array([0.0] * len(v))

    norm1 = np.linalg.norm(matrix, ord=np.inf)
    print(norm1)
   #  еще нужна проверка 0 на диагонали
    if norm1 >= 1:
        return "норма > 1. равна " + str(norm1)


    while True:

        buff = x.copy()

        for i in range(0,len(v)):
            x[i] = v[i]/matrix[i][i] + sum([-matrix[i][j]/matrix[i][i] * buff[j] if i != j else 0 for j in range(0, len(v))])

        if(max(abs(x-buff)) < 0.01*(1-norm1)/norm1):
            return x



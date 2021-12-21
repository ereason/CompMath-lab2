import numpy
import numpy as np

import GaussMethod
import simpleIterationMethod

# норма матрцы из варианта 1 больше 1
# m = numpy.array([[1., 1., 15.],[4., 15., 1.],[15., 0, 1.] ])
# v = numpy.array([17., 16., 20.])
m = numpy.array([[3.2, 1., 1.], [1., 3.7, 1.], [1., 1., 4.2]])
v = numpy.array([2., 3., 5.])
eps = 0.0001

resTest = numpy.linalg.solve(m, v)
resGaus = GaussMethod.start(m.copy(), v.copy())
resSimpleIteration = simpleIterationMethod.start(m, v, eps)
print("Numpy: ", resTest)
print("Метод Гауса: ", resGaus)

for i in [1, 0.5, 0.1, 0.01, 0.0000001]:
    eps = i
    resSimpleIteration = simpleIterationMethod.start(m, v, eps)
    print("Метод простых итераций: ", resSimpleIteration[0], "eps: ", eps, "Итераций: ", resSimpleIteration[1])

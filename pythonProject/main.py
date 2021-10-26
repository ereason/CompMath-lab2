import numpy
import GaussMethod
import simpleIterationMethod

m = numpy.array([[1., 1., 15.], [4., 15., 1.], [15., 0., 1.]])
v = numpy.array([17., 20.,16.])

resTest = numpy.linalg.solve(m, v)
res = GaussMethod.start(m.copy(), v.copy())
print(resTest)
print(res)
print(simpleIterationMethod.start(m , v))

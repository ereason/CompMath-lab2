import numpy
import GaussMethod

m = numpy.array([[11., 1., 15.], [15., 5., 1.], [4., 15., 1.]])
v = numpy.array([17., 100., 20.])

resTest = numpy.linalg.solve(m, v)
res = GaussMethod.start(m,v)
print(resTest)
print(res)

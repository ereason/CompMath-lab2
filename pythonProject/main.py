import numpy


m = numpy.array([[1., 1., 15.], [15., 0., 1.], [4., 15., 1.]])
v = numpy.array([17., 16., 20.])

res = numpy.linalg.solve(m, v)

print(res)

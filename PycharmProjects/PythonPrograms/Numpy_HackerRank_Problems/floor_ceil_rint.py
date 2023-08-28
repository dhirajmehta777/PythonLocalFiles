import numpy
numpy.set_printoptions(legacy="1.13")
a=list(map(float, input().split()))
arr=numpy.array(a)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
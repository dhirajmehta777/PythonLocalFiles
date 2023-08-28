"""
Why use Numpy?
it provides efficient storage.
it also provides better ways of handling data for processing
it is fast
it is easy to learn
it uses relatively less memory to store data

"""
import numpy as np
#myarr=np.array([3,6,32,7])
myarr1=np.array([3,6,32,7], np.int8)#it means we use 8 byte integer, one more thing if we are providing
# dtype then the numbers in the list should not be more then 8 byte else it throw an error, if the number
# we are providing in the list are more the 8 bytes then we can use int64 or int32 also
myarr2=np.array([[3,6,32,7]], np.int32)#two dimensional array
print(myarr1[0])#single dimensional array
print(myarr2[0,1])#we have created a numpy array, maine ek python list se numpy array banaliya
print(myarr1.shape)
print(myarr2.shape)
print(myarr1.dtype)
print(myarr2.dtype)
#to know more about dtypes just search "numpy types references"
myarr2[0,1]=45
print(myarr2)

"""
we have 5 mechanisms to create array using numpy
1.conversin from other python structures
"""
listarray=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(listarray)
print(listarray.dtype)
print(listarray.shape)
print(listarray.size)
p=np.array({34,23,23})
print(p)

"""
2.Intrensic numpy array creation objects
"""
zeros=np.zeros((2,5))
print(zeros)#this will create a two dimensional array of 2,5
print(zeros.dtype)
print(zeros.shape)
print(zeros.size)

rng=np.arange(15)
print(rng)#this will provide an array containing numbers from 0 to n-1

lspace=np.linspace(1,5,12)
print(lspace)#this will provide us 12 elements having equally spaced

emp=np.empty((4,6))
print(emp)#it will provide random integers in an array of 4,6, hey aapko random elements se barke dega

emp_like=np.empty_like(lspace) #hey purane array ko copy karke uska ek empty array banadega
print(emp_like)

ide=np.identity(3)
print(ide)#this will create an two dimensional array of 3x3
print(ide.shape)

arr=np.arange(99)
print(arr)
print(arr.reshape(3,33))
print(arr.ravel())#this will print in single line that is from 2D to 1D array

"""
Numpy Axis:
"""
x=[[1,2,3],[4,5,6],[7,1,10]]
ar=np.array(x)
print(ar)
print(ar.sum(axis=0))
print(ar.sum(axis=1))
print(ar.T)#this will transpose the given matrix
print(ar.flat)#this will provide us a iterator
for items in ar.flat:
    print(items)

print(ar.ndim)#this will provide the no of dimensions
print(ar.size)#this will provide the no of elements in an array
print(ar.nbytes)#this will provide how many bytes the array ellements are consumed
print(ar.argmax())
print(ar.argmin())
print(ar.argmax(axis=0))
print(ar.argmax(axis=1))

one=np.array([1,3,4,634,2])
print(one.argmax())#this will provide us the index of max value in a 1D array
print(one.argmin())
print(one.argsort())

# some mathematical operations on munpy array
import numpy as np
from numpy import linalg as test
#dimenstion of array
a=np.array(([1,2,3],[4,5,6]))
l=a.ndim
print "the dimension of the array=",l
#size of elements in an array
k=a.itemsize
print "item size=",k
#type of the data
print "type of data=",a.dtype
#to find shape of array
print"shape of arrray=",a.shape
#to reshape array (3x2 as 2x3)
a=a.reshape(3,2)
print "reshape of array=",a
#slicing
a=np.array(([1,2,3,4],[3,4,5,6]))
print "getting the second element in oth index=",a[0,2]
print "the second element in each row=",a[0:,2]
#finding max,min&sum of given array
print "minimum value of given array=",a.min()
print "maximum value of given array=",a.max()
print "sum of the elements in numpy array=",a.sum()
#to find standard deviation of array
print "standard deviation of array=",np.std(a)
#square root of  elements in an array
print "square root of elements in an array",np.sqrt(a)

#concatenating array by using vertical and horizontal stacking

x=np.array(([1,2,3],[3,4,5]))
y=np.array(([1,2,3],[4,5,6]))
print "vertical stacking", np.vstack((x,y))
print "horizontal stacking" ,np.hstack((x,y))
#to convert nd array as single dimensinal array
z=np.array([[1,2,3],[4,5,6],[6,7,8]])
print "1d array",z.ravel()
#det ,rank and eigenvalues of the matrix
d=np.linalg.det(z)
print "det of the numpy array=",d
print "rank of numpy array=",np.linalg.matrix_rank(z)
#transpose of the matrix
s=z.T
print "transpose of a matrix",s
#tracing and sorting the numpy array
t=np.trace(z)
print "trace of array=",t
b=np.array([[9,8,7,6],[3,4,5,6]])
o=np.sort(b)
print "sorted array=",o
#inverse of matrix
w=np.linalg.inv(z)
print "inverse of z=",w








 


'''import array
arr=array.array('i',[12,67,89,23])
print(arr,type(arr))
arr.append(45)
print(arr)
arr.append(78)
print(arr)'''
import numpy
arr=numpy.array([12,45,78,23])
arr1=numpy.array([1,2,3],
                 [4,5,6],
                 [7,8,9])
print(arr)
print(arr1.shape)
print(arr.dtype)
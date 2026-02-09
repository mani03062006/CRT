'''import array
arr=array.array('i',[12,67,89,23])
print(arr,type(arr))
arr.append(45)
print(arr)
arr.append(78)
print(arr)

import numpy
arr=numpy.array([12,45,78,23])
arr1=numpy.array([1,2,3],
                 [4,5,6],
                 [7,8,9])
print(arr)
print(arr1.shape)
print(arr.dtype)
'''
'''
It is collection of homogenous data elements that can store under a single variable Python does not support arrays
 
Numpy:
NUmpy-->Numerical Python
it can easily access arrays
Mainly uses in ML,DS,AI applications'''
'''
import numpy as np
arr=np.array([12,45,78,23])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(5))
print("Even number list is: ",np.arange(2,10,2))
print("Odd number list is: ",np.arange(1,10,2))

n=int(input("Enter the size of array: "))
ele=list(map(int,input("Enter the elements of array: ").split()))
print("Array elements are: ",np.array(ele))
'''
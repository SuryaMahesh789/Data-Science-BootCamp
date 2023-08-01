# 1.Getting started with Numpy

# what is numpy
# Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.
# Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data.


# Difference between the list and numpy array
# A list in Python is a linear data structure that can hold heterogeneous elements they do not require to be declared and are flexible to shrink and grow. On the other hand, an array is a data structure which can hold homogeneous elements, arrays are implemented in Python using the NumPy library. Arrays require less memory than list.

# The similarity between an array and a list is that the elements of both array and a list can be identified by its index value.

import numpy as np

l=[1,2,3,4,5]
print(l)
print(type(l))

print("\n")

arr=np.array(l)

print("\n")
print(arr)

print("\n")
print(type(arr))

a=np.array([1,2,3,4,5])
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])


# numpy.ndarray.ndim() function return the number of dimensions of an array.
print(a)
print("Dimensions of Array a:- ",a.ndim)

print("\n")
print(type(a))

print(b)
print("Dimensions of Array b:- ",b.ndim)

print("\n")
print(type(b))

# shape will basically return us the total number of rows and columns of the array in a tuple format (number of rows, number of columns)

# size will tell us the total number of elements or values present in the array

# dtype will tell us the data type of values which the array is containing

print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)


print("\n")

print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)


print("\n")

# The numpy.zeros() function returns a new array of given shape and type, with zeros. Syntax:

# numpy.zeros(shape, dtype = None, order = 'C')
print("\n")
a=np.zeros(2,dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.zeros([2,2],dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.zeros([3,3],dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.zeros([2,3],dtype=float)
print("Matrix : \n",a)

# The numpy.ones() function returns a new array of given shape and type, with ones. Syntax:

# numpy.ones(shape, dtype = None, order = 'C')
print("\n")
a=np.ones(2,dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.ones([2,2],dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.ones([3,3],dtype=int)
print("Matrix : \n",a)

print("\n")
a=np.ones([2,3],dtype=float)
print("Matrix : \n",a)

print("\n")


# 2.Reshape and Random Number Generator


# numpy.random.random() is one of the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).

# Syntax : numpy.random.random(size=None)

# Parameters :
# size : [int or tuple of ints, optional] Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. Default is None, in which case a single value is returned.

# Return : Array of random floats in the interval [0.0, 1.0). or a single such random float if size not provided.

a=np.random.random()
print(a)

print("\n")

a=np.random.random(5)
print(a)

print("\n")

# The arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. [Start, Stop) 

# Parameters : 

# start : [optional] start of interval range. By default start = 0
# stop  : end of interval range
# step  : [optional] step size of interval. By default step size = 1,  
# For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
# dtype : type of output array
# Return: 

# Array of evenly spaced values.
# Length of array being generated  = Ceil((Stop - Start) / Step) 

a=np.arange(4)
print(a)

print("\n")


a=np.arange(3,10)
print(a)

print("\n")

a=np.arange(3,10,2)
print(a)

print("\n")


a=np.arange(4,20)
print(a)

print("\n")

print(a.size)

print(a.reshape(4,4))

print("\n")
print(a.reshape(2,8))

print("\n")


# The numpy.reshape() function shapes an array without changing the data of the array.

# Syntax:

# numpy.reshape(array, shape, order = 'C')
# Parameters : 

# array : [array_like]Input array
# shape : [int or tuples of int] e.g. if we are arranging an array with 10 elements then shaping
#         it like numpy.reshape(4, 8) is wrong; we can do numpy.reshape(2, 5) or (5, 2)
# order  : [C-contiguous, F-contiguous, A-contiguous; optional]         
#          C-contiguous order in memory(last index varies the fastest)
#          C order means that operating row-rise on the array will be slightly quicker
#          FORTRAN-contiguous order in memory (first index varies the fastest).
#          F order means that column-wise operations will be faster. 
#          ‘A’ means to read / write the elements in Fortran-like index order if,
#          array is Fortran contiguous in memory, C-like order otherwise
# Return Type: 

# Array which is reshaped without changing the data.

print("\n Input Array -1D Array")
a=np.arange(8)
print(a)

print("\n")

print("\n reshaped Array -2D Array")
a=np.arange(8).reshape(2,4)
print(a)

print("\n")

print("\n reshaped Array -2D Array")
a=np.arange(8).reshape(4,2)
print(a)

print("\n")

print("\n Reshaped Array -3D Array")
a=np.arange(8).reshape(2,2,2)
print(a)

print("\n")



# 3. Arithmetic Operations on Array

# NumPy achieves its fast implementation using vectorization. One of the important features of NumPy arrays is that a developer can perform the same mathematical operation on every element with a single command.

# Addition

a=np.array([1,2,3,4,5])
b=np.array([1,1,1,1,1])
print(a+b)

print("\n")

c=np.add(a,b)
print(c)

print("\n")

a=np.array([1,1,1,1,1])
b=np.array([3,3,3,3,3])
c=np.array([2,2,2,2,2])

print(a+b+c)

print("\n")

print(np.add(a,b,c))

print("\n")

# Subraction

a=np.array([1,2,3,4,5])
b=np.array([1,1,1,1,1])
print(a-b)

print("\n")

c=np.subtract(a,b)
print(c)

print("\n")

a=np.array([1,1,1,1,1])
b=np.array([3,3,3,3,3])
c=np.array([2,2,2,2,2])

print(a+c-b)

print("\n")

# Multiplication

a=np.array([1,2,3,4,5])
b=np.array([1,1,1,1,1])
print(a*b)

print("\n")

c=np.multiply(a,b)
print(c)

print("\n")

a=np.array([1,1,1,1,1])
b=np.array([3,3,3,3,3])
c=np.array([2,2,2,2,2])

print(a*b*c)

print("\n")

# division

a=np.array([2,4,6,8,10])
b=np.array([2,2,2,2,2])
print(a/b)

print("\n")

c=np.divide(a,b)
print(c)

print("\n")

# find the maximum element. To do this we have to use numpy.max(“array name”) function. 

# Syntax: 

# numpy.max(arr)

#  finding the minimum element use numpy.min(“array name”) function.

# Syntax:

# numpy.min(arr)

arr=np.array([1,2,3,4,5,6,7,8,9,10])

print("Maximum :-",np.max(arr))

print("Minimum :- ",np.min(arr))


print("")
arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print("Maximum :-",np.max(arr))

print("Minimum :- ",np.min(arr))

# if we want to find the maximum or minimum from the rows or the columns then we have to add 0 or 1. See how it works: 

# maximum_element = numpy.max(arr, 0)
# maximum_element = numpy.max(arr, 1)
# If we use 0 it will give us a list containing the maximum or minimum values from each column. 
# Here we will get a list like [11 81 22] which have all the maximum numbers each column. 

# If we use 1 instead of 0, will get a list like [11 16 81], which contain the maximum number from each row.

print("")
arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr)
print("Maximum among columns of array :-",np.max(arr,0))

print("Minimum among columns of array :-",np.min(arr,0))

print("Maximum among rows of array :-",np.max(arr,1))

print("Minimum among rows of array :-",np.min(arr,1))


# 4. Array Sorting

# There are multiple ways in Numpy to sort an array, based on the requirement using Python.
# Let’s try to understand them with the help of different methods. In this article, we will see How to sort a Numpy Array in Python.

# Sort a Numpy Array using the sort()
# Here we sort the given array based on the axis using the sort() method i.e. create a sorted copy of the given numpy array. 

# Sorting axis 0 = column wise adjusts the elements and rearranges into new array with shape as the input array
# Sorting axis -1 = row wise adjusts the elements and rearranges into new array with shape as the input array
# Sorting axis None = takes all the elements and sorts them into ascending order and rearranges into 1 Dimensional array

a=np.array([[12,15],[10,1]])
print("Input array:- ")
print(a)
print()

print("Sorted array axis 0 first axis:- ")
print(np.sort(a,axis=0))
print()

print("Sorted array axis -1 last axis:- ")
print(np.sort(a,axis=-1))
print()

print("Sorted array axis -1 none axis:- ")
print(np.sort(a,axis=None))
print()

# Sorting axis 0 = column wise adjusts the elements and rearranges into new array with shape as the input array
# Sorting axis -1 = row wise adjusts the elements and rearranges into new array with shape as the input array
# Sorting axis None = takes all the elements and sorts them into ascending order and rearranges into 1 Dimensional array

a=np.array([[1,2,3],[4,8,6],[9,7,5]])

print("Input array:- ")
print(a)
print()

print("Sorted array axis 0 first axis:- ")
print(np.sort(a,axis=0))
print()

print("Sorted array axis -1 last axis:- ")
print(np.sort(a,axis=-1))
print()

print("Sorted array axis -1 none axis:- ")
print(np.sort(a,axis=None))
print()

# We can choose which type of sorting we want perform using the kind parameter inside the sort function.
# We can either choose between quicksort, mergesort and heapsort.

arr = np.array([[7,3,8,6,4], [7,2,9,8,6],[5,4,2,3,1]])
print("Input array:- ")
print(arr)
print()

print("Sorted array axis 0 using mergesort:- ")
print(np.sort(arr , axis = 0, kind = 'mergesort'))
print()

print("Sorted array axis 1 using quicksort:- ")
print(np.sort(arr , axis = 1, kind = 'quicksort'))
print()

print("Sorted array axis -1 using quicksort:- ")
print(np.sort(arr , axis = -1, kind = 'quicksort'))
print()

print("Sorted array axis none using heapsort:- ")
print(np.sort(arr ,axis=None, kind = 'heapsort'))


print(np.sort(arr, kind = 'heapsort'))

print()

# Array Merging

# numpy.vstack() function is used to stack the sequence of input arrays vertically to make a single array.

# Syntax : numpy.vstack(tup)

# Parameters :
# tup : [sequence of ndarrays] Tuple containing arrays to be stacked. The arrays must have the same shape along all but the first axis.

# Return : [stacked ndarray] The stacked array of the input arrays.

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a,"\n")
print(b,"\n")

print(np.vstack((a,b)),"\n")

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[-1,-2,-3],[-4,-5,-6]])

print(a,"\n")
print(b,"\n")

print(np.vstack((a,b)),"\n")


# numpy.hstack() function is used to stack the sequence of input arrays horizontally (i.e. column wise) to make a single array.

# Syntax : numpy.hstack(tup)

# Parameters :
# tup : [sequence of ndarrays] Tuple containing arrays to be stacked. The arrays must have the same shape along all but the second axis.

# Return : [stacked ndarray] The stacked array of the input arrays.

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a,"\n")
print(b,"\n")

print(np.hstack((a,b)),"\n")

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[-1,-2,-3],[-4,-5,-6]])

print(a,"\n")
print(b,"\n")

print(np.hstack((a,b)),"\n")


# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

# Syntax : numpy.concatenate((arr1, arr2, …), axis=0, out=None)
# Parameters :
# arr1, arr2, … : [sequence of array_like] The arrays must have the same shape, except in the dimension corresponding to axis.
# axis : [int, optional] The axis along which the arrays will be joined. If axis is None, arrays are flattened before use. Default is 0.
# out : [ndarray, optional] If provided, the destination to place the result. The shape must be correct, matching that of what concatenate would have returned if no out argument were specified.
# Return : [ndarray] The concatenated array.


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

print(arr1,"\n")
print(arr2,"\n")


arr=np.concatenate((arr1,arr2),axis=0)
print("concatenation on axis 0:- column wise")
print(arr,"\n")

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

print(arr1,"\n")
print(arr2,"\n")

print("concatenation on axis 1:- row wise")
arr=np.concatenate((arr1,arr2),axis=1)

print(arr,"\n")





# numpy.vsplit() function split an array into multiple sub-arrays vertically (row-wise). vsplit is equivalent to split with axis=0 (default), the array is always split along the first axis regardless of the array dimension.

# Syntax : numpy.vsplit(arr, indices_or_sections)
# Parameters :
# arr : [ndarray] Array to be divided into sub-arrays.
# indices_or_sections : [int or 1-D array] If indices_or_sections is an integer, N, the array will be divided into N equal arrays along axis.
# If indices_or_sections is a 1-D array of sorted integers, the entries indicate where along axis the array is split
# Return : [ndarray] A list of sub-arrays.

print("np.vsplit\n")
arr=np.arange(9.0).reshape(3,3)
print(arr,"\n")

a=np.vsplit(arr,1)

print(a,"\n")

arr=np.arange(16).reshape(4,4)
print(arr,"\n")

a=np.vsplit(arr,2)

print(a,"\n")

# numpy.hsplit() function split an array into multiple sub-arrays horizontally (column-wise). hsplit is equivalent to split with axis=1, the array is always split along the second axis regardless of the array dimension.

# Syntax : numpy.hsplit(arr, indices_or_sections)
# Parameters :
# arr : [ndarray] Array to be divided into sub-arrays.
# indices_or_sections : [int or 1-D array] If indices_or_sections is an integer, N, the array will be divided into N equal arrays along axis.
# If indices_or_sections is a 1-D array of sorted integers, the entries indicate where along axis the array is split
# Return : [ndarray] A list of sub-arrays.

print("np.hsplit\n")

arr=np.arange(9.0).reshape(3,3)
print(arr,"\n")

a=np.hsplit(arr,1)

print(a,"\n")

arr=np.arange(16).reshape(4,4)
print(arr,"\n")

a=np.hsplit(arr,2)

print(a,"\n")

# Arrays Slicing - DAP

# In Python, array slicing is a common practice and it is the most used technique for programmers to solve efficient problems. Consider a python numpy array, In-order to access a range of elements in an array, you need to slice an array. One way to do this is to use the simple slicing operator i.e. colon(:)

# With this operator, one can specify where to start the slicing, where to end, and specify the step. List slicing returns a new list from the existing list.

# Syntax:

# Array[ Initial : End : IndexJump ]


arr=np.array([1,2,3,4,5,6,7,8,9,10])

print(arr,"\n")

print(arr[3:],"\n")

print(arr[:-3],"\n")

print(arr[3:-3],"\n")

print(arr[:],"\n")

# If we want to access a specific element or data from a 2 Dimension array
# we can use the comma within the square brackets to indicate the row index
# in the first part and the column index in the second part [row index, column index].

arr=np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]])

print(arr,"\n")

# row index, column index - index starts from 0 

print(arr[3,1],"\n")


# The second output is a combination with slicing where we printed the array starting from the 2nd row(index 1)
# and 2nd column(index 1) and the rest of the elements which are coming in the upcoming indexes.

print(arr[1:,1:],"\n")

print(arr[:-1,:-1],"\n")

print(arr[2:,2:],"\n")

print(arr[:-2,:-2],"\n")

print(arr[1:3,1:3],"\n")


# Automating using Numpy

# We can use numpy arrays for automation that is the amount of code which we need to do for filtering a list is way more than that of a numpy array. Let us see with the help of an example.

# Say we have a list containing element 1 to 10. Now we want to print the all the elements which are greater than 5.


l=[1,2,3,4,5,6,7,8,9,10]

for i in l:
    if i<=5:
        print(i,end=" ")
        
print()

for i in l:
    if i >5:
        print(i,end=" ")
        
print()


#in a single line we have done the same thing which we did previously and this time without using the for loop

arr=np.array(l)

print(arr,"\n")

print(arr[arr<=5],"\n")

print(arr[arr>5],"\n")



# QUIZ 

import numpy as np 

arr=np.array([1,2,3,4,5])

print(arr)
arr=np.array((1,2,3,4,5))

print(arr)

print(arr.dtype)

# randn command generates random numbers following a ?
# Normalized Normal Distribution

l=list(arr)

print(l)

# which of the following is an essential argument to pass in the full() function of numpy array
# shape 
# value

a=np.array([6,7,5,8])

b=np.array([4,3,7,8])

c=np.dot(a,b)

print(c,"\n")

arr=np.array([[1,2,3],[5,6,7],[8,9,10]])

print(arr,"\n")

# get the transpose of the array by three ways 

print(np.transpose(arr),"\n")

print(arr.T,"\n")

print(arr.transpose(),"\n")

arr=np.array([[1,2,3],[5,6,7],[8,9,10]])

print(arr,"\n")

# get the reverse of the array by three ways 

print(np.flipud(arr),"\n")

arr=np.array([1,9,2,8,3,7,4,6,5])

print(arr,"\n")

# ascending order sorting 
print(np.sort(arr),"\n")

# descending orer sorting = ascending order and reverse it 
print(np.sort(arr)[::-1],"\n")

arr=np.array([1,2,3,4,5,6,7,8,9,10])

# get the all the odd indexed elements in the array 
print(arr[1::2],"\n")

# get the all the even indexed elements in the array 
print(arr[::2],"\n")


# stack 

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

print(np.stack((a,b),axis=0),"\n")

print(np.stack((a,b),axis=1),"\n")

# concatenate 

a=np.array([[1,2],[3,4]])

b=np.array([[5,6]])

print(a,"\n")

print(b,"\n")

print(np.concatenate((a,b),axis=0),"\n")

print(np.concatenate((a,b.T),axis=1),"\n")

# column_stack 


a=np.array([[1,2,3,4],[5,6,7,8]])

b=np.array([[1,1,1,1],[2,2,2,2]])

print(a,"\n")

print(b,"\n")

print(np.column_stack([a,b]),"\n")


# no for loop automation / complex operation in a simpler way 

a=np.array([1,2,3,4,5,6,7,8,9,10])

print(a,"\n")

print(a[a>5],"\n")

print(a[a%3==0],"\n")

# print all the even elements 
print(a[a%2==0],"\n")

# print all the odd elements 
print(a[a%2!=0],"\n")


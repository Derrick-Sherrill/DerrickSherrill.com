##VIDEO OUTLINE
"""
Why Use Numpy?
- Efficiency of large operations
- Many Packages based around numpy (Flash Packages on Screen)
"""

# Import Package for scientific computing
import numpy as np

"""Arrays"""
## Standard Arrays
numbers = np.array([[0,1,2],[3,4,5]])
strings = np.array([[6,'seven',8],[9,'ten',11]])
print(numbers)
print(strings)

## Structured arrays
structured_array = np.array([('One', 1, 1.01), ('Two', 2, 2.02)], dtype=[('text', 'U16'), ('number', 'int32'), ('decimal', 'float64')])
print(structured_array)

#Working with dtypes:
type = numbers.dtype #Check the dtype
print(type)

#Common dtypes
"""
bool_ = Boolean as byte
int32 = integers (-2147483648 to 2147483647)
int64 = integers (-9223372036854775808 to 9223372036854775807)
float32 = single precision float
float64 = double precision float
complex64 & complex128 = complex number data types
U16, U32, U64 = strings (unicode)
"""

## Intro to Array Shapes
print(numbers.shape) # (# of arrays, # of items in each array)
reshape = numbers.reshape(3,2)
transpose = numbers.transpose() #Show in Excel

print(reshape) # Notice difference between this reshape and transpose
print(transpose)

"""Indexing Arrays"""
array = np.array([0,1,2,3,4,5,6,7,8,9,10])
#Forward Slice (start:stop:step-size)
slice = array[1:9:2] #Remember Python Indexing Starts with 0, not 1
print(slice)
#Backwards steps
bslice = array[-2:2:-1]
naslice = array[0:1:-1] #Explain why this prints empty
print(bslice)
print(naslice)

""" Masking Arrays"""
#import masking
import numpy.ma as ma

#Masking - Combination of standard array and mask
x = np.array([1, 2, 3, -1, 5])
mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
print(mx)

#Conditional Masking
mc = ma.masked_where(x<0,x) 
print(mc)

""" Mathematical Functions """
import math
# Defining the arrays
array1 = np.array([1,2,3])
array2 = np.array([10,20,30])
array3 = np.array([-10,-20,-30])
array4 = np.array(['one','two','three'])
print(array1)
print(array2)
print(array3)
#Terminal prints of operations
print(np.sin(array1)) #Trig Functions
print(np.cumsum(array1)) #Cumulative sum of single array
print(np.add(array1, array2)) #Add two arrays to form new array
print(np.exp(array1, order=2)) # e^x
print(np.abs(array3)) #Absolute values of array
print(np.matrix(array1)) #change Array to Matrix
print(np.core.defchararray.upper(array4)) #Edit strings


#Count Business Days
date1 = '2019-03-01'
date2 = '2019-03-30'
print(np.busday_count(np.datetime64(date1), np.datetime64(date2)))

#financial Operations
print(np.fv((array1/100)/12,5*12, -500, -1000)) #fv(rate,periods, payment, present value)

#linear Algebra
print(np.dot(array1, array2))

#Logic Functions
print(np.greater(array1,array2))
print(np.less(array1, array2))

#random
random_array = np.random.rand(3,2)
print(random_array)

#Statistics
print(np.median(random_array))
print(np.average(random_array))


#Saving File

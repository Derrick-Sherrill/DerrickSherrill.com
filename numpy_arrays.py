import numpy as np

A = [1,2,3,4,5] # Creates a Python List of ints
B = [1.5,2.5,3.5] # Creates a Python list of floats
C = [1, 1.5, 2, 2.5, 3] # Creates a python list of floats, overwriting ints
print(type(C)) # Returns floats

ArrayA = np.array(A, dtype=np.int32)
ArrayB = np.array(B, dtype=np.float32) # Creates NumPy array and specifics data type
ArrayC = np.array(C)
#bool, int, float, complex
print(A)
print(ArrayA)
print(ArrayB)
print(ArrayC)

D = [[1,2],[3,4],[5,6],[7,8]] # Nested list operation
ArrayD = np.array(D, dtype=np.int32) # Assigns array data type
print(ArrayD)
print(ArrayD.shape) # returns shape of array

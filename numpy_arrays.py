import numpy as np

A = [1,2,3,4,5]
B = [1.5,2.5,3.5]
C = [1, 1.5, 2, 2.5, 3]
print(type(C))

ArrayA = np.array(A, dtype=np.int32)
ArrayB = np.array(B, dtype=np.float32)
ArrayC = np.array(C)
#bool, int, float, complex
print(A)
print(ArrayA)
print(ArrayB)
print(ArrayC)

D = [[1,2],[3,4],[5,6],[7,8]]
ArrayD = np.array(D, dtype=np.int32)
print(ArrayD)
print(ArrayD.shape)

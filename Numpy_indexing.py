import numpy as np

ListA = [0,1,2,3,4,5,6,7,8,9,10]
ListB = [11,12,13,14,15,16,17,18,19,20,21]
A = np.array(ListA, dtype=np.int32)
print(A)

#A[start:stop:step]
print(A[::1])

ListC = [ListA,ListB]
AB = np.array(ListC, dtype=np.int32)
print(AB.shape)

print(AB[1,2:4:1])

print(A[np.array([0,0,0,0,1,2,3])])

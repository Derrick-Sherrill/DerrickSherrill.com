import numpy as np

ListA = [1,2,3,4]
ListB = [-1,2,4,6]

A = np.array(ListA, dtype=np.int32)
B = np.array(ListB, dtype=np.int32)

print(A)

ListA2 = []
for element in ListA:
    element = element +1
    ListA2.append(element)

print(ListA2)

print(A+1)
print(np.add(A,B))
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(np.sqrt(A))

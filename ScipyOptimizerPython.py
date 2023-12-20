from scipy.optimize import root
from math import cos
from scipy.optimize import minimize
import numpy as np
from scipy.sparse import csr_matrix

def eqn(x):
    return x+cos(x)

my_root = root(eqn, 0)
print(my_root)

#Minizime method 
def eqn(x):
    return x**2 + x +2

my_min = minimize(eqn, 0, method='BFGS')
print(my_min)


#Sparse array
arr = np.array([0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

#Sparce matrix Methods

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).count_nonzero())

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)


arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)


arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)
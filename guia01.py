import numpy as np
import matplotlib.pyplot as plt

1 + 3
a = 7
b = a + 1
print('b = ', b)
# Vectores
v = np.array([1,2,3,-1])
w = np.array([2,3,0,5])
print('v + w = ', v + w)
print('2 * v = ', 2 * v)
print('v ** 2 = ', v ** 2)
# Matrices(ejecutar los comandos uno a uno para verlos resultados)
a = np.array([[1,2,3,4,5],[0,1,2,3,4],[2,3,4,5,6],[0,0,1,2,3],[0,0,0,0,1]])
print(a)
a[0:2,3:5]
a[:2,3:]
a[[0,2,4],:] # me devuelve la fila 0, 2 y 4 entera
ind = np.array([0,2,4]) 
a[ind,ind] # hace la interseccio y me devuelve el elem a[0,0], a[2,2], a[4,4]
print(a[ind, ind[:,None]]) #preguntar

# NUMEROS COMPLEJOS
im1 = 1j*1j
im2 = (1+2j)*1j

a = -3/2
b = 11/2
c = -3
xx = np.array([1,2,3])
yy = np.array([1,2,0])
x = np.linspace(0,4,100)
f = lambda t: a* t**2 + b * t + c
plt.plot(xx,yy, 'o', color = 'purple')
plt.plot(x, f(x))
plt.show()

# FUNCION PARA ESCALONAR MATRICES

import numpy as np

def row_echelon(M):
    """ Return Row Echelon Form of matrix A """
    A = np.copy(M)
    if (issubclass(A.dtype.type, np.integer)):
        A = A.astype(float)
    #A = M.astype(float)
    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

# Clase 05 Descomposición LU
import numpy as np

#Escribir funciones de Python que calculen la solución de un sistema:
# Ly = b siendo L triangular inferior.

def resolverSistemaTrianInf(L, b):
    n = L.shape[1]
    y = np.zeros(n)
    cantDistCeros = 0
    for i in range(n):
        y[i] = b[i]/L[i,i]
        for j in range(cantDistCeros):
            y[i] -= L[i,j] * y[j]/L[i,i]
        cantDistCeros += 1
    return y

L = np.array([[2, 0, 0, 0],
              [4, 5, 0, 0],
              [1, 5, 10, 0],
              [44, 3, 6, 8]])

b = np.array([10,4,2,9])

print(resolverSistemaTrianInf(L,b))

#Ux = y siendo U triangular superior

def resolverSistemaTrianSup(U, x):
    n = U.shape[1]
    y = np.zeros(n)
    cantDistCeros = 0
    for i in range(n-1, -1, -1):
        y[i] = x[i]/U[i,i]
        for j in range(cantDistCeros):
            y[i] -= U[i,n-j-1] * y[n-j-1] / U[i,i]
        cantDistCeros += 1
    return y,3


U = np.array([[2, 4, 1, 4],
              [0, 5, 5, 3],
              [0, 0, 10, 6],    
              [0, 0, 0, 8]])

x = np.array([10,4,2,9])

print(resolverSistemaTrianSup(U,x))

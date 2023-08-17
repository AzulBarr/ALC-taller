import numpy as np

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

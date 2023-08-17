import numpy as np

a = np.array([[1,2,1], [3,4,1]]) #tienen que ser filas del mismo tamaño

mlin, mcol = a.shape #devuelve una tupla con la cantidad de filas y columnas, se puede guardar en dos variables separadas.

# FUNCIONES DE MATRICES
def esCuadrada(a):
    nlin, ncol = a.shape
    return nlin == ncol

def traza(a):
    #chequea que es cuadrada
    if esCuadrada(a):
        tr = 0
        nlin, ncol = a.shape
        for i in range(nlin):
            tr += a[i,i]
        return tr
    else:
        print('la matriz no es cuadrada')
        return -9999
      
def esSimetrica(a):
    if esCuadrada(a):
        res = True
        nlin, ncol = a.shape
        for i in range(nlin):
            for j in range(ncol):
                if a[i,j] != a[j,i]:
                    res = False
        return res
    else:
        print('la matriz no es cuadrada')
        return -9999 

# EN OTRO ARCHIVO
import funciones
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,8]])

print(funciones.traza(a),a)

# JUPYTER NOTEBOOK

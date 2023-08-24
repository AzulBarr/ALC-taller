# Aritmética de punto flotante 
## Representacion de numeros en una computadora
### Naturales
Números en base 2.
### Enteros
Primer bit 0/1 para decir si es positivo o negativo.
### Racionales
Representacion de numeros con coma separando la parte entera y la parte decimal.
### Reales
Los numeros con decimales infinitos se separan en 3 partes: signo, exponente y mantisa. A los exponentes se le restan 127, los exponentes menores a 127 son negativos.
### Complejos
Se representan como dos números reales. El imaginario i se pone como j.

---
## Error numérico

Hay números que no puede representar bien en sistemas con 32 o 64 bits.

```python
print(0.3-0.2)
```
> 0.09999999999999998

Se puede elegir la cantidad de bits.

```python
import numpy as np
np.float32(11334232.0)
```
Aunque haya un margen de error chico, se puede acumular y generar problemas.

```python
import numpy as np
from math import sqrt

def igualdad(n1,n2):
    return n1 == n2

print(igualdad(0.1, 0.3-0.2))
```

> False

Debería ser verdadero, se puede arreglar con una tolerancia de error.

```python
def igualdad(n1,n2):
    ep = 0.0001
    return abs(n1 - n2) < ep
```
> True

## Características de float 64

* Máximo número flotante que puede representar Python: 1.7976931348623157e+308 
```python
np.finfo(float).max
```
* Mínimo flotante positivo [normalizado]: 2.2250738585072014e-308 
```python
np.finfo(float).tiny
```
* Mínimo flotante positivo [subnormal]: 5e-324 
```python
np.nextafter(0., 1.)
```
* Epsilon de máquina: 2.220446049250313e-16 = spacing(1)
```python
# El épsilon de máquina es el número de máquina más chico tal que 1 + eps es distinto de 1
np.finfo(float).eps

# Dem:
eps = np.finfo(np.double).eps
print('1 + ε =', 1 + eps)
print('1 + ε/2 =', 1 + eps/2,'\n')

print('¿1 + ε = 1?', 1 + eps == 1)
print('¿1 + ε/2 = 1?', 1 + eps/2 == 1)
```
> 1 + ε = 1.0000000000000002 

>1 + ε/2 = 1.0 

>¿1 + ε = 1? False

>¿1 + ε/2 = 1? True

## Funciones

```python
# muestra 22 cifras significativas
format(0.1, '.22f')
```
```python
import numpy as np
# muestra la distancia de un número al siguiente, hay menos espacio para los números cercanos a 0.
np.spacing(202)
```
## Complejos

```python
c1 = 1 + 2j
real = c1.real
imaginaria = c1.imag

def conjugado(c):
    return c.real - c.imag * 1j

def esReal(c):
    return conjugado(c) == c

def esImaginario(c):
    return conjugado(c) != c and c.real == 0

```

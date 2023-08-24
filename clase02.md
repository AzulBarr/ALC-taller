
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

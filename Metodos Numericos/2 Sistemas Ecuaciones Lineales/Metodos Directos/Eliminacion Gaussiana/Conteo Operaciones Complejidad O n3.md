---
title: Conteo Operaciones Complejidad O n3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - complejidad-algoritmica
draft: false
aliases:
  - Complejidad computacional
  - Operaciones de punto flotante
  - FLOP count
  - Orden cúbico
---

# Conteo de Operaciones y Complejidad $O(n^3)$

> [!definicion]
> El **conteo de operaciones** (o *FLOP count*) es el número de operaciones aritméticas de punto flotante (sumas, restas, multiplicaciones, divisiones) que ejecuta un algoritmo en función del tamaño del problema $n$. La **complejidad asintótica** describe el término dominante cuando $n \to \infty$.

En métodos numéricos para álgebra lineal, el conteo de operaciones es crucial porque determina la viabilidad práctica de un algoritmo para problemas de gran escala.

---

## Unidad de medida: FLOP

> [!definicion]
> Un **FLOP** (*Floating-point Operation*) es una operación aritmética elemental entre números de punto flotante:
> - Multiplicación: $a \times b$
> - División: $a / b$
> - Suma: $a + b$
> - Resta: $a - b$
> 
> En análisis de complejidad, típicamente se cuentan **multiplicaciones y divisiones** por separado de **sumas y restas**, aunque modernamente se usa "FLOP" para referirse a cualquier operación escalar.

Para matrices densas, el costo se expresa en términos de $n$ (dimensión) y se busca el **término dominante** cuando $n$ es grande.

> [!info]
> **Notación asintótica estándar.**
> - $O(n^3)$: El costo crece como $c \cdot n^3$ para alguna constante $c$.
> - $O(n^2)$: Crecimiento cuadrático.
> - $O(n \log n)$: Crecimiento casi lineal.
> 
> Las constantes ocultas en la notación $O$ son importantes en la práctica, pero el orden asintótico domina para $n$ grande.

---

## Conteo detallado: Eliminación Gaussiana sin pivoteo

Consideremos la [[Eliminacion Gaussiana]] aplicada a una matriz $A \in \mathbb{R}^{n \times n}$.

### Fase de eliminación (Forward Elimination)

En el paso $k$ ($k = 1, 2, \dots, n-1$):
1. **Cálculo de multiplicadores:** Para $i = k+1, \dots, n$:
   $$m_{ik} = \frac{a_{ik}}{a_{kk}} \quad \Rightarrow \quad n - k \text{ divisiones}$$

2. **Actualización de la submatriz:** Para $i = k+1, \dots, n$ y $j = k+1, \dots, n$:
   $$a_{ij} \leftarrow a_{ij} - m_{ik} \cdot a_{kj} \quad \Rightarrow \quad (n-k)^2 \text{ multiplicaciones y } (n-k)^2 \text{ restas}$$

3. **Actualización del vector $b$:** Para $i = k+1, \dots, n$:
   $$b_i \leftarrow b_i - m_{ik} \cdot b_k \quad \Rightarrow \quad n - k \text{ multiplicaciones y } n - k \text{ restas}$$

> [!teoria]
> **Conteo total para la eliminación (matriz $A$ solamente).**
> 
> Divisiones:
> $$\sum_{k=1}^{n-1} (n - k) = \frac{n(n-1)}{2} \approx \frac{n^2}{2}$$
> 
> Multiplicaciones y restas (operaciones $\times$ y $+$):
> $$\sum_{k=1}^{n-1} (n - k)^2 = \sum_{j=1}^{n-1} j^2 = \frac{(n-1)n(2n-1)}{6} \approx \frac{n^3}{3}$$
> 
> **Total para $A$:** $\approx \frac{n^3}{3}$ multiplicaciones $+$ $\frac{n^3}{3}$ sumas $= \frac{2n^3}{3}$ FLOPs.

Incluyendo el vector $b$:
- Multiplicaciones adicionales: $\sum_{k=1}^{n-1} (n-k) = \frac{n(n-1)}{2} \approx \frac{n^2}{2}$
- Sumas adicionales: $\frac{n^2}{2}$

**Total eliminación + término independiente:** $\approx \frac{2n^3}{3} + n^2$ FLOPs.

### Fase de sustitución regresiva

Para $i = n, n-1, \dots, 1$:
$$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij} x_j}{a_{ii}}$$

En el paso $i$:
- Multiplicaciones: $n - i$
- Sumas: $n - i$
- División: $1$

Total sustitución:
- Multiplicaciones y sumas: $\sum_{i=1}^{n} (n - i) = \frac{n(n-1)}{2} \approx \frac{n^2}{2}$
- Divisiones: $n$

**Total sustitución:** $\approx n^2$ FLOPs.

> [!teorema]
> **Complejidad total de la eliminación Gaussiana.**
> 
> Sumando ambas fases:
> $$\text{FLOPs totales} = \frac{2n^3}{3} + \frac{3n^2}{2} + O(n) \sim \frac{2n^3}{3}$$
> 
> Para $n$ grande, el término dominante es $\frac{2n^3}{3}$ FLOPs.

> [!ejemplo]
> **Costo para $n=1000$.**
> 
> $$\frac{2 \cdot 1000^3}{3} = \frac{2 \cdot 10^9}{3} \approx 6.67 \times 10^8 \text{ FLOPs}$$
> 
> En un procesador moderno ($\approx 10^9$ FLOPs/segundo), esto toma menos de un segundo.
> 
> Para $n=10000$:
> $$\frac{2 \cdot 10000^3}{3} \approx 6.67 \times 10^{11} \text{ FLOPs} \approx 11 \text{ minutos}$$
> 
> Para $n=100000$:
> $$\approx 6.67 \times 10^{14} \text{ FLOPs} \approx 185 \text{ horas}$$

Este crecimiento $O(n^3)$ hace que la eliminación Gaussiana sea **impráctica para matrices densas muy grandes** ($n > 50000$), motivando el uso de [[Metodos Iterativos]] o métodos para [[Relleno Matrices Dispersas|matrices dispersas]].

---

## Conteo con pivoteo parcial

El [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]] añade:
- **Comparaciones:** En el paso $k$, buscar el máximo en $n-k$ elementos.
- **Intercambios:** Intercambiar filas (punteros, no datos).

> [!info]
> **Costo del pivoteo parcial.**
> - Comparaciones: $\sum_{k=1}^{n-1} (n-k) = \frac{n^2}{2}$ comparaciones (no son FLOPs, pero consumen tiempo).
> - Intercambios: $O(n^2)$ en el peor caso, pero típicamente implementados con punteros ($O(1)$ por intercambio).
> 
> El costo adicional es $O(n^2)$, **despreciable** frente a $O(n^3)$ de la eliminación.

El [[Pivoteo Parcial Total Estabilidad|pivoteo total]], en cambio, requiere buscar el máximo en $(n-k)^2$ elementos en cada paso:
$$\sum_{k=1}^{n-1} (n-k)^2 \approx \frac{n^3}{3} \text{ comparaciones}$$
Este costo $O(n^3)$ adicional **duplica** el tiempo de ejecución, razón por la cual el pivoteo total rara vez se usa.

---

## Comparativa de complejidad: Métodos directos

| Método | FLOPs (orden dominante) | Notas |
|:---|:---:|:---|
| [[Eliminacion Gaussiana]] | $\frac{2}{3}n^3$ | Estándar para matrices densas |
| [[Factorizacion LU]] | $\frac{2}{3}n^3$ | Idéntico a Gauss, reutilizable |
| [[Factorizacion Cholesky Matrices Definidas Positivas \|Cholesky]] | $\frac{1}{3}n^3$ | Solo para simétricas definidas positivas |
| [[Factorizacion QR]] (Householder) | $\frac{4}{3}n^3$ | Más estable, útil para mínimos cuadrados |
| [[Factorizacion QR]] (Gram-Schmidt) | $2n^3$ | Inestable numéricamente |
| [[Valores Singulares y Descomposicion SVD \|SVD]] | $\approx 20n^3$ | Máxima estabilidad, muy costoso |
| [[Determinante y Matriz Inversa \|Inversa explícita]] | $n^3$ | Rara vez necesaria; mejor resolver sistema |

> [!warning]
> **Nunca calcular $A^{-1}$ para resolver $Ax = b$.**
> Calcular $A^{-1}$ requiere $\approx n^3$ FLOPs y luego $x = A^{-1}b$ requiere $n^2$. Resolver directamente con eliminación Gaussiana o LU cuesta $\frac{2}{3}n^3$ y es numéricamente más estable.

---

## Resolución de múltiples sistemas: Ventaja de LU

Si se necesita resolver $Ax = b_i$ para $m$ vectores $b_i$ diferentes:

| Estrategia | Costo |
|:---|:---|
| Eliminación Gaussiana $m$ veces | $m \cdot \frac{2}{3}n^3$ |
| [[Factorizacion LU]] una vez + $m$ sustituciones | $\frac{2}{3}n^3 + m \cdot n^2$ |

> [!ejemplo]
> **Ahorro con LU.**
> 
> Para $n=1000$, $m=100$:
> - Gauss repetido: $100 \cdot \frac{2}{3}10^9 \approx 6.67 \times 10^{10}$ FLOPs.
> - LU + sustituciones: $\frac{2}{3}10^9 + 100 \cdot 10^6 \approx 6.67 \times 10^8 + 10^8 = 7.67 \times 10^8$ FLOPs.
> 
> **Factor de ahorro:** $\approx 87\times$ más rápido.

Esta es la razón por la que la [[Factorizacion LU]] es el método preferido en aplicaciones donde la matriz $A$ es fija pero los lados derechos varían (ej. análisis estructural con múltiples casos de carga).

---

## Complejidad para matrices con estructura especial

La complejidad $O(n^3)$ asume matriz **densa** (sin ceros). Muchas aplicaciones generan matrices con estructura que reduce drásticamente el costo.

| Estructura | Complejidad | Ejemplo de aplicación |
|:---|:---:|:---|
| **Tridiagonal** | $O(n)$ | [[Metodo Diferencias Finitas|Diferencias finitas]] 1D, splines cúbicos |
| **Banda (ancho $b$)** | $O(n b^2)$ | Elementos finitos con numeración adecuada |
| **Hessenberg superior** | $O(n^2)$ | [[Metodo Potencia Directo|Método de la potencia]], valores propios |
| **Triangular** | $O(n^2)$ | Sustitución regresiva/progresiva |
| **Dispersa (sparse)** | $O(n^{1.5})$ a $O(n^2)$ | Depende del [[Relleno Matrices Dispersas|relleno]] |

> [!ejemplo]
> **Sistema tridiagonal.**
> 
> $$A = \begin{pmatrix} 
> b_1 & c_1 & 0 & \cdots & 0 \\
> a_2 & b_2 & c_2 & \cdots & 0 \\
> 0 & a_3 & b_3 & \ddots & \vdots \\
> \vdots & \ddots & \ddots & \ddots & c_{n-1} \\
> 0 & \cdots & 0 & a_n & b_n
> \end{pmatrix}$$
> 
> El [[Algoritmo de Thomas]] (eliminación Gaussiana especializada) resuelve $Ax = d$ en $8n$ FLOPs, es decir, $O(n)$ en lugar de $O(n^3)$.
> 
> ```python
> import numpy as np
> 
> def thomas(a, b, c, d):
>     n = len(d)
>     c_prime = np.zeros(n-1)
>     d_prime = np.zeros(n)
>     
>     # Forward elimination
>     c_prime[0] = c[0] / b[0]
>     d_prime[0] = d[0] / b[0]
>     
>     for i in range(1, n-1):
>         denom = b[i] - a[i] * c_prime[i-1]
>         c_prime[i] = c[i] / denom
>         d_prime[i] = (d[i] - a[i] * d_prime[i-1]) / denom
>     
>     d_prime[n-1] = (d[n-1] - a[n-1] * d_prime[n-2]) / (b[n-1] - a[n-1] * c_prime[n-2])
>     
>     # Back substitution
>     x = np.zeros(n)
>     x[n-1] = d_prime[n-1]
>     for i in range(n-2, -1, -1):
>         x[i] = d_prime[i] - c_prime[i] * x[i+1]
>     
>     return x
> ```
> 
> Este algoritmo es fundamental en la resolución de [[Splines Cubicos Naturales Sujetos|splines cúbicos]] y en la discretización de [[Problema Valor Frontera PVF|problemas de valor en la frontera]] unidimensionales.

---

## Complejidad de métodos iterativos

A diferencia de los métodos directos ($O(n^3)$ garantizado), los [[Metodos Iterativos]] tienen complejidad **por iteración** y un número de iteraciones que depende de las propiedades de la matriz.

| Método | Costo por iteración | Iteraciones típicas |
|:---|:---:|:---|
| [[Jacobi]] | $O(n^2)$ denso, $O(\text{nnz})$ disperso | $O(\kappa(A) \log(1/\varepsilon))$ |
| [[Gauss Seidel]] | $O(n^2)$ denso, $O(\text{nnz})$ disperso | $\approx \frac{1}{2}$ de Jacobi |
| [[Gradiente Conjugado]] | $O(n^2)$ denso, $O(\text{nnz})$ disperso | $\leq n$ (teórico), $O(\sqrt{\kappa(A)})$ práctico |

> [!info]
> **nnz** = *number of non-zeros* (número de elementos no nulos en la matriz dispersa).

Para matrices dispersas grandes ($n > 10^5$, nnz $\ll n^2$), los métodos iterativos pueden ser **órdenes de magnitud más rápidos** que los directos, especialmente si se combinan con [[Precondicionamiento|precondicionadores]].

---

## Conteo de operaciones en la práctica

> [!warning]
> **FLOPs teóricos vs. rendimiento real.**
> El conteo de FLOPs es una **cota inferior ideal**. En la práctica, el rendimiento está limitado por:
> 1. **Jerarquía de memoria:** Accesos a RAM son $\approx 100\times$ más lentos que operaciones en caché.
> 2. **Vectorización:** Uso de instrucciones SIMD (AVX, SSE) puede acelerar $4\times$-$8\times$.
> 3. **Paralelismo:** Multi-hilos y GPUs pueden reducir el tiempo en órdenes de magnitud.
> 4. **Localidad de datos:** Algoritmos por bloques (blocked algorithms) explotan la caché.

> [!ejemplo]
> **Eliminación Gaussiana por bloques.**
> 
> Las bibliotecas modernas (LAPACK, cuBLAS) implementan eliminación Gaussiana operando sobre submatrices (bloques) de tamaño $b \times b$ que caben en caché L2/L3.
> 
> - Costo teórico: $\frac{2}{3}n^3$ FLOPs.
> - Con bloques: Mismo número de FLOPs, pero **menor tiempo de ejecución** debido a mejor uso de caché.
> - Aceleración típica: $3\times$-$10\times$ sobre implementación ingenua.

```python
import numpy as np
import time

n = 2000
A = np.random.randn(n, n)
b = np.random.randn(n)

# Implementación ingenua (no usar en producción)
def gauss_naive(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k+1:] -= factor * A[k, k+1:]
            b[i] -= factor * b[k]
    # Back substitution...
    return b

# Implementación optimizada (NumPy)
t0 = time.time()
x_numpy = np.linalg.solve(A, b)
t_numpy = time.time() - t0

print(f"Tiempo NumPy (LAPACK): {t_numpy:.4f} s")
```

> La diferencia en rendimiento entre una implementación ingenua en Python puro y `np.linalg.solve` (que llama a LAPACK compilado en Fortran/C) puede ser de **varios órdenes de magnitud**.

---

## Implicaciones para la selección de algoritmos

El conteo de operaciones guía la elección del método numérico según el tamaño y estructura del problema.

| Tamaño $n$ | Densidad | Método recomendado |
|:---|:---|:---|
| $n < 1000$ | Densa | Eliminación Gaussiana / LU |
| $1000 < n < 50000$ | Densa | LU con bloques (LAPACK) |
| $n > 50000$ | Densa | Considerar métodos iterativos o reducción de dimensionalidad |
| $n > 10^5$ | Dispersa (nnz $\sim O(n)$) | [[Gradiente Conjugado]] o [[GMRES]] con [[Precondicionamiento]] |
| $n$ cualquiera | Tridiagonal | [[Algoritmo de Thomas]] $O(n)$ |
| $n$ cualquiera | Banda estrecha | Eliminación Gaussiana para banda $O(n b^2)$ |

> [!corolario]
> **Regla de oro.**
> Conocer la complejidad $O(n^3)$ de la eliminación Gaussiana permite anticipar si un problema es computacionalmente viable. Para $n > 10^4$, la resolución densa comienza a ser costosa; para $n > 10^5$, es prohibitiva sin hardware especializado o explotación de estructura dispersa.

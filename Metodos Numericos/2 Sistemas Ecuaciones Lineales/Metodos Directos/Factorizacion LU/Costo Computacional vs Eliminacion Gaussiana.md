---
title: Costo Computacional vs Eliminacion Gaussiana
order: 4
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - complejidad-algoritmica
  - factorizacion-lu
draft: false
aliases:
  - LU vs Gauss
  - Eficiencia de LU
  - Comparativa de costo computacional
---

# Costo Computacional: Factorización LU vs. Eliminación Gaussiana

> [!definicion]
> El **costo computacional** de un algoritmo de álgebra lineal numérica es el número de operaciones de punto flotante (FLOPs) requeridas en función de la dimensión $n$ del problema. La comparación entre la [[Factorizacion LU]] y la [[Eliminacion Gaussiana]] repetida determina cuándo conviene usar una u otra estrategia para resolver sistemas lineales $Ax = b$.

Aunque ambos métodos son algebraicamente equivalentes, su eficiencia difiere drásticamente cuando se resuelven **múltiples sistemas** con la misma matriz $A$.

---

## Recordatorio de costos individuales

Del análisis detallado en [[Conteo Operaciones Complejidad O n3]], tenemos los siguientes costos asintóticos para una matriz densa $n \times n$:

| Operación | FLOPs (término dominante) |
|:---|:---:|
| **Eliminación Gaussiana** (resolver $Ax = b$ desde cero) | $\frac{2}{3}n^3$ |
| **Factorización LU** (calcular $P, L, U$ tal que $PA = LU$) | $\frac{2}{3}n^3$ |
| **Sustitución progresiva** ($Ly = Pb$) | $n^2$ |
| **Sustitución regresiva** ($Ux = y$) | $n^2$ |

> [!info]
> **Observación clave:** La factorización LU tiene el mismo costo asintótico que una eliminación Gaussiana completa. La diferencia radica en que la factorización **separa** la parte costosa ($O(n^3)$) de la parte barata ($O(n^2)$).

---

## Escenario 1: Un solo sistema $Ax = b$

Si solo se necesita resolver **un único sistema lineal**:

| Estrategia | Costo total |
|:---|:---:|
| Eliminación Gaussiana directa | $\frac{2}{3}n^3$ |
| Factorizar LU + resolver | $\frac{2}{3}n^3 + 2n^2$ |

> [!conclusion]
> Para $m = 1$ sistema, la eliminación Gaussiana directa es **ligeramente más eficiente** que LU, ya que evita el paso explícito de formar $L$ y $U$ como estructuras separadas y las dos sustituciones adicionales. La diferencia es marginal ($2n^2$ vs. $\frac{2}{3}n^3$).

En la práctica, muchas bibliotecas (como LAPACK) implementan la rutina `dgesv` que internamente llama a `dgetrf` (LU) + `dgetrs` (sustituciones), incluso para un solo sistema, porque la sobrecarga es mínima y el código es más modular.

---

## Escenario 2: Múltiples sistemas $Ax = b_i$ ($m > 1$)

Cuando se necesita resolver $Ax = b_i$ para $m$ vectores $b_i$ **diferentes**, la ventaja de LU se vuelve decisiva.

| Estrategia | Costo total |
|:---|:---:|
| Eliminación Gaussiana repetida $m$ veces | $m \cdot \frac{2}{3}n^3$ |
| Factorización LU una vez + $m$ pares de sustituciones | $\frac{2}{3}n^3 + m \cdot 2n^2$ |

> [!teorema]
> **Punto de equilibrio.** La factorización LU es más eficiente que la eliminación Gaussiana repetida cuando:
> $$\frac{2}{3}n^3 + 2m n^2 < m \cdot \frac{2}{3}n^3$$
> 
> Simplificando para $n$ grande:
> $$m > \frac{\frac{2}{3}n^3}{\frac{2}{3}n^3 - 2n^2} \approx 1 + \frac{3}{n}$$
> 
> **Para todo $n \geq 3$ y $m \geq 2$, LU es más eficiente.**

> [!ejemplo]
> **Ahorro concreto para $n = 1000$, $m = 10$.**
> 
> - **Gauss repetido:** $10 \cdot \frac{2}{3} \cdot 10^9 \approx 6.67 \times 10^9$ FLOPs.
> - **LU + sustituciones:** $\frac{2}{3} \cdot 10^9 + 10 \cdot 2 \cdot 10^6 \approx 6.67 \times 10^8 + 2 \times 10^7 = 6.87 \times 10^8$ FLOPs.
> 
> **Factor de aceleración:** $\frac{6.67 \times 10^9}{6.87 \times 10^8} \approx 9.7\times$ más rápido.
> 
> Para $m = 100$:
> - Gauss repetido: $\approx 6.67 \times 10^{10}$ FLOPs.
> - LU + sustituciones: $\approx 6.67 \times 10^8 + 2 \times 10^8 = 8.67 \times 10^8$ FLOPs.
> 
> **Factor de aceleración:** $\approx 77\times$ más rápido.

---

## Escenario 3: Matrices simétricas definidas positivas

Si $A$ es simétrica definida positiva, se puede usar la [[Factorizacion Cholesky Matrices Definidas Positivas|factorización de Cholesky]] ($A = LL^T$).

| Método | Costo de factorización | Costo por sistema |
|:---|:---:|:---:|
| Gauss repetido $m$ veces | $m \cdot \frac{2}{3}n^3$ | — |
| LU + $m$ sustituciones | $\frac{2}{3}n^3$ | $2n^2$ |
| **Cholesky + $m$ sustituciones** | $\frac{1}{3}n^3$ | $2n^2$ |

> [!proposicion]
> **Ventaja de Cholesky.** Para matrices SDP, Cholesky no solo es más estable, sino que reduce el costo de factorización a la **mitad** respecto a LU.
> 
> **Ahorro adicional:** Factor $\approx 2\times$ sobre LU en la fase de factorización.

> [!ejemplo]
> **$n = 1000$, $m = 100$, matriz SDP.**
> 
> - LU + sustituciones: $\approx 8.67 \times 10^8$ FLOPs.
> - Cholesky + sustituciones: $\frac{1}{3} \cdot 10^9 + 100 \cdot 2 \cdot 10^6 \approx 3.33 \times 10^8 + 2 \times 10^8 = 5.33 \times 10^8$ FLOPs.
> 
> Cholesky es $\approx 1.6\times$ más rápido que LU, y $\approx 125\times$ más rápido que Gauss repetido.

---

## Escenario 4: Múltiples lados derechos simultáneos

Si se conoce de antemano el conjunto de $m$ vectores $b_i$, se pueden organizar como columnas de una matriz $B \in \mathbb{R}^{n \times m}$ y resolver $AX = B$.

| Estrategia | Costo total |
|:---|:---:|
| Eliminación Gaussiana por columnas | $\frac{2}{3}n^3 + m n^2$ |
| Factorización LU + sustituciones por columnas | $\frac{2}{3}n^3 + 2m n^2$ |

> [!info]
> La eliminación Gaussiana aplicada a la matriz aumentada $[A | B]$ es ligeramente más eficiente que LU + sustituciones separadas, porque la eliminación se hace una sola vez para todas las columnas de $B$ simultáneamente, ahorrando un factor constante en las sustituciones.

En la práctica, LAPACK ofrece la rutina `dgesv` que acepta múltiples lados derechos y aplica esta optimización.

---

## Costo en memoria

Además del tiempo de cómputo, el almacenamiento es un factor crítico para problemas grandes.

| Método | Almacenamiento requerido |
|:---|:---:|
| Eliminación Gaussiana in-place | $n^2$ (sobrescribe $A$) |
| Factorización LU in-place | $n^2$ (sobrescribe $A$) |
| Factorización Cholesky in-place | $n(n+1)/2$ (solo mitad triangular) |

> [!warning]
> **Factorización explícita vs. in-place.** Si se requiere conservar la matriz original $A$, se debe hacer una copia ($+n^2$ memoria). Las implementaciones in-place modifican $A$, ahorrando memoria pero destruyendo la matriz original.

---

## Resumen de decisiones

| Situación | Método recomendado | Costo dominante |
|:---|:---|:---|
| Un solo sistema $Ax = b$ | Eliminación Gaussiana directa | $\frac{2}{3}n^3$ |
| Múltiples sistemas ($m \geq 2$) con la misma $A$ | Factorización LU + sustituciones | $\frac{2}{3}n^3 + 2m n^2$ |
| $A$ simétrica definida positiva, múltiples sistemas | [[Factorizacion Cholesky Matrices Definidas Positivas\|Cholesky]] + sustituciones | $\frac{1}{3}n^3 + 2m n^2$ |
| Múltiples lados derechos conocidos simultáneamente | `dgesv` (LAPACK) con matriz $B$ | $\frac{2}{3}n^3 + m n^2$ |
| Matriz tridiagonal | [[Algoritmo de Thomas]] | $O(n)$ por sistema |

---

## Visualización gráfica

Para $n = 1000$ fijo, variando $m$:

| $m$ | Gauss repetido (FLOPs) | LU + sustituciones (FLOPs) | Aceleración |
|:---:|:---:|:---:|:---:|
| 1 | $6.67 \times 10^8$ | $6.69 \times 10^8$ | $1.00\times$ |
| 2 | $1.33 \times 10^9$ | $6.71 \times 10^8$ | $1.99\times$ |
| 5 | $3.33 \times 10^9$ | $6.77 \times 10^8$ | $4.92\times$ |
| 10 | $6.67 \times 10^9$ | $6.87 \times 10^8$ | $9.71\times$ |
| 50 | $3.33 \times 10^{10}$ | $7.67 \times 10^8$ | $43.5\times$ |
| 100 | $6.67 \times 10^{10}$ | $8.67 \times 10^8$ | $76.9\times$ |

La ventaja de LU crece linealmente con $m$.

---

## Implicaciones prácticas

> [!info]
> **Aplicaciones donde LU es indispensable.**
> 
> 1. **Análisis estructural por elementos finitos:** La matriz de rigidez $K$ es fija; se analizan múltiples casos de carga (viento, sismo, peso propio).
> 2. **Circuitos eléctricos:** La matriz de admitancias es constante; se varían las fuentes de excitación.
> 3. **Simulaciones Monte Carlo:** Se resuelve $Ax = b(\omega)$ para miles de realizaciones aleatorias de $b$.
> 4. **Refinamiento iterativo:** Mejora de una solución inicial resolviendo $A \Delta x = r$ con la misma LU.
> 5. **Cálculo de la matriz inversa:** Aunque rara vez es necesario, $A^{-1}$ se obtiene resolviendo $AX = I$ (LU una vez + $n$ sustituciones).

> [!warning]
> **Cuándo NO usar LU.**
> - Sistemas extremadamente grandes y dispersos: el relleno durante la factorización puede hacerla inviable en memoria.
> - Matrices mal condicionadas donde la precisión de LU con pivoteo parcial es insuficiente; considerar [[Factorizacion QR]] o SVD.
> - Problemas donde $A$ cambia en cada iteración (ej. métodos de Newton con Jacobiano actualizado).

---

## Relación con otros costos

El costo de la factorización LU domina sobre otras operaciones matriciales comunes:

| Operación | Costo | Comparación con LU |
|:---|:---:|:---:|
| Producto matriz-vector ($Ax$) | $2n^2$ | $O(n)$ veces más barato |
| Producto matriz-matriz ($AB$) | $2n^3$ | $\approx 3\times$ LU |
| Cálculo de determinante vía LU | $\frac{2}{3}n^3 + O(n^2)$ | Idéntico a factorizar |
| Cálculo de inversa vía LU | $\frac{8}{3}n^3$ | $4\times$ más caro que LU |

> [!corolario]
> **Regla de oro.** Nunca calcular $A^{-1}$ explícitamente para resolver $Ax = b$. Factorizar LU y resolver por sustituciones es $\approx 4\times$ más rápido y numéricamente más estable.

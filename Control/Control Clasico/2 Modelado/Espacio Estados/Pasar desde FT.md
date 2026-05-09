---
title: De Función Transferencia a Espacio de Estados
tags:
  - control-clasico
  - teoria
  - espacio-estados
draft: false
aliases:
  - ft a espacio
  - transferencia a estados
  - realización
  - realizaciones canónicas
---

# De Función Transferencia a Espacio de Estados

# Definición

> [!definicion] Realización
> Dada una función transferencia $G(s)$, una **realización** es un conjunto de matrices $\{\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}\}$ tales que:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$
> 
> La realización **no es única**. Existen infinitas representaciones equivalentes.

# Condición de realizabilidad

> [!teorema] Condición necesaria y suficiente
> $G(s)$ es realizable en espacio de estados si y solo si es **propia o estrictamente propia**:
> $$\lim_{s \to \infty} G(s) < \infty$$
> 
> - **Sistemas propios**: grado numerador $\le$ grado denominador
> - **Sistemas estrictamente propios**: grado numerador $<$ grado denominador ($\mathbf{D} = \mathbf{0}$)
> - **Sistemas impropios**: grado numerador $>$ grado denominador → no realizables físicamente

# Realización canónica controlable (forma de controlabilidad)

> [!definicion] Forma canónica controlable
> Para $G(s) = \frac{b_{n-1}s^{n-1} + \dots + b_1 s + b_0}{s^n + a_{n-1}s^{n-1} + \dots + a_1 s + a_0}$ (estrictamente propia):
> 
> $$\mathbf{A} = \begin{bmatrix}
> 0 & 1 & 0 & \dots & 0 \\
> 0 & 0 & 1 & \dots & 0 \\
> \vdots & \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & 0 & \dots & 1 \\
> -a_0 & -a_1 & -a_2 & \dots & -a_{n-1}
> \end{bmatrix}, \quad
> \mathbf{B} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$
> 
> $$\mathbf{C} = \begin{bmatrix} b_0 & b_1 & \dots & b_{n-1} \end{bmatrix}, \quad
> \mathbf{D} = 0$$

> [!demostracion] Verificación
> La función transferencia de esta realización es:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} = \frac{b_{n-1}s^{n-1} + \dots + b_0}{s^n + a_{n-1}s^{n-1} + \dots + a_0}$$
> 
> Se verifica por construcción del polinomio característico en la última fila de $\mathbf{A}$.

> [!ejemplo] Sistema de segundo orden
> $$G(s) = \frac{2s + 3}{s^2 + 4s + 5}$$
> 
> Identificar: $a_1 = 4$, $a_0 = 5$, $b_1 = 2$, $b_0 = 3$
> 
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -5 & -4 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad
>    \mathbf{C} = \begin{bmatrix} 3 & 2 \end{bmatrix}, \quad
>    \mathbf{D} = 0$$

# Realización canónica observable (forma de observabilidad)

> [!definicion] Forma canónica observable
> Para la misma $G(s)$:
> 
> $$\mathbf{A} = \begin{bmatrix}
> 0 & 0 & \dots & 0 & -a_0 \\
> 1 & 0 & \dots & 0 & -a_1 \\
> 0 & 1 & \dots & 0 & -a_2 \\
> \vdots & \vdots & \ddots & \vdots & \vdots \\
> 0 & 0 & \dots & 1 & -a_{n-1}
> \end{bmatrix}, \quad
> \mathbf{B} = \begin{bmatrix} b_0 \\ b_1 \\ \vdots \\ b_{n-1} \end{bmatrix}$$
> 
> $$\mathbf{C} = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix}, \quad
> \mathbf{D} = 0$$

> [!ejemplo] Mismo sistema de segundo orden
> $$G(s) = \frac{2s + 3}{s^2 + 4s + 5}$$
> 
> $$\mathbf{A} = \begin{bmatrix} 0 & -5 \\ 1 & -4 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}, \quad
>    \mathbf{C} = \begin{bmatrix} 0 & 1 \end{bmatrix}, \quad
>    \mathbf{D} = 0$$

# Realización diagonal (forma de Jordan)

> [!definicion] Forma diagonal (polos simples)
> Si los polos $p_1, p_2, \dots, p_n$ son distintos:
> 
> $$\mathbf{A} = \begin{bmatrix}
> p_1 & 0 & \dots & 0 \\
> 0 & p_2 & \dots & 0 \\
> \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \dots & p_n
> \end{bmatrix}, \quad
> \mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{bmatrix}$$
> 
> $$\mathbf{C} = \begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix}, \quad
> \mathbf{D} = \text{(ganancia directa si existe)}$$
> 
> donde $c_i = \left. (s - p_i) G(s) \right|_{s = p_i}$ (residuos).

> [!demostracion]
> Expandiendo $G(s)$ en fracciones parciales:
> $$G(s) = \sum_{i=1}^n \frac{c_i}{s - p_i} + \mathbf{D}$$
> 
> Cada término $\frac{c_i}{s - p_i}$ se realiza como:
> $$\dot{x}_i = p_i x_i + u, \quad y_i = c_i x_i$$
> 
> Sumando todas las salidas se obtiene la realización diagonal.

> [!ejemplo] Polos reales distintos
> $$G(s) = \frac{6}{(s+1)(s+2)(s+3)}$$
> 
> Residuos:
> $$c_1 = \left. \frac{6}{(s+2)(s+3)} \right|_{s=-1} = \frac{6}{1 \cdot 2} = 3$$
> $$c_2 = \left. \frac{6}{(s+1)(s+3)} \right|_{s=-2} = \frac{6}{(-1) \cdot 1} = -6$$
> $$c_3 = \left. \frac{6}{(s+1)(s+2)} \right|_{s=-3} = \frac{6}{(-2)(-1)} = 3$$
> 
> Realización diagonal:
> $$\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad
>    \mathbf{C} = \begin{bmatrix} 3 & -6 & 3 \end{bmatrix}, \quad
>    \mathbf{D} = 0$$

# Realización de Jordan (polos repetidos)

> [!definicion] Bloque de Jordan para polo $p$ de multiplicidad $r$
> Para $G(s) = \frac{c_r}{(s-p)^r} + \frac{c_{r-1}}{(s-p)^{r-1}} + \dots + \frac{c_1}{s-p}$:
> 
> $$\mathbf{A} = \begin{bmatrix}
> p & 1 & 0 & \dots & 0 \\
> 0 & p & 1 & \dots & 0 \\
> \vdots & \vdots & \ddots & \ddots & \vdots \\
> 0 & 0 & \dots & p & 1 \\
> 0 & 0 & \dots & 0 & p
> \end{bmatrix}, \quad
> \mathbf{B} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$
> 
> $$\mathbf{C} = \begin{bmatrix} c_1 & c_2 & \dots & c_r \end{bmatrix}$$

> [!ejemplo] Polo doble
> $$G(s) = \frac{1}{(s+1)^2} + \frac{2}{s+1} = \frac{s+3}{(s+1)^2}$$
> 
> Realización de Jordan:
> $$\mathbf{A} = \begin{bmatrix} -1 & 1 \\ 0 & -1 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad
>    \mathbf{C} = \begin{bmatrix} 2 & 1 \end{bmatrix}, \quad
>    \mathbf{D} = 0$$

# Procedimiento general para sistemas con $\mathbf{D} \neq 0$

> [!info] Caso propio (grado numerador = grado denominador)
> $$G(s) = \frac{b_n s^n + b_{n-1}s^{n-1} + \dots + b_0}{s^n + a_{n-1}s^{n-1} + \dots + a_0}$$
> 
> Dividir para obtener:
> $$G(s) = \mathbf{D} + \frac{\tilde{b}_{n-1}s^{n-1} + \dots + \tilde{b}_0}{s^n + a_{n-1}s^{n-1} + \dots + a_0}$$
> 
> donde $\mathbf{D} = b_n$. Luego aplicar forma canónica a la parte estrictamente propia.

> [!ejemplo] Sistema propio
> $$G(s) = \frac{2s^2 + 3s + 1}{s^2 + 4s + 5}$$
> 
> División:
> $$\frac{2s^2 + 3s + 1}{s^2 + 4s + 5} = 2 + \frac{-5s - 9}{s^2 + 4s + 5}$$
> 
> $\mathbf{D} = 2$, parte estrictamente propia: $\frac{-5s - 9}{s^2 + 4s + 5}$
> 
> Realización controlable:
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -5 & -4 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad
>    \mathbf{C} = \begin{bmatrix} -9 & -5 \end{bmatrix}, \quad
>    \mathbf{D} = 2$$

# Transformaciones entre realizaciones

> [!teorema] Equivalencia por cambio de base
> Si $\{\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}\}$ es una realización, entonces $\{\mathbf{T}\mathbf{A}\mathbf{T}^{-1}, \mathbf{T}\mathbf{B}, \mathbf{C}\mathbf{T}^{-1}, \mathbf{D}\}$ también lo es, para cualquier $\mathbf{T}$ invertible.
> 
> Ver [[Forma General]].

# Resumen de realizaciones comunes

> [!info] Tabla comparativa
> | Realización | Ventaja | Desventaja |
> |-------------|---------|-------------|
> | Controlable | Útil para diseño por ubicación de polos | No observable en general |
> | Observable | Útil para diseño de observadores | No controlable en general |
> | Diagonal | Análisis modal directo | Requiere polos distintos |
> | Jordan | Maneja polos repetidos | Más compleja |

# Limitaciones

> [!warning]
> 1. Las realizaciones canónicas pueden ser **numéricamente mal condicionadas** para sistemas de orden alto
> 2. Para sistemas MIMO, las formas canónicas son más complejas
> 3. La realización diagonal requiere polos distintos (no repetidos)
> 4. Las cancelaciones polo-cero indican que la realización no es mínima
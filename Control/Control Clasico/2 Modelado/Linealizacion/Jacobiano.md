---
title: Jacobiano
tags:
  - control-clasico
  - teoria
  - linealizacion
  - matematicas
draft: false
aliases:
  - matriz jacobiana
  - jacobiano
  - derivada parcial vectorial
---

# Jacobiano

# Definición para sistemas de control

> [!definicion] Matriz Jacobiana (para un sistema de estados)
> Dado un sistema con $n$ ecuaciones de estado y $n$ variables de estado:
> 
> $$\dot{x}_1 = f_1(x_1, x_2, \dots, x_n, u_1, \dots, u_m)$$
> $$\dot{x}_2 = f_2(x_1, x_2, \dots, x_n, u_1, \dots, u_m)$$
> $$\vdots$$
> $$\dot{x}_n = f_n(x_1, x_2, \dots, x_n, u_1, \dots, u_m)$$
> 
> La matriz Jacobiana respecto a los estados es:
> 
> $$\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
> \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\[4pt]
> \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\[4pt]
> \vdots & \vdots & \ddots & \vdots \\[4pt]
> \frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \cdots & \frac{\partial f_n}{\partial x_n}
> \end{bmatrix}$$

> [!definicion] Jacobiana respecto a entradas
> $$\frac{\partial \mathbf{f}}{\partial \mathbf{u}} = \begin{bmatrix}
> \frac{\partial f_1}{\partial u_1} & \cdots & \frac{\partial f_1}{\partial u_m} \\
> \vdots & \ddots & \vdots \\
> \frac{\partial f_n}{\partial u_1} & \cdots & \frac{\partial f_n}{\partial u_m}
> \end{bmatrix}$$

# Interpretación

> [!info] Significado físico
> La entrada $(i,j)$ de $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ es la **sensibilidad** de la $i$-ésima ecuación de estado respecto a la $j$-ésima variable de estado.
> 
> Es decir: cuánto cambia $\dot{x}_i$ cuando $x_j$ varía ligeramente, manteniendo todas las demás variables constantes.

# Cálculo paso a paso

> [!info] Reglas básicas
> 1. **Derivada de una constante:** $\frac{\partial c}{\partial x} = 0$
> 2. **Derivada de $x_i$ respecto a $x_j$:** $\frac{\partial x_i}{\partial x_j} = \begin{cases} 1 & \text{si } i=j \\ 0 & \text{si } i \neq j \end{cases}$
> 3. **Linealidad:** $\frac{\partial}{\partial x}(a f + b g) = a \frac{\partial f}{\partial x} + b \frac{\partial g}{\partial x}$
> 4. **Regla del producto:** $\frac{\partial}{\partial x}(f \cdot g) = \frac{\partial f}{\partial x} \cdot g + f \cdot \frac{\partial g}{\partial x}$
> 5. **Regla de la cadena:** $\frac{\partial}{\partial x} f(g(x)) = \frac{\partial f}{\partial g} \cdot \frac{\partial g}{\partial x}$

# Ejemplo 1: Sistema de segundo orden (lineal)

> [!ejemplo] Sistema masa-resorte-amortiguador lineal
> $$f_1 = x_2$$
> $$f_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 + \frac{1}{m}u$$
> 
> **Derivadas parciales:**
> 
> $\frac{\partial f_1}{\partial x_1} = 0$, $\frac{\partial f_1}{\partial x_2} = 1$
> 
> $\frac{\partial f_2}{\partial x_1} = -\frac{k}{m}$, $\frac{\partial f_2}{\partial x_2} = -\frac{b}{m}$
> 
> $\frac{\partial f_2}{\partial u} = \frac{1}{m}$
> 
> **Jacobianas:**
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix}$$

# Ejemplo 2: Sistema no lineal (péndulo)

> [!ejemplo] Péndulo
> $$f_1 = x_2$$
> $$f_2 = -\frac{g}{l}\sin x_1 - \frac{b}{ml^2}x_2 + \frac{1}{ml^2}u$$
> 
> **Derivadas parciales:**
> 
> $\frac{\partial f_1}{\partial x_1} = 0$, $\frac{\partial f_1}{\partial x_2} = 1$
> 
> $\frac{\partial f_2}{\partial x_1} = -\frac{g}{l}\cos x_1$
> 
> $\frac{\partial f_2}{\partial x_2} = -\frac{b}{ml^2}$
> 
> $\frac{\partial f_2}{\partial u} = \frac{1}{ml^2}$
> 
> **Jacobianas (evaluadas en $x_{10}=0$, $x_{20}=0$):**
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{l} & -\frac{b}{ml^2} \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{ml^2} \end{bmatrix}$$

# Ejemplo 3: Sistema con producto de estados

> [!ejemplo] Términos de acoplamiento no lineal
> $$\dot{x}_1 = x_1 x_2 + u$$
> $$\dot{x}_2 = -x_1^2 + 3x_2$$
> 
> **Derivadas parciales:**
> 
> $\frac{\partial f_1}{\partial x_1} = x_2$, $\frac{\partial f_1}{\partial x_2} = x_1$, $\frac{\partial f_1}{\partial u} = 1$
> 
> $\frac{\partial f_2}{\partial x_1} = -2x_1$, $\frac{\partial f_2}{\partial x_2} = 3$, $\frac{\partial f_2}{\partial u} = 0$
> 
> **Jacobianas en $x_1=0, x_2=0, u=0$:**
> $$\mathbf{A} = \begin{bmatrix} 0 & 0 \\ 0 & 3 \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

# Caso SISO vs MIMO

> [!info] Comparación
> | | SISO (una entrada, una salida) | MIMO (múltiples entradas, salidas) |
> |---|-------------------------------|-------------------------------------|
> | $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ | $n \times n$ | $n \times n$ |
> | $\frac{\partial \mathbf{f}}{\partial \mathbf{u}}$ | $n \times 1$ | $n \times m$ |
> | $\frac{\partial \mathbf{h}}{\partial \mathbf{x}}$ | $1 \times n$ | $p \times n$ |
> | $\frac{\partial \mathbf{h}}{\partial \mathbf{u}}$ | $1 \times 1$ | $p \times m$ |

# Cálculo rápido para sistemas LTI

> [!info] Sistemas lineales
> Si el sistema ya es lineal:
> $$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$
> 
> Entonces:
> $$\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \mathbf{A}, \quad \frac{\partial \mathbf{f}}{\partial \mathbf{u}} = \mathbf{B}$$
> 
> (Las derivadas son las matrices originales, no dependen del punto de operación)

# Relación con la linealización

> [!teorema] Linealización = Jacobiana en el punto de equilibrio
> Para un sistema no lineal $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$ con punto de equilibrio $(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\mathbf{A} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
>    \mathbf{B} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}$$
> 
> Ver [[Linealizacion/index | linealización]].

# Propiedades del Jacobiano

> [!info] Propiedades útiles
> 1. **Determinante:** $\det\left(\frac{\partial \mathbf{f}}{\partial \mathbf{x}}\right)$ indica cambio de volumen local (criterio de invertibilidad)
> 2. **Autovalores:** Los autovalores de $\mathbf{A}$ determinan la estabilidad local (para sistemas autónomos)
> 3. **Rango:** Si $\text{rango}\left(\frac{\partial \mathbf{f}}{\partial \mathbf{x}}\right) = n$, el sistema es localmente invertible

# Ejemplo con salida

> [!ejemplo] Ecuación de salida
> $$y = h(x_1, x_2) = x_1^2 + x_2$$
> 
> **Jacobiana de salida:**
> $$\frac{\partial h}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial h}{\partial x_1} & \frac{\partial h}{\partial x_2} \end{bmatrix} = \begin{bmatrix} 2x_1 & 1 \end{bmatrix}$$
> 
> Evaluada en $x_1=0$, $x_2=0$:
> $$\mathbf{C} = \begin{bmatrix} 0 & 1 \end{bmatrix}$$

# Limitaciones

> [!warning]
> 1. **No linealidades fuertes:** Si las derivadas parciales no existen (función no diferenciable), el Jacobiano no está definido
> 2. **Puntos de bifurcación:** En puntos donde $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ tiene autovalores nulos, la aproximación lineal puede ser insuficiente
> 3. **Dependencia del punto de operación:** El Jacobiano cambia si el punto de operación cambia
> 4. **Sistemas a tiempo discreto:** Se usa el mismo concepto pero con ecuaciones en diferencias
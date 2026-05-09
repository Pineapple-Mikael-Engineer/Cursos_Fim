---
title: Forma General de Espacio de Estados
tags:
  - control-clasico
  - teoria
  - espacio-estados
draft: false
aliases:
  - forma general
  - representación general
---

# Forma General de Espacio de Estados

# Definición

> [!definicion] Sistema continuo LTI
> Un sistema lineal invariante en el tiempo (LTI) de orden $n$, con $m$ entradas y $p$ salidas, se representa como:
> 
> $$\dot{\mathbf{x}}(t) = \mathbf{A} \mathbf{x}(t) + \mathbf{B} \mathbf{u}(t)$$
> 
> $$\mathbf{y}(t) = \mathbf{C} \mathbf{x}(t) + \mathbf{D} \mathbf{u}(t)$$
> 
> con condiciones iniciales $\mathbf{x}(0) = \mathbf{x}_0$.

> [!definicion] Sistema discreto
> Para sistemas en tiempo discreto:
> 
> $$\mathbf{x}[k+1] = \mathbf{A}_d \mathbf{x}[k] + \mathbf{B}_d \mathbf{u}[k]$$
> 
> $$\mathbf{y}[k] = \mathbf{C}_d \mathbf{x}[k] + \mathbf{D}_d \mathbf{u}[k]$$

# Dimensiones

> [!info] Tamaño de las matrices
> | Matriz | Dimensión | Significado |
> |--------|-----------|--------------|
> | $\mathbf{A}$ | $n \times n$ | Dinámica del sistema |
> | $\mathbf{B}$ | $n \times m$ | Influencia de entradas |
> | $\mathbf{C}$ | $p \times n$ | Medición de estados |
> | $\mathbf{D}$ | $p \times m$ | Alimentación directa |
> | $\mathbf{x}(t)$ | $n \times 1$ | Vector de estados |
> | $\mathbf{u}(t)$ | $m \times 1$ | Vector de entradas |
> | $\mathbf{y}(t)$ | $p \times 1$ | Vector de salidas |

# Clasificación según $\mathbf{D}$

> [!info] Casos típicos
> - **$\mathbf{D} = \mathbf{0}$**: sistema estrictamente propio (más común)
> - **$\mathbf{D} \neq \mathbf{0}$**: sistema bipropio (tiene alimentación directa)
> - **$\mathbf{D}$ con términos infinitos**: sistema impropio (no realizable físicamente)

# Transformación de variables de estado

> [!teorema] Cambio de base
> Sea $\mathbf{z}(t) = \mathbf{T} \mathbf{x}(t)$ con $\mathbf{T}$ invertible. Entonces:
> 
> $$\dot{\mathbf{z}}(t) = \tilde{\mathbf{A}} \mathbf{z}(t) + \tilde{\mathbf{B}} \mathbf{u}(t)$$
> 
> $$\mathbf{y}(t) = \tilde{\mathbf{C}} \mathbf{z}(t) + \tilde{\mathbf{D}} \mathbf{u}(t)$$
> 
> donde:
> $$\tilde{\mathbf{A}} = \mathbf{T} \mathbf{A} \mathbf{T}^{-1}, \quad 
>    \tilde{\mathbf{B}} = \mathbf{T} \mathbf{B}, \quad 
>    \tilde{\mathbf{C}} = \mathbf{C} \mathbf{T}^{-1}, \quad 
>    \tilde{\mathbf{D}} = \mathbf{D}$$

> [!demostracion]
> Derivando $\mathbf{z}(t) = \mathbf{T} \mathbf{x}(t)$:
> 
> $$\dot{\mathbf{z}} = \mathbf{T} \dot{\mathbf{x}} = \mathbf{T}(\mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u}) = \mathbf{T}\mathbf{A} \mathbf{T}^{-1} \mathbf{z} + \mathbf{T}\mathbf{B} \mathbf{u}$$
> 
> La salida:
> 
> $$\mathbf{y} = \mathbf{C} \mathbf{x} + \mathbf{D} \mathbf{u} = \mathbf{C} \mathbf{T}^{-1} \mathbf{z} + \mathbf{D} \mathbf{u}$$

> [!ejemplo] Cambio de orden de estados
> Sistema de segundo orden:
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$
> 
> Intercambiar estados: $\mathbf{T} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, $\mathbf{T}^{-1} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$
> 
> $$\tilde{\mathbf{A}} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} -3 & -2 \\ 1 & 0 \end{bmatrix}$$

# Solución de la ecuación de estado

> [!teorema] Solución general (tiempo continuo)
> $$\mathbf{x}(t) = e^{\mathbf{A}t} \mathbf{x}(0) + \int_0^t e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) d\tau$$
> 
> donde $e^{\mathbf{A}t}$ es la **matriz exponencial**.

> [!definicion] Matriz exponencial
> $$e^{\mathbf{A}t} = \mathbf{I} + \mathbf{A}t + \frac{\mathbf{A}^2 t^2}{2!} + \frac{\mathbf{A}^3 t^3}{3!} + \dots = \sum_{k=0}^\infty \frac{\mathbf{A}^k t^k}{k!}$$

> [!demostracion] Verificación por derivación
> Derivando la solución propuesta:
> 
> $$\frac{d}{dt} e^{\mathbf{A}t} \mathbf{x}(0) = \mathbf{A} e^{\mathbf{A}t} \mathbf{x}(0)$$
> 
> $$\frac{d}{dt} \int_0^t e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) d\tau = \mathbf{B} \mathbf{u}(t) + \mathbf{A} \int_0^t e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) d\tau$$
> 
> Sumando:
> 
> $$\dot{\mathbf{x}}(t) = \mathbf{A} \left[ e^{\mathbf{A}t} \mathbf{x}(0) + \int_0^t e^{\mathbf{A}(t-\tau)} \mathbf{B} \mathbf{u}(\tau) d\tau \right] + \mathbf{B} \mathbf{u}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)$$
> 
> Evaluando en $t=0$: $\mathbf{x}(0) = \mathbf{x}(0)$.

# Ejemplo: sistema de primer orden

> [!ejemplo] Circuito RC
> Ecuación: $RC \dot{v}_c + v_c = v_i$
> 
> **Paso 1:** Elegir estado $x = v_c$, entrada $u = v_i$, salida $y = v_c$.
> 
> $$\dot{x} = -\frac{1}{RC} x + \frac{1}{RC} u$$
> 
> **Paso 2:** Matrices:
> $$A = -\frac{1}{RC}, \quad B = \frac{1}{RC}, \quad C = 1, \quad D = 0$$
> 
> **Paso 3:** Solución analítica:
> $$x(t) = e^{-t/RC} x(0) + \frac{1}{RC} \int_0^t e^{-(t-\tau)/RC} u(\tau) d\tau$$

# Ejemplo: sistema de segundo orden

> [!ejemplo] Masa-resorte-amortiguador (SISO)
> $$m\ddot{y} + b\dot{y} + ky = u$$
> 
> **Paso 1:** Estados: $x_1 = y$, $x_2 = \dot{y}$
> 
> **Paso 2:** Ecuaciones:
> $$\dot{x}_1 = x_2$$
> $$\dot{x}_2 = -\frac{k}{m} x_1 - \frac{b}{m} x_2 + \frac{1}{m} u$$
> 
> **Paso 3:** Forma matricial:
> $$\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix} \mathbf{x} + \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix} u$$
> $$y = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}$$
> 
> **Paso 4:** Matriz exponencial (por Laplace):
> $$e^{\mathbf{A}t} = \mathcal{L}^{-1}\{(s\mathbf{I} - \mathbf{A})^{-1}\}$$

# Propiedades de la matriz exponencial

> [!info] Propiedades clave
> 1. $e^{\mathbf{A} \cdot 0} = \mathbf{I}$
> 2. $\frac{d}{dt} e^{\mathbf{A}t} = \mathbf{A} e^{\mathbf{A}t} = e^{\mathbf{A}t} \mathbf{A}$
> 3. $e^{\mathbf{A}(t_1 + t_2)} = e^{\mathbf{A}t_1} e^{\mathbf{A}t_2}$
> 4. $(e^{\mathbf{A}t})^{-1} = e^{-\mathbf{A}t}$
> 5. Si $\mathbf{A}$ es diagonal: $e^{\mathbf{A}t} = \text{diag}(e^{\lambda_1 t}, e^{\lambda_2 t}, \dots, e^{\lambda_n t})$

# Equivalencia con función transferencia

> [!teorema] Relación
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$
> 
> Ver [[Pasar a FT]].

# Sistemas no lineales

> [!definicion] Forma general no lineal
> $$\dot{\mathbf{x}}(t) = \mathbf{f}(\mathbf{x}(t), \mathbf{u}(t), t)$$
> $$\mathbf{y}(t) = \mathbf{h}(\mathbf{x}(t), \mathbf{u}(t), t)$$
> 
> Para análisis local, se [[Linealizacion | linealiza]] alrededor de un punto de operación.

# Limitaciones

> [!warning]
> 1. La solución con matriz exponencial es difícil de calcular analíticamente para $n > 3$
> 2. En la práctica se usan métodos numéricos (simulación)
> 3. La elección de variables de estado no es única
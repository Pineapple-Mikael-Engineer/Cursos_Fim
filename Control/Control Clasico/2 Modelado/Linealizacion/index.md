---
title: Linealización
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - linealizacion
  - aproximación lineal
---

# Linealización

# Definición

> [!definicion] Linealización
> Proceso de aproximar un sistema no lineal por un sistema lineal alrededor de un **punto de operación**.
> 
> Dado $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$, con punto de operación $(\mathbf{x}_0, \mathbf{u}_0)$ tal que $\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$:
> 
> $$\dot{\mathbf{x}} \approx \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{0} (\mathbf{x} - \mathbf{x}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_{0} (\mathbf{u} - \mathbf{u}_0)$$

# Jacobiano (definición operativa)

> [!definicion] Matriz Jacobiana (para linealización)
> Dado un sistema con $n$ estados y $m$ entradas:
> 
> $$\mathbf{f}(\mathbf{x}, \mathbf{u}) = \begin{bmatrix} f_1(x_1, \dots, x_n, u_1, \dots, u_m) \\ \vdots \\ f_n(x_1, \dots, x_n, u_1, \dots, u_m) \end{bmatrix}$$
> 
> La matriz Jacobiana respecto a los estados es:
> 
> $$\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
> \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
> \vdots & \ddots & \vdots \\
> \frac{\partial f_n}{\partial x_1} & \cdots & \frac{\partial f_n}{\partial x_n}
> \end{bmatrix}$$
> 
> Cada entrada $(i,j)$ es la **derivada parcial** de la $i$-ésima ecuación de estado respecto a la $j$-ésima variable de estado.
> 
> Similarmente para $\frac{\partial \mathbf{f}}{\partial \mathbf{u}}$ (matriz $n \times m$).
> 
> Ver [[Jacobiano]] para teoría completa (derivadas parciales, propiedades, aplicaciones en otras áreas).

# Por qué linealizar

> [!info] Razones
> 1. La mayoría de sistemas reales son **no lineales**
> 2. El análisis y diseño de sistemas lineales es **mucho más simple**
> 3. Cerca del punto de operación, la aproximación es **válida** (pequeñas desviaciones)
> 4. Permite usar herramientas como: función transferencia, lugar de raíces, Bode, Nyquist

# Procedimiento general

> [!info] Pasos
> 1. Encontrar un punto de equilibrio $(\mathbf{x}_0, \mathbf{u}_0)$ donde $\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$
> 2. Definir **variables de desviación**: $\delta \mathbf{x} = \mathbf{x} - \mathbf{x}_0$, $\delta \mathbf{u} = \mathbf{u} - \mathbf{u}_0$
> 3. Calcular las matrices Jacobianas:
>    $$\mathbf{A} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
>       \mathbf{B} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}$$
> 4. El sistema linealizado es:
>    $$\delta \dot{\mathbf{x}} = \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u}$$
> 5. Para la salida $\mathbf{y} = \mathbf{h}(\mathbf{x}, \mathbf{u})$:
>    $$\mathbf{C} = \left. \frac{\partial \mathbf{h}}{\partial \mathbf{x}} \right|_{0}, \quad
>       \mathbf{D} = \left. \frac{\partial \mathbf{h}}{\partial \mathbf{u}} \right|_{0}$$

# Demostración

> [!teorema] Serie de Taylor de primer orden
> Alrededor de $(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\mathbf{f}(\mathbf{x}, \mathbf{u}) = \mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_0 (\mathbf{x} - \mathbf{x}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_0 (\mathbf{u} - \mathbf{u}_0) + \text{términos de orden superior}$$
> 
> Ver [[Serie Taylor]] para la demostración completa y condiciones de validez.
# Ejemplo 1: Péndulo simple (detallado)

> [!ejemplo] Modelo no lineal
> $$ml^2 \ddot{\theta} + b\dot{\theta} + mgl \sin \theta = u$$
> 
> **Paso 1:** Variables de estado:
> $$x_1 = \theta, \quad x_2 = \dot{\theta}$$
> 
> **Paso 2:** Ecuaciones de estado:
> $$\dot{x}_1 = x_2 = f_1(x_1, x_2, u)$$
> $$\dot{x}_2 = -\frac{b}{ml^2} x_2 - \frac{g}{l} \sin x_1 + \frac{1}{ml^2} u = f_2(x_1, x_2, u)$$
> 
> **Paso 3:** Punto de equilibrio: $\theta_0 = 0$, $\dot{\theta}_0 = 0$, $u_0 = 0$
> 
> Verificación: $f_1 = 0$, $f_2 = 0 - 0 + 0 = 0$ ✓
> 
> **Paso 4:** Calcular derivadas parciales para $\mathbf{A}$:
> 
> $$\frac{\partial f_1}{\partial x_1} = \frac{\partial}{\partial x_1}(x_2) = 0$$
> 
> $$\frac{\partial f_1}{\partial x_2} = \frac{\partial}{\partial x_2}(x_2) = 1$$
> 
> $$\frac{\partial f_2}{\partial x_1} = \frac{\partial}{\partial x_1}\left(-\frac{b}{ml^2} x_2 - \frac{g}{l} \sin x_1 + \frac{1}{ml^2} u\right) = -\frac{g}{l} \cos x_1$$
> 
> En $x_1 = 0$: $\cos 0 = 1$, entonces $\left. \frac{\partial f_2}{\partial x_1} \right|_0 = -\frac{g}{l}$
> 
> $$\frac{\partial f_2}{\partial x_2} = \frac{\partial}{\partial x_2}\left(-\frac{b}{ml^2} x_2 - \frac{g}{l} \sin x_1 + \frac{1}{ml^2} u\right) = -\frac{b}{ml^2}$$
> 
> **Paso 5:** Jacobiana $\mathbf{A}$:
> $$\mathbf{A} = \begin{bmatrix}
> 0 & 1 \\
> -\frac{g}{l} & -\frac{b}{ml^2}
> \end{bmatrix}$$
> 
> **Paso 6:** Derivadas parciales para $\mathbf{B}$:
> 
> $$\frac{\partial f_1}{\partial u} = \frac{\partial}{\partial u}(x_2) = 0$$
> 
> $$\frac{\partial f_2}{\partial u} = \frac{\partial}{\partial u}\left(-\frac{b}{ml^2} x_2 - \frac{g}{l} \sin x_1 + \frac{1}{ml^2} u\right) = \frac{1}{ml^2}$$
> 
> **Paso 7:** Jacobiana $\mathbf{B}$:
> $$\mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{ml^2} \end{bmatrix}$$
> 
> **Paso 8:** Sistema linealizado:
> $$\delta \dot{x}_1 = \delta x_2$$
> $$\delta \dot{x}_2 = -\frac{g}{l} \delta x_1 - \frac{b}{ml^2} \delta x_2 + \frac{1}{ml^2} \delta u$$

# Ejemplo 2: Péndulo invertido (punto inestable)

> [!ejemplo] Mismo péndulo, otro punto de equilibrio
> Punto de operación: $\theta_0 = \pi$, $\dot{\theta}_0 = 0$, $u_0 = 0$
> 
> Verificación: $\sin \pi = 0$, $f_2 = 0 - 0 + 0 = 0$ ✓
> 
> La única derivada que cambia es $\frac{\partial f_2}{\partial x_1} = -\frac{g}{l} \cos x_1$
> 
> En $x_1 = \pi$: $\cos \pi = -1$, entonces $\left. \frac{\partial f_2}{\partial x_1} \right|_0 = -\frac{g}{l} \cdot (-1) = \frac{g}{l}$
> 
> $$\mathbf{A} = \begin{bmatrix}
> 0 & 1 \\
> \frac{g}{l} & -\frac{b}{ml^2}
> \end{bmatrix}$$
> 
> El autovalor $\sqrt{g/l}$ es positivo → sistema inestable (péndulo invertido).

# Ejemplo 3: Sistema mecánico con no linealidad cúbica

> [!ejemplo] Resorte duro
> $$m\ddot{y} + b\dot{y} + k y + \alpha y^3 = u$$
> 
> **Paso 1:** Estados: $x_1 = y$, $x_2 = \dot{y}$
> 
> **Paso 2:** Ecuaciones:
> $$\dot{x}_1 = x_2 = f_1$$
> $$\dot{x}_2 = -\frac{k}{m} x_1 - \frac{b}{m} x_2 - \frac{\alpha}{m} x_1^3 + \frac{1}{m} u = f_2$$
> 
> **Paso 3:** Punto de equilibrio: $x_{10} = 0$, $x_{20} = 0$, $u_0 = 0$
> 
> **Paso 4:** Derivadas parciales:
> 
> $\frac{\partial f_1}{\partial x_1} = 0$, $\frac{\partial f_1}{\partial x_2} = 1$
> 
> $\frac{\partial f_2}{\partial x_1} = -\frac{k}{m} - \frac{3\alpha}{m} x_1^2$
> 
> En $x_1 = 0$: $\left. \frac{\partial f_2}{\partial x_1} \right|_0 = -\frac{k}{m}$
> 
> $\frac{\partial f_2}{\partial x_2} = -\frac{b}{m}$
> 
> $\frac{\partial f_2}{\partial u} = \frac{1}{m}$
> 
> **Paso 5:** Matrices linealizadas:
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}, \quad
>    \mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix}$$
> 
> La no linealidad cúbica **desaparece** en la linealización alrededor de $x_1=0$.

# Validez de la aproximación

> [!info] Condiciones
> - Las desviaciones $\delta \mathbf{x}$ y $\delta \mathbf{u}$ deben ser **pequeñas**
> - El sistema original debe ser **continuamente diferenciable**
> - El punto de operación debe ser un **punto de equilibrio** ($\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$)

> [!warning] Limitaciones
> 1. La aproximación lineal **no es válida** para grandes desviaciones
> 2. Puede perder fenómenos como: ciclos límite, bifurcaciones, caos
> 3. La estabilidad del sistema linealizado **no garantiza** la estabilidad global del sistema no lineal

# Variables de desviación

> [!info] Definición
> $$\delta \mathbf{x} = \mathbf{x} - \mathbf{x}_0, \quad \delta \mathbf{u} = \mathbf{u} - \mathbf{u}_0, \quad \delta \mathbf{y} = \mathbf{y} - \mathbf{y}_0$$
> 
> En variables de desviación, el sistema linealizado tiene punto de equilibrio en el origen.
> 
> Ver [[Variables Desviacion]] para ejemplos y propiedades.

# Uso en control

> [!info] Aplicaciones
> 1. Diseño de controladores alrededor de puntos de operación
> 2. Análisis de estabilidad local (criterio de Routh-Hurwitz, lugar de raíces)
> 3. Estimación de ganancias para control PID
> 4. Modelado de sistemas para control predictivo (MPC)

# Limitaciones generales

> [!warning]
> 1. La linealización **no captura** dinámicas no lineales como saturación, histéresis, fricción estática
> 2. Para sistemas con múltiples puntos de equilibrio, se necesita linealizar **cada uno**
> 3. Algunos sistemas (ej. osciladores) requieren análisis no lineal incluso para pequeñas señales
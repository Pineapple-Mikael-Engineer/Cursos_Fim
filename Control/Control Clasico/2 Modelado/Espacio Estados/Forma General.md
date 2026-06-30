---
title: Forma General de Espacio de Estados
order: 1
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

> [!definicion]
> La forma general de un sistema LTI continuo de orden $n$, $m$ entradas y $p$ salidas es:
> $$\dot{\mathbf{x}}(t)=\mathbf{A}\mathbf{x}(t)+\mathbf{B}\mathbf{u}(t),\qquad \mathbf{y}(t)=\mathbf{C}\mathbf{x}(t)+\mathbf{D}\mathbf{u}(t),\qquad \mathbf{x}(0)=\mathbf{x}_0.$$
> $\mathbf{A}$ propaga el estado, $\mathbf{B}$ inyecta la entrada al estado, $\mathbf{C}$ lee el estado en la salida y $\mathbf{D}$ pasa la entrada directo a la salida.

> [!info]
> Subnota del módulo de [[index | espacio de estados]]: aquí se fija el significado y las dimensiones de $A,B,C,D$, el diagrama de bloques y la solución $e^{\mathbf{A}t}$. Para convertir entre representaciones ver [[Pasar a FT]] y [[Pasar desde FT]].

---

## Ejemplo

> [!ejemplo] Identificar $A,B,C,D$ con matrices concretas
> Sea el sistema de segundo orden
> $$\dot{\mathbf{x}}=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}\mathbf{x}+\begin{bmatrix}0\\1\end{bmatrix}u,\qquad y=\begin{bmatrix}1&0\end{bmatrix}\mathbf{x}+0\cdot u.$$
>
> **Lectura de cada matriz** ($n=2$, $m=1$, $p=1$, sistema SISO):
> - $\mathbf{A}=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}$ ($2\times2$): la fila 1 dice $\dot{x}_1=x_2$; la fila 2, $\dot{x}_2=-2x_1-3x_2$.
> - $\mathbf{B}=\begin{bmatrix}0\\1\end{bmatrix}$ ($2\times1$): la entrada solo actúa sobre $\dot{x}_2$.
> - $\mathbf{C}=\begin{bmatrix}1&0\end{bmatrix}$ ($1\times2$): se mide $y=x_1$.
> - $\mathbf{D}=0$ ($1\times1$): no hay alimentación directa → sistema estrictamente propio.
>
> **Dinámica.** $\det(s\mathbf{I}-\mathbf{A})=s^2+3s+2=(s+1)(s+2)$ → autovalores $-1,-2$, estable.

> [!ejemplo] Diagrama de la representación de estados
> ![[ee_forma_general.svg|620]]
>
> Estructura de $\dot{x}=Ax+Bu,\ y=Cx+Du$: la entrada pasa por $B$, se integra en el bloque $\tfrac1s\mathbf{I}$ (de $\dot{x}$ a $x$), $A$ realimenta el estado y $D$ lo transmite directo a la salida junto con $Cx$.

> [!ejemplo] Cambio de base (intercambiar estados)
> Con la misma $\mathbf{A}=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}$ y $\mathbf{T}=\mathbf{T}^{-1}=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ (permuta $x_1\leftrightarrow x_2$):
> $$\tilde{\mathbf{A}}=\mathbf{T}\mathbf{A}\mathbf{T}^{-1}=\begin{bmatrix}-3&-2\\1&0\end{bmatrix}.$$
> El sistema transformado describe la **misma** dinámica (mismos autovalores $-1,-2$): la representación no es única.

---

## En qué consiste

> [!info] Tamaño y significado de las matrices
> | Matriz | Dimensión | Significado |
> |---|---|---|
> | $\mathbf{A}$ | $n\times n$ | dinámica del sistema |
> | $\mathbf{B}$ | $n\times m$ | influencia de las entradas |
> | $\mathbf{C}$ | $p\times n$ | medición de los estados |
> | $\mathbf{D}$ | $p\times m$ | alimentación directa |
> | $\mathbf{x},\mathbf{u},\mathbf{y}$ | $n\times1,\ m\times1,\ p\times1$ | estado, entrada, salida |

> [!info] Clasificación según $\mathbf{D}$
> - $\mathbf{D}=\mathbf{0}$: **estrictamente propio** (lo más común).
> - $\mathbf{D}\neq\mathbf{0}$: **bipropio** (hay alimentación directa).
> - $\mathbf{D}$ con términos infinitos: **impropio**, no realizable físicamente.

> [!definicion] Sistema discreto
> La versión en tiempo discreto reemplaza la derivada por un avance:
> $$\mathbf{x}[k+1]=\mathbf{A}_d\mathbf{x}[k]+\mathbf{B}_d\mathbf{u}[k],\qquad \mathbf{y}[k]=\mathbf{C}_d\mathbf{x}[k]+\mathbf{D}_d\mathbf{u}[k].$$

> [!teorema] Cambio de base
> Sea $\mathbf{z}=\mathbf{T}\mathbf{x}$ con $\mathbf{T}$ invertible. La dinámica en las nuevas variables es:
> $$\tilde{\mathbf{A}}=\mathbf{T}\mathbf{A}\mathbf{T}^{-1},\quad \tilde{\mathbf{B}}=\mathbf{T}\mathbf{B},\quad \tilde{\mathbf{C}}=\mathbf{C}\mathbf{T}^{-1},\quad \tilde{\mathbf{D}}=\mathbf{D}.$$

> [!demostracion]
> Derivando $\mathbf{z}=\mathbf{T}\mathbf{x}$:
> $$\dot{\mathbf{z}}=\mathbf{T}\dot{\mathbf{x}}=\mathbf{T}(\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u})=\mathbf{T}\mathbf{A}\mathbf{T}^{-1}\mathbf{z}+\mathbf{T}\mathbf{B}\mathbf{u}.$$
> Y la salida $\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}=\mathbf{C}\mathbf{T}^{-1}\mathbf{z}+\mathbf{D}\mathbf{u}$. Como $\mathbf{T}$ es solo un cambio de coordenadas, los autovalores y la FT no cambian.

---

## Solución de la ecuación de estado

> [!teorema] Solución general (tiempo continuo)
> $$\mathbf{x}(t)=e^{\mathbf{A}t}\mathbf{x}(0)+\int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau)\,d\tau,$$
> donde $e^{\mathbf{A}t}=\sum_{k=0}^\infty \dfrac{\mathbf{A}^k t^k}{k!}$ es la **matriz exponencial** (matriz de transición de estado).

> [!demostracion] Verificación por derivación
> Derivando la solución propuesta:
> $$\frac{d}{dt}e^{\mathbf{A}t}\mathbf{x}(0)=\mathbf{A}e^{\mathbf{A}t}\mathbf{x}(0),$$
> $$\frac{d}{dt}\int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau)\,d\tau=\mathbf{B}\mathbf{u}(t)+\mathbf{A}\int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau)\,d\tau.$$
> Sumando: $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$, y en $t=0$ se recupera $\mathbf{x}(0)$. $\blacksquare$

> [!info] Propiedades de $e^{\mathbf{A}t}$
> 1. $e^{\mathbf{A}\cdot0}=\mathbf{I}$.
> 2. $\dfrac{d}{dt}e^{\mathbf{A}t}=\mathbf{A}e^{\mathbf{A}t}=e^{\mathbf{A}t}\mathbf{A}$.
> 3. $e^{\mathbf{A}(t_1+t_2)}=e^{\mathbf{A}t_1}e^{\mathbf{A}t_2}$.
> 4. $(e^{\mathbf{A}t})^{-1}=e^{-\mathbf{A}t}$.
> 5. Si $\mathbf{A}$ es diagonal: $e^{\mathbf{A}t}=\operatorname{diag}(e^{\lambda_1 t},\dots,e^{\lambda_n t})$.
>
> En la práctica se calcula vía Laplace: $e^{\mathbf{A}t}=\mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$.

> [!ejemplo] Primer orden (circuito RC)
> Ecuación $RC\dot{v}_c+v_c=v_i$. Con estado $x=v_c$, entrada $u=v_i$, salida $y=v_c$:
> $$A=-\frac{1}{RC},\quad B=\frac{1}{RC},\quad C=1,\quad D=0,$$
> $$x(t)=e^{-t/RC}x(0)+\frac{1}{RC}\int_0^t e^{-(t-\tau)/RC}u(\tau)\,d\tau.$$

> [!definicion] Forma general no lineal
> $$\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u},t),\qquad \mathbf{y}=\mathbf{h}(\mathbf{x},\mathbf{u},t).$$
> Para análisis local se [[Linealizacion/index | linealiza]] en torno a un punto de operación, obteniendo $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$ como jacobianos.

---

## Limitaciones

> [!warning]
> 1. La solución con $e^{\mathbf{A}t}$ es difícil de calcular analíticamente para $n>3$; en la práctica se simula numéricamente.
> 2. La elección de variables de estado no es única.
> 3. La forma no lineal requiere linealizar para aplicar las herramientas LTI.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Continuo | $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u},\ \mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$ |
> | Discreto | $\mathbf{x}[k+1]=\mathbf{A}_d\mathbf{x}[k]+\mathbf{B}_d\mathbf{u}[k]$ |
> | Dimensiones | $A_{n\times n},B_{n\times m},C_{p\times n},D_{p\times m}$ |
> | Solución | $\mathbf{x}(t)=e^{\mathbf{A}t}\mathbf{x}(0)+\int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}\,d\tau$ |
> | Cambio de base | $\tilde A=TAT^{-1},\ \tilde B=TB,\ \tilde C=CT^{-1},\ \tilde D=D$ |

> [!corolario]
> $A,B,C,D$ codifican respectivamente la dinámica, la inyección de entrada, la medición y la alimentación directa; sus dimensiones se fijan por $(n,m,p)$. La solución se construye con la matriz exponencial $e^{\mathbf{A}t}$, y todo cambio de base $\mathbf{T}$ deja invariantes autovalores y FT. De aquí se salta a $G(s)$ con [[Pasar a FT]] o se construye una realización con [[Pasar desde FT]].

> [!referencia]
> - Módulo padre: [[index]].
> - De estados a FT: [[Pasar a FT]].
> - De FT a estados: [[Pasar desde FT]].
> - Caso no lineal: [[Linealizacion/index]].

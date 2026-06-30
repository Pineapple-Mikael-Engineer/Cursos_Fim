---
title: Espacio de Estados
order: 4
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - espacio estados
  - representación en estados
  - variables de estado
---

# Espacio de Estados

> [!definicion]
> La representación en **espacio de estados** describe un sistema dinámico de orden $n$ mediante un vector de estados $\mathbf{x}\in\mathbb{R}^n$, $m$ entradas $\mathbf{u}$ y $p$ salidas $\mathbf{y}$:
> $$\dot{\mathbf{x}}(t)=\mathbf{A}\mathbf{x}(t)+\mathbf{B}\mathbf{u}(t),\qquad \mathbf{y}(t)=\mathbf{C}\mathbf{x}(t)+\mathbf{D}\mathbf{u}(t).$$
> $\mathbf{A}_{n\times n}$ (dinámica), $\mathbf{B}_{n\times m}$ (entrada), $\mathbf{C}_{p\times n}$ (salida), $\mathbf{D}_{p\times m}$ (transmisión directa). Convierte una EDO de orden $n$ en $n$ EDOs de primer orden acopladas.

> [!info]
> Es la representación matricial del modelado, alternativa a la [[Funcion Transferencia/index | función transferencia]]. Sus subnotas detallan la [[Forma General | forma general]] (significado de $A,B,C,D$), cómo [[Pasar a FT | pasar a FT]] vía $G(s)=C(sI-A)^{-1}B+D$ y cómo [[Pasar desde FT | pasar desde una FT]] mediante formas canónicas. Maneja sistemas MIMO, condiciones iniciales y es la base de la [[Linealizacion/index | linealización]].

---

## Ejemplo

> [!ejemplo]
> **Plantear un sistema masa-resorte-amortiguador en espacio de estados.** Sea $m\ddot{y}+b\dot{y}+ky=u$, con $m=1$, $b=3$, $k=2$. Obtener $A,B,C,D$ midiendo la posición.
>
> **Paso 1 — Elegir variables de estado** (una por cada orden de la EDO):
> $$x_1=y\ \text{(posición)},\qquad x_2=\dot{y}\ \text{(velocidad)}.$$
>
> **Paso 2 — Escribir las derivadas.** La primera es inmediata; la segunda se despeja de la EDO $\ddot{y}=\tfrac{1}{m}(-b\dot{y}-ky+u)$:
> $$\dot{x}_1=x_2,\qquad \dot{x}_2=-\frac{k}{m}x_1-\frac{b}{m}x_2+\frac{1}{m}u.$$
>
> **Paso 3 — Forma matricial** (sustituyendo $m=1,b=3,k=2$):
> $$\dot{\mathbf{x}}=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}\mathbf{x}+\begin{bmatrix}0\\1\end{bmatrix}u,\qquad y=\begin{bmatrix}1&0\end{bmatrix}\mathbf{x}+0\cdot u.$$
>
> **Paso 4 — Verificar la dinámica.** Los autovalores de $\mathbf{A}$ son las raíces de $\det(s\mathbf{I}-\mathbf{A})=s^2+3s+2=(s+1)(s+2)$, es decir $\lambda=-1,-2$: sistema estable y sobreamortiguado. Coinciden con los polos de su FT $G(s)=\dfrac{1}{s^2+3s+2}$.
>
> ![[espacio_estados_diagrama.svg|600]]
>
> El diagrama muestra la estructura interna: el integrador genera $\mathbf{x}$, $\mathbf{A}$ la realimenta y $\mathbf{C}$ extrae la salida.

> [!ejemplo]
> **Sistema MIMO desacoplado.** Dos subsistemas de primer orden independientes con dos entradas y dos salidas:
> $$\dot{\mathbf{x}}=\begin{bmatrix}-1&0\\0&-2\end{bmatrix}\mathbf{x}+\begin{bmatrix}1&0\\0&1\end{bmatrix}\mathbf{u},\qquad \mathbf{y}=\begin{bmatrix}1&0\\0&1\end{bmatrix}\mathbf{x}.$$
> Aquí $n=2$, $m=2$, $p=2$: $\mathbf{B}$ y $\mathbf{C}$ son $2\times2$. La diagonal de $\mathbf{A}$ muestra dos modos desacoplados $e^{-t}$ y $e^{-2t}$. La FT es ahora una **matriz** $\mathbf{G}(s)=\operatorname{diag}\!\big(\tfrac{1}{s+1},\tfrac{1}{s+2}\big)$.

---

## En qué consiste

> [!teoria]
> El estado $\mathbf{x}(t)$ es la mínima información que, junto con la entrada futura $\mathbf{u}(t)$, determina por completo la evolución del sistema. La **ecuación de estado** $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$ describe la dinámica interna; la **ecuación de salida** $\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$ extrae lo que se mide. Una EDO de orden $n$ se reescribe como $n$ ecuaciones de primer orden tomando como estados la variable y sus $n-1$ derivadas.

> [!info] SISO vs MIMO
> | Caso | $\mathbf{u}$ | $\mathbf{B}$ | $\mathbf{y}$ | $\mathbf{C}$ | $\mathbf{D}$ |
> |---|---|---|---|---|---|
> | SISO | escalar | $n\times1$ | escalar | $1\times n$ | escalar |
> | MIMO | $m\times1$ | $n\times m$ | $p\times1$ | $p\times n$ | $p\times m$ |

> [!info] Ventajas sobre la función transferencia
> 1. **Condiciones iniciales:** se incorporan de forma natural ($\mathbf{x}(0)=\mathbf{x}_0$).
> 2. **MIMO:** maneja múltiples entradas/salidas con la misma notación.
> 3. **No lineales y variantes:** base para [[Linealizacion/index | linealizar]] y admite $\mathbf{A}(t),\mathbf{B}(t),\dots$
> 4. **Análisis interno:** permite estudiar controlabilidad, observabilidad y estabilidad interna, invisibles para $G(s)$.

> [!teorema] Relación con la función transferencia
> Para un sistema SISO, tomando Laplace con CI nulas:
> $$G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}.$$
> En MIMO el resultado es la matriz de transferencia $\mathbf{G}(s)\in\mathbb{C}^{p\times m}$. Detalle y demostración en [[Pasar a FT]].

> [!teorema] Estabilidad interna
> $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}$ es asintóticamente estable si y solo si todos los autovalores de $\mathbf{A}$ tienen parte real negativa:
> $$\Re\big(\lambda_i(\mathbf{A})\big)<0\quad\forall i.$$
> Equivale a que todos los polos de $\mathbf{G}(s)$ cumplan $\Re(p_i)<0$ **si no hay cancelaciones polo-cero**.

> [!info] Formas canónicas (realizaciones)
> | Forma | Característica | Uso |
> |---|---|---|
> | Controlable | controlabilidad explícita | ubicación de polos |
> | Observable | observabilidad explícita | diseño de observadores |
> | Diagonal | polos en la diagonal (desacoplado) | análisis modal |
> | Jordan | polos repetidos | autovalores múltiples |
>
> Construcción de cada una desde una FT en [[Pasar desde FT]].

---

## Limitaciones

> [!warning]
> 1. Para orden alto, las matrices $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$ crecen y el cálculo manual se vuelve inviable.
> 2. La elección de variables de estado **no es única**; una mala elección complica el modelo.
> 3. La transformación a formas canónicas puede ser numéricamente sensible.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ecuación de estado | $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$ |
> | Ecuación de salida | $\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$ |
> | Dimensiones | $\mathbf{A}_{n\times n},\ \mathbf{B}_{n\times m},\ \mathbf{C}_{p\times n},\ \mathbf{D}_{p\times m}$ |
> | Estados | variable y sus $n-1$ derivadas |
> | A FT | $G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$ |
> | Estabilidad | $\Re(\lambda_i(\mathbf{A}))<0$ |

> [!corolario]
> Espacio de estados reescribe una EDO de orden $n$ como $n$ ecuaciones de primer orden $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$, $\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$. Frente a la FT gana en sistemas MIMO, condiciones iniciales y análisis interno; los autovalores de $\mathbf{A}$ son los polos del sistema. Ver la [[Forma General | forma general]] y los puentes [[Pasar a FT]] / [[Pasar desde FT]].

> [!referencia]
> - Significado de $A,B,C,D$: [[Forma General]].
> - De estados a FT: [[Pasar a FT]].
> - De FT a estados: [[Pasar desde FT]].
> - Representación alternativa: [[Funcion Transferencia/index]].

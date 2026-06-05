---
title: Construcción del Sistema Tridiagonal Lineal
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - diferencias-finitas
  - sistemas-lineales
draft: false
aliases:
  - Sistema tridiagonal del PVF
  - Ensamblaje de diferencias finitas
  - Tridiagonal BVP system
---

# Construcción del Sistema Tridiagonal Lineal

> [!definicion]
> Al [[Discretizacion Dominio y Aproximacion Centrada|discretizar]] un PVF lineal en $N-1$ nodos internos, las ecuaciones nodales se ensamblan en un **sistema lineal tridiagonal** $A\mathbf{y} = \mathbf{b}$, donde cada fila relaciona un nodo con sus dos vecinos. Se resuelve en $O(N)$ por el algoritmo de Thomas.

> [!info]
> La estructura tridiagonal es consecuencia directa de las [[Discretizacion Dominio y Aproximacion Centrada|diferencias centradas]], que solo acoplan nodos contiguos. Es la misma matriz que aparece en los [[Condiciones Continuidad C2 y Sistema Tridiagonal|splines cúbicos]], y hereda su resolución eficiente y, a menudo, su [[Teorema Diagonal Dominante Estricta|diagonal dominancia]].

---

## Ensamblaje del sistema

> [!teorema]
> Para el PVF lineal $y'' = p(x)y' + q(x)y + r(x)$ con $y(a)=\alpha$, $y(b)=\beta$, la ecuación nodal en $i=1,\dots,N-1$,
> $$\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = p_i\frac{y_{i+1}-y_{i-1}}{2h} + q_i y_i + r_i,$$
> se reordena como $a_i y_{i-1} + b_i y_i + c_i y_{i+1} = d_i$ con
> $$a_i = 1 + \tfrac{h}{2}p_i, \qquad b_i = -(2 + h^2 q_i), \qquad c_i = 1 - \tfrac{h}{2}p_i, \qquad d_i = h^2 r_i.$$

> [!info]
> Las incógnitas son los $N-1$ valores internos $y_1,\dots,y_{N-1}$; los valores de frontera $y_0=\alpha$, $y_N=\beta$ son conocidos y pasan al lado derecho en la primera y última ecuación (condiciones [[Tratamiento Condiciones Frontera Dirichlet Neumann|Dirichlet]]).

---

## Estructura de la matriz

> [!teorema]
> El sistema $A\mathbf y = \mathbf b$ tiene forma **tridiagonal**:
> $$\begin{pmatrix} b_1 & c_1 & & \\ a_2 & b_2 & c_2 & \\ & \ddots & \ddots & \ddots \\ & & a_{N-1} & b_{N-1} \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_{N-1} \end{pmatrix} = \begin{pmatrix} d_1 - a_1\alpha \\ d_2 \\ \vdots \\ d_{N-1} - c_{N-1}\beta \end{pmatrix}.$$
> Los términos de frontera $a_1\alpha$ y $c_{N-1}\beta$ se restan al lado derecho.

> [!info]
> **Diagonal dominancia.** Si $q(x) \geq 0$ y $h$ es suficientemente pequeño ($\frac{h}{2}|p_i| < 1$), la matriz es estrictamente [[Teorema Diagonal Dominante Estricta|diagonal dominante]]: $|b_i| = 2+h^2q_i \geq |a_i|+|c_i| = 2$. Esto garantiza solución única y estabilidad del algoritmo de Thomas sin pivoteo.

---

## Algoritmo de Thomas

> [!algoritmo]
> **Resolución tridiagonal $O(N)$** (la misma de los [[Condiciones Continuidad C2 y Sistema Tridiagonal|splines]]).
>
> ```python
> import numpy as np
>
> def thomas(a, b, c, d):
>     """Resuelve sistema tridiagonal: a_i y_{i-1} + b_i y_i + c_i y_{i+1} = d_i."""
>     n = len(b)
>     cp, dp = np.zeros(n), np.zeros(n)
>     cp[0], dp[0] = c[0]/b[0], d[0]/b[0]
>     for i in range(1, n):                       # eliminación hacia adelante
>         m = b[i] - a[i]*cp[i-1]
>         cp[i] = c[i]/m
>         dp[i] = (d[i] - a[i]*dp[i-1])/m
>     y = np.zeros(n)
>     y[-1] = dp[-1]
>     for i in range(n-2, -1, -1):                # sustitución hacia atrás
>         y[i] = dp[i] - cp[i]*y[i+1]
>     return y
> ```
>
> Costo $O(N)$ en tiempo y memoria, frente al $\frac{2}{3}N^3$ de un sistema denso.

---

## Ejemplo completo

> [!ejemplo]
> **$y'' = -y + x$, $y(0)=0$, $y(1)=0$**, $N=4$, $h=0.25$. Aquí $p=0$, $q=-1$, $r=x$, así $a_i=c_i=1$, $b_i=-(2-h^2)=-1.9375$, $d_i = h^2 x_i$:
>
> $$\begin{pmatrix} -1.9375 & 1 & 0 \\ 1 & -1.9375 & 1 \\ 0 & 1 & -1.9375 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = \begin{pmatrix} 0.0156 \\ 0.0313 \\ 0.0469 \end{pmatrix}.$$
>
> Thomas da $y \approx (-0.0356, -0.0492, -0.0376)$, que aproxima la solución exacta $y(x) = x - \frac{\sin x}{\sin 1}$ con error $O(h^2)$.

---

## Caso no lineal

> [!warning]
> Si el PVF es **no lineal** ($y'' = f(x,y,y')$ con $f$ no lineal en $y, y'$), la discretización produce un **sistema no lineal** de ecuaciones, que se resuelve por [[Newton Raphson Multivariable/index|Newton multivariable]]. La jacobiana resulta también tridiagonal, así que cada iteración de Newton sigue costando $O(N)$.

---

## Relación con otras notas

> [!info]
> - La discretización que genera las ecuaciones: [[Discretizacion Dominio y Aproximacion Centrada]].
> - La misma estructura en splines: [[Condiciones Continuidad C2 y Sistema Tridiagonal]].
> - La diagonal dominancia que da estabilidad: [[Teorema Diagonal Dominante Estricta]].
> - El caso no lineal: [[Newton Raphson Multivariable/index]].
> - Las fronteras Neumann que cambian la matriz: [[Tratamiento Condiciones Frontera Dirichlet Neumann]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Sistema | $A\mathbf y = \mathbf b$, tridiagonal |
| Coeficientes | $a_i=1+\tfrac h2 p_i$, $b_i=-(2+h^2q_i)$, $c_i=1-\tfrac h2 p_i$ |
| Frontera Dirichlet | $\alpha,\beta$ pasan al lado derecho |
| Diagonal dominante | si $q\geq0$ y $h$ pequeño |
| Resolución | Thomas, $O(N)$ |
| No lineal | Newton (jacobiana tridiagonal) |

> [!corolario]
> Las ecuaciones nodales del PVF discretizado se ensamblan en un sistema tridiagonal $A\mathbf y=\mathbf b$, con coeficientes derivados de las diferencias centradas y los valores de frontera incorporados al lado derecho. La matriz es a menudo [[Teorema Diagonal Dominante Estricta|diagonal dominante]] (si $q\geq0$), lo que garantiza solución única y permite resolverla en $O(N)$ por el algoritmo de Thomas —el mismo de los [[Condiciones Continuidad C2 y Sistema Tridiagonal|splines cúbicos]]—. Para PVF no lineales, la discretización da un sistema resuelto por [[Newton Raphson Multivariable/index|Newton]] con jacobiana también tridiagonal. La convergencia de la solución discreta a la exacta la asegura el [[Consistencia Estabilidad Convergencia Lax|teorema de Lax]].

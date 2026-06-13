---
title: Condiciones de Continuidad C² y Sistema Tridiagonal
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
  - sistemas-lineales
draft: false
aliases:
  - Sistema tridiagonal de splines
  - Continuidad C2
  - Momentos del spline
  - Tridiagonal spline system
---

# Condiciones de Continuidad $C^2$ y Sistema Tridiagonal

> [!definicion]
> La construcción del [[Splines Cubicos Naturales Sujetos|spline cúbico]] reduce las condiciones de continuidad $C^2$ a un **sistema lineal tridiagonal** para los momentos $M_i = S''(x_i)$ (segundas derivadas en los nodos). Una vez conocidos los $M_i$, cada tramo cúbico queda determinado.

> [!info]
> El sistema es **tridiagonal, simétrico y diagonal dominante**, por lo que se resuelve en $O(n)$ con el algoritmo de Thomas (eliminación gaussiana sin pivoteo, estable aquí). Es el paso computacional central de la interpolación por splines.

---

## Derivación del sistema

> [!teorema]
> Dentro de $[x_i, x_{i+1}]$, $S''$ es lineal: $S_i''(x) = M_i\frac{x_{i+1}-x}{h_i} + M_{i+1}\frac{x-x_i}{h_i}$, con $h_i = x_{i+1}-x_i$. Integrando dos veces e imponiendo $S_i(x_i)=y_i$, $S_i(x_{i+1})=y_{i+1}$ se obtiene $S_i'$. La **continuidad de la primera derivada** $S_{i-1}'(x_i) = S_i'(x_i)$ en cada nodo interno da, para $i=1,\dots,n-1$:
> $$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)\,M_i + h_i\,M_{i+1} = 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}\right).$$

> [!demostracion]
> Integrando $S_i''$ dos veces:
> $$S_i'(x) = -M_i\frac{(x_{i+1}-x)^2}{2h_i} + M_{i+1}\frac{(x-x_i)^2}{2h_i} + \frac{y_{i+1}-y_i}{h_i} - \frac{(M_{i+1}-M_i)h_i}{6}.$$
> Evaluando $S_i'(x_i^+)$ y $S_{i-1}'(x_i^-)$ e igualando (continuidad $C^1$), tras simplificar aparece la ecuación de tres términos en $M_{i-1}, M_i, M_{i+1}$. La continuidad $C^2$ ya está garantizada porque los $M_i$ se comparten entre tramos vecinos.

---

## Estructura tridiagonal

> [!info]
> Las $n-1$ ecuaciones internas forman el sistema
> $$\begin{pmatrix} 2(h_0+h_1) & h_1 & & \\ h_1 & 2(h_1+h_2) & h_2 & \\ & \ddots & \ddots & \ddots \\ & & h_{n-2} & 2(h_{n-2}+h_{n-1}) \end{pmatrix}\!\begin{pmatrix} M_1 \\ M_2 \\ \vdots \\ M_{n-1} \end{pmatrix} = 6\begin{pmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_{n-1} \end{pmatrix},$$
> con $\delta_i = \frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}$. Es **estrictamente diagonal dominante** ($2(h_{i-1}+h_i) > h_{i-1}+h_i$), lo que asegura solución única y estabilidad sin pivoteo (véase [[Teorema Diagonal Dominante Estricta]]).

> [!info]
> **Cierre por frontera.** Las dos ecuaciones faltantes vienen de las condiciones de borde:
> - **Natural:** $M_0 = M_n = 0$ (se eliminan del sistema).
> - **Sujeto:** ecuaciones extra que ligan $M_0, M_1$ (y $M_{n-1}, M_n$) con $f'(a), f'(b)$.

---

## Algoritmo de Thomas

> [!algoritmo]
> **Resolución tridiagonal $O(n)$** del sistema $a_i M_{i-1} + b_i M_i + c_i M_{i+1} = d_i$:
>
> ```
> # Eliminación hacia adelante
> para i = 2 .. n-1:
>     w = a[i] / b[i-1]
>     b[i] = b[i] - w * c[i-1]
>     d[i] = d[i] - w * d[i-1]
> # Sustitución hacia atrás
> M[n-1] = d[n-1] / b[n-1]
> para i = n-2 .. 1:
>     M[i] = (d[i] - c[i] * M[i+1]) / b[i]
> ```
>
> Coste $O(n)$ en tiempo y memoria, frente al $\frac{2}{3}n^3$ de un sistema denso. Es eliminación gaussiana especializada a la estructura tridiagonal.

---

## Ejemplo

> [!ejemplo]
> **Spline natural, nodos $(0,0),(1,1),(2,0),(3,-1)$**, $h_i=1$. Ecuaciones internas ($i=1,2$) con $M_0=M_3=0$:
> $$\begin{cases} 4M_1 + M_2 = 6(\tfrac{0-1}{1}-\tfrac{1-0}{1}) = -12 \\ M_1 + 4M_2 = 6(\tfrac{-1-0}{1}-\tfrac{0-1}{1}) = 0 \end{cases}$$
> Resolviendo el sistema $2\times2$: $M_1 = -\tfrac{16}{5} = -3.2$, $M_2 = \tfrac{4}{5} = 0.8$. Con estos momentos se reconstruyen las tres cúbicas.

---

## Relación con otras notas

> [!info]
> - El spline que este sistema construye: [[Splines Cubicos Naturales Sujetos]].
> - La propiedad de diagonal dominancia que garantiza estabilidad: [[Teorema Diagonal Dominante Estricta]].
> - La eliminación gaussiana que el algoritmo de Thomas especializa: [[Eliminacion Gaussiana]].
> - El sentido variacional del resultado: [[Propiedad Minima Curvatura]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Incógnitas | momentos $M_i = S''(x_i)$ |
| Ecuación interna | $h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_iM_{i+1} = 6\delta_i$ |
| Matriz | tridiagonal, simétrica, diagonal dominante |
| Cierre | natural ($M_0=M_n=0$) o sujeto |
| Solución | algoritmo de Thomas, $O(n)$ |

> [!corolario]
> Las condiciones de continuidad $C^2$ del spline cúbico se reducen, vía continuidad de la primera derivada, a un sistema tridiagonal para los momentos $M_i = S''(x_i)$. La matriz es estrictamente [[Teorema Diagonal Dominante Estricta|diagonal dominante]], lo que garantiza solución única y permite resolverla con el algoritmo de Thomas en $O(n)$ sin pivoteo. Las condiciones de frontera (natural o sujeto) aportan las dos ecuaciones restantes. Resuelto el sistema, las cúbicas quedan determinadas, completando la construcción del [[Splines Cubicos Naturales Sujetos|spline cúbico]] cuya [[Propiedad Minima Curvatura|mínima curvatura]] justifica su suavidad.

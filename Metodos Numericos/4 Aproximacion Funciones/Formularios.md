---
title: Formulario — Aproximación de Funciones
order: 99
tags:
  - metodos-numericos
  - formulario
  - aproximacion
draft: false
aliases:
  - formulario aproximacion de funciones
  - formulas interpolacion y ajuste
---

# Formulario — Aproximación de Funciones

## Mínimos cuadrados — Residuos y norma euclídea

**Modelo lineal en los parámetros** — $c_j$ coeficientes, $\varphi_j$ funciones base.
$$\phi(x; c) = \sum_{j=1}^n c_j\varphi_j(x)$$

**Vector de residuos y matriz de diseño** — $A\in\mathbb{R}^{m\times n}$, datos $\{(x_i,y_i)\}_{i=1}^m$, $m>n$.
$$r = Ac - y, \qquad A_{ij} = \varphi_j(x_i)$$

**Problema de mínimos cuadrados.**
$$\min_{c\in\mathbb{R}^n}\ \|Ac - y\|_2^2 = \min_c \sum_{i=1}^m \big(\textstyle\sum_j c_j\varphi_j(x_i) - y_i\big)^2$$

**Condición de óptimo (ortogonalidad del residuo).**
$$A^T(Ac^* - y) = 0 \quad\Longleftrightarrow\quad A^TA\,c^* = A^Ty$$

**Funcional y gradiente.**
$$J(c) = c^TA^TAc - 2c^TA^Ty + y^Ty, \qquad \nabla J(c) = 2A^TAc - 2A^Ty$$

**Matriz de proyección** — proyecta $y$ sobre $\operatorname{col}(A)$.
$$P = A(A^TA)^{-1}A^T, \qquad P^2 = P, \quad P^T = P$$

**Descomposición del dato.**
$$\hat y = Py, \qquad r = (I-P)y$$

---

## Mínimos cuadrados — Ecuaciones normales y matriz de Gram

**Ecuaciones normales.**
$$A^TA\,c = A^Ty$$

**Matriz de Gram** — $G_{jk}$ producto interno de columnas.
$$G = A^TA \in \mathbb{R}^{n\times n}, \qquad G_{jk} = \varphi_j^T\varphi_k = \sum_i \varphi_j(x_i)\varphi_k(x_i)$$

**Propiedades de $G$.**
$$G^T = G, \qquad c^TGc = \|Ac\|_2^2 \geq 0, \qquad G \text{ definida positiva} \Leftrightarrow \operatorname{rango}(A)=n$$

**Solución (rango completo).**
$$c = G^{-1}A^Ty$$

**Resolución por Cholesky** — $G$ simétrica definida positiva; costo $\approx mn^2 + n^3/3$.
$$G = LL^T, \qquad Lz = b,\quad L^Tc = z, \qquad b = A^Ty$$

**Amplificación del condicionamiento.**
$$\kappa_2(A^TA) = \kappa_2(A)^2$$

---

## Mínimos cuadrados — Condicionamiento y QR

**Número de condición y valores singulares** — $\sigma_1\geq\cdots\geq\sigma_n>0$.
$$\kappa_2(A) = \frac{\sigma_1}{\sigma_n}, \qquad \kappa_2(A^TA) = \frac{\sigma_1^2}{\sigma_n^2} = \kappa_2(A)^2$$

**SVD y autovalores de Gram** — $A = U\Sigma V^T$.
$$A^TA = V\Sigma^2 V^T$$

**Error relativo según método** — $u$ unidad de redondeo.
$$\text{ecuaciones normales: } \sim \kappa_2(A)^2\,u, \qquad \text{método estable en } A: \sim \kappa_2(A)\,u$$

**Dígitos correctos.**
$$\text{ec. normales: } -\log_{10}u - 2\log_{10}\kappa(A), \qquad \text{QR: } -\log_{10}u - \log_{10}\kappa(A)$$

**Factorización QR** — $Q^TQ=I$, $R$ triangular superior.
$$A = QR, \qquad R\,c = Q^T y, \qquad \kappa_2(R) = \kappa_2(A)$$

**Descomposición de la norma.**
$$\|Ac - y\|_2^2 = \|Rc - Q^Ty\|_2^2 + \|(I - QQ^T)y\|_2^2$$

**Costos** — ec. normales $mn^2 + \tfrac{n^3}{3}$; QR $2mn^2 - \tfrac{2n^3}{3}$; SVD $\sim mn^2$.

---

## Mínimos cuadrados — Regresión lineal, polinomial y múltiple

**Modelos.**
$$y = c_0 + c_1 x, \qquad y = c_0 + c_1 x + \cdots + c_p x^p, \qquad y = c_0 + c_1 x_1 + \cdots + c_k x_k$$

**Filas de la matriz de diseño** — recta $[1,\ x_i]$; polinomio $[1, x_i, \dots, x_i^p]$; múltiple $[1, x_{i1}, \dots, x_{ik}]$; en todo caso $A_{ij}=\varphi_j(x_i)$.

**Regresión lineal simple: fórmulas cerradas** — $\bar x,\bar y$ medias; recta pasa por el centroide $(\bar x,\bar y)$.
$$c_1 = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}, \qquad c_0 = \bar y - c_1\bar x$$

**Coeficiente de determinación** — $\hat y_i$ valores ajustados, $r$ residuo.
$$R^2 = 1 - \frac{\sum_i (y_i - \hat y_i)^2}{\sum_i (y_i - \bar y)^2} = 1 - \frac{\|r\|_2^2}{\|y - \bar y\|_2^2}$$

**Modelos linealizables** — $y=a e^{bx}\Rightarrow \ln y = \ln a + bx$; $y=ax^b\Rightarrow \ln y = \ln a + b\ln x$; $y=\tfrac{1}{a+bx}\Rightarrow 1/y = a+bx$.

---

## Interpolación polinómica — Existencia y unicidad

**Problema de interpolación** — $n+1$ nodos distintos, $p\in\mathbb{P}_n$.
$$p(x_i) = y_i, \quad i = 0,\dots,n$$

**Polinomios cardinales (existencia constructiva).**
$$L_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j} \in \mathbb{P}_n, \qquad L_i(x_k) = \delta_{ik}$$

**Interpolador de Lagrange.**
$$p(x) = \sum_{i=0}^n y_i L_i(x)$$

**Sistema de Vandermonde** — base de monomios $p(x)=\sum_j c_j x^j$.
$$V c = y, \qquad V = \begin{pmatrix} 1 & x_0 & \cdots & x_0^n \\ 1 & x_1 & \cdots & x_1^n \\ \vdots & & & \vdots \\ 1 & x_n & \cdots & x_n^n \end{pmatrix}, \qquad \det V = \prod_{0 \leq i < j \leq n} (x_j - x_i)$$

---

## Interpolación polinómica — Matriz de Vandermonde y condicionamiento

**Matriz de Vandermonde** — $V_{ij} = x_i^{\,j}$.
$$V = \begin{pmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^n \\ 1 & x_1 & x_1^2 & \cdots & x_1^n \\ \vdots & & & & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^n \end{pmatrix}, \qquad Vc = y$$

**Determinante.**
$$\det V = \prod_{0 \leq i < j \leq n} (x_j - x_i)$$

**Crecimiento del condicionamiento (nodos equiespaciados).**
$$\kappa_2(V) \sim O\!\big(2^n\big), \qquad \text{dígitos perdidos} \sim n\log_{10}2 \approx 0.3\,n$$

**Costo de resolver $Vc=y$** — $\tfrac{2}{3}n^3$, frente a $O(n^2)$ de Lagrange/Newton.

---

## Interpolación polinómica — Polinomios cardinales de Lagrange

**Definición.**
$$L_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j} \in \mathbb{P}_n$$

**Propiedades.**
$$L_i(x_k) = \delta_{ik}, \qquad \sum_{i=0}^n L_i(x) \equiv 1, \qquad \sum_{i=0}^n x_i^m L_i(x) = x^m \ (0\leq m\leq n)$$

**Interpolador** — $y_i = f(x_i)$.
$$p_n(x) = \sum_{i=0}^n y_i\, L_i(x)$$

**Constante de Lebesgue** — sensibilidad a errores en los datos.
$$\Lambda_n = \max_x \sum_i |L_i(x)|$$

**Pesos de cuadratura (Newton–Cotes).**
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^n w_i\, f(x_i), \qquad w_i = \int_a^b L_i(x)\,dx$$

---

## Interpolación polinómica — Costo y forma baricéntrica (Lagrange)

**Costo evaluación directa** — $O(n^2)$ por punto, $O(mn^2)$ en $m$ puntos, no incremental.

**Pesos baricéntricos** — independientes de $x$ y de $y_i$.
$$w_i = \frac{1}{\prod_{j\neq i}(x_i - x_j)}$$

**Segunda forma baricéntrica** — $x\neq x_i$.
$$p_n(x) = \frac{\displaystyle\sum_{i=0}^n \dfrac{w_i}{x - x_i}\,y_i}{\displaystyle\sum_{i=0}^n \dfrac{w_i}{x - x_i}}$$

**Polinomio nodal auxiliar.**
$$\ell(x) = \prod_{j=0}^n (x - x_j), \qquad L_i(x) = \ell(x)\,\frac{w_i}{x - x_i}, \qquad \ell(x) = \frac{1}{\sum_i \frac{w_i}{x-x_i}}$$

**Pesos para nodos especiales** — equiespaciados $w_i = (-1)^i \binom{n}{i}$; Chebyshev (2.ª especie) $w_i = (-1)^i \delta_i$ con $\delta_i=\tfrac12$ en extremos, $1$ en interior.

**Costo baricéntrico** — precálculo $O(n^2)$, evaluación $O(n)$ por punto, incremental $O(n)$.

---

## Interpolación polinómica — Tabla de diferencias divididas (Newton)

**Diferencia dividida (recurrencia).**
$$f[x_i] = f(x_i), \qquad f[x_i,\dots,x_{i+k}] = \frac{f[x_{i+1},\dots,x_{i+k}] - f[x_i,\dots,x_{i+k-1}]}{x_{i+k} - x_i}$$

**Forma de Newton** — coeficientes $c_k = f[x_0,\dots,x_k]$ (diagonal superior).
$$p_n(x) = \sum_{k=0}^n c_k \prod_{j<k}(x-x_j)$$

**Propiedades** — simetría ante permutación; incrementalidad; coeficiente director $f[x_0,\dots,x_n]$.

**Nodos repetidos (confluentes).**
$$f[x_0, x_0] = f'(x_0), \qquad f[\underbrace{x_0,\dots,x_0}_{k+1}] = \frac{f^{(k)}(x_0)}{k!}$$

---

## Interpolación polinómica — Forma anidada de Horner (Newton)

**Polinomio de Newton.**
$$p_n(x) = c_0 + c_1(x-x_0) + c_2(x-x_0)(x-x_1) + \cdots + c_n\prod_{j=0}^{n-1}(x-x_j)$$

**Forma anidada de Horner.**
$$p_n(x) = c_0 + (x-x_0)\big[c_1 + (x-x_1)\big[c_2 + \cdots + (x-x_{n-1})c_n\big]\big]$$

**Costo** — $O(n)$ por punto, $n$ multiplicaciones (óptimo, teorema de Ostrowski). Horner extendido da derivadas $p_n', p_n'', \dots$ con $O(n)$ adicional por orden.

---

## Interpolación polinómica — Diferencias divididas y derivadas (Hermite)

**Teorema del valor medio para diferencias divididas** — $\xi\in(\min x_i,\max x_i)$.
$$f[x_0, x_1, \dots, x_k] = \frac{f^{(k)}(\xi)}{k!}$$

**Caso $k=1$.**
$$f[x_0,x_1] = \frac{f(x_1)-f(x_0)}{x_1-x_0} = f'(\xi)$$

**Nodos confluentes (Hermite).**
$$f[\underbrace{x_0, \dots, x_0}_{m+1}] = \frac{f^{(m)}(x_0)}{m!}$$

---

## Interpolación polinómica — Error de interpolación (fórmula de Cauchy)

**Error.**
$$e_n(x) = f(x) - p_n(x)$$

**Fórmula de Cauchy** — $f\in C^{n+1}[a,b]$, $\xi_x\in(a,b)$.
$$e_n(x) = \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\,\prod_{i=0}^n (x - x_i)$$

**Polinomio nodal.**
$$\omega(x) = \prod_{i=0}^n (x - x_i), \qquad \omega^{(n+1)} \equiv (n+1)!$$

**Forma con diferencias divididas.**
$$f(x) - p_n(x) = f[x_0, \dots, x_n, x]\,\prod_{i=0}^n (x - x_i)$$

**Cota de error** — $M_{n+1} = \max_{[a,b]}|f^{(n+1)}|$.
$$|e_n(x)| \leq \frac{M_{n+1}}{(n+1)!}\,\max_{x\in[a,b]}\Big|\prod_{i=0}^n(x-x_i)\Big|$$

**Nodos equiespaciados** — paso $h=(b-a)/n$.
$$\max\Big|\prod(x-x_i)\Big| \leq \frac{n!}{4}h^{n+1}, \qquad |e_n(x)| \leq \frac{M_{n+1}}{4(n+1)}\,h^{n+1} = O(h^{n+1})$$

---

## Interpolación polinómica — Fenómeno de Runge y nodos de Chebyshev

**Función de Runge.**
$$f(x) = \frac{1}{1 + 25x^2}, \quad x\in[-1,1]$$

**Constante de Lebesgue (equiespaciados).**
$$\Lambda_n \sim \frac{2^n}{n\log n}$$

**Nodos de Chebyshev en $[-1,1]$.**
$$x_i = \cos\!\left(\frac{2i+1}{2(n+1)}\pi\right) \text{ (ceros)}, \qquad x_i = \cos\!\left(\frac{i\pi}{n}\right) \text{ (extremos, Chebyshev–Lobatto)}$$

**Polinomio nodal mínimo (mónico grado $n+1$).**
$$\max_{[-1,1]}\Big|\prod_{i=0}^n (x - x_i)\Big| = \frac{1}{2^n}$$

**Constante de Lebesgue (Chebyshev).**
$$\Lambda_n \sim \frac{2}{\pi}\log n$$

---

## Splines — Splines lineales y continuidad $C^0$

**Spline lineal en $[x_i, x_{i+1}]$.**
$$S_i(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i}(x - x_i)$$

**Propiedades** — $C^0$ (esquinas), local, sin oscilación, construcción $O(n)$ sin sistema.

**Cota de error** — $f\in C^2[a,b]$, $h = \max_i(x_{i+1}-x_i)$.
$$\max_{[a,b]}|f(x) - S(x)| \leq \frac{h^2}{8}\,\max_{[a,b]}|f''(x)| = O(h^2)$$

**Error por tramo (Cauchy con $n=1$).**
$$f(x) - S_i(x) = \frac{f''(\xi)}{2}(x - x_i)(x - x_{i+1})$$

---

## Splines — Splines cúbicos naturales y sujetos

**Definición** — $S\in C^2[a,b]$, cúbica en cada $[x_i,x_{i+1}]$, $S(x_i)=y_i$, empalmes $C^1$ y $C^2$.

**Grados de libertad** — $4n$ coeficientes, $4n-2$ condiciones, faltan $2$ (frontera).

**Condiciones de frontera** — natural $S''(x_0)=S''(x_n)=0$; sujeto $S'(x_0)=f'(a),\ S'(x_n)=f'(b)$; not-a-knot $S'''$ continua en $x_1$ y $x_{n-1}$.

**Sistema tridiagonal en los momentos** — $M_i=S''(x_i)$, $h_i=x_{i+1}-x_i$, $i=1,\dots,n-1$.
$$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_i M_{i+1} = 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}\right)$$

**Reconstrucción de cada tramo.**
$$S_i(x) = \frac{M_i(x_{i+1}-x)^3 + M_{i+1}(x-x_i)^3}{6h_i} + \Big(\frac{y_i}{h_i} - \frac{M_i h_i}{6}\Big)(x_{i+1}-x) + \Big(\frac{y_{i+1}}{h_i} - \frac{M_{i+1}h_i}{6}\Big)(x-x_i)$$

**Cota de error (sujeto)** — $f\in C^4[a,b]$, $h=\max h_i$.
$$\max_{[a,b]}|f - S| \leq \frac{5}{384}\,h^4\,\max_{[a,b]}|f^{(4)}|, \qquad \max|f' - S'| = O(h^3), \qquad \max|f'' - S''| = O(h^2)$$

---

## Splines — Continuidad $C^2$ y sistema tridiagonal

**Segunda derivada lineal en el tramo** — $h_i=x_{i+1}-x_i$.
$$S_i''(x) = M_i\frac{x_{i+1}-x}{h_i} + M_{i+1}\frac{x-x_i}{h_i}$$

**Primera derivada.**
$$S_i'(x) = -M_i\frac{(x_{i+1}-x)^2}{2h_i} + M_{i+1}\frac{(x-x_i)^2}{2h_i} + \frac{y_{i+1}-y_i}{h_i} - \frac{(M_{i+1}-M_i)h_i}{6}$$

**Ecuación interna** — $\delta_i = \dfrac{y_{i+1}-y_i}{h_i} - \dfrac{y_i-y_{i-1}}{h_{i-1}}$.
$$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)\,M_i + h_i\,M_{i+1} = 6\,\delta_i$$

**Forma matricial tridiagonal.**
$$\begin{pmatrix} 2(h_0+h_1) & h_1 & & \\ h_1 & 2(h_1+h_2) & h_2 & \\ & \ddots & \ddots & \ddots \\ & & h_{n-2} & 2(h_{n-2}+h_{n-1}) \end{pmatrix}\!\begin{pmatrix} M_1 \\ M_2 \\ \vdots \\ M_{n-1} \end{pmatrix} = 6\begin{pmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_{n-1} \end{pmatrix}$$

**Diagonal dominancia estricta.**
$$2(h_{i-1}+h_i) > h_{i-1}+h_i$$

**Cierre por frontera** — natural $M_0=M_n=0$; sujeto ecuaciones extra ligando $M_0,M_1$ y $M_{n-1},M_n$ con $f'(a),f'(b)$.

**Algoritmo de Thomas** — $O(n)$ para $a_i M_{i-1} + b_i M_i + c_i M_{i+1} = d_i$.
$$w = \frac{a_i}{b_{i-1}}, \quad b_i \leftarrow b_i - w\,c_{i-1}, \quad d_i \leftarrow d_i - w\,d_{i-1}; \qquad M_i = \frac{d_i - c_i M_{i+1}}{b_i}$$

---

## Splines — Propiedad de mínima curvatura

**Energía de flexión.**
$$E[g] = \int_a^b \big(g''(x)\big)^2\,dx$$

**Teorema de minimización** — $S$ spline natural, $g\in C^2$ con $g(x_i)=y_i$; igualdad sii $g\equiv S$.
$$\int_a^b \big(S''\big)^2\,dx \;\leq\; \int_a^b \big(g''\big)^2\,dx$$

**Descomposición (término cruzado nulo)** — $e=g-S$.
$$\int_a^b (g'')^2 = \int_a^b (S'')^2 + \int_a^b (e'')^2, \qquad \int_a^b S''\,e''\,dx = 0$$

---

## Splines — Convergencia y estabilidad frente a grado alto

**Convergencia garantizada.**
$$\text{spline lineal: } \|f-S\|_\infty = O(h^2), \qquad \text{spline cúbico: } \|f-S\|_\infty = O(h^4)$$

**Polinomio global equiespaciado.**
$$\|f - p_n\|_\infty \xrightarrow{n\to\infty} \infty \quad \text{(p. ej. función de Runge)}$$

**Constantes de Lebesgue** — polinomio equiespaciado $\sim 2^n$; polinomio Chebyshev $\sim \log n$; spline cúbico acotada $\leq 3$ (independiente de $n$).

**Convergencia espectral (Chebyshev, $f$ analítica).**
$$\|f - p_n\|_\infty = O(\rho^{-n})$$

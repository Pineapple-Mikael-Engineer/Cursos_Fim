---
title: Condición de Contracción y Norma Matricial
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - punto-fijo
  - convergencia
draft: false
aliases:
  - Contracción multivariable
  - Iteración de punto fijo multivariable
  - Condición de contracción
  - Contraction mapping
---

# Condición de Contracción y Norma Matricial

> [!definicion]
> Una **iteración de punto fijo** para $F(x) = 0$ reescribe el problema como $x = G(x)$ e itera $x^{(k+1)} = G(x^{(k)})$, con $G:\mathbb{R}^n\to\mathbb{R}^n$. El punto fijo $x^* = G(x^*)$ es la solución. La iteración converge si $G$ es una **contracción**: existe $L < 1$ tal que
> $$\|G(x) - G(y)\| \leq L\,\|x - y\| \quad \forall x, y \in D.$$

> [!info]
> Es la generalización multivariable del [[Punto Fijo Aproximaciones Sucesivas/index|punto fijo escalar]]: la condición $|g'(r)| < 1$ se reemplaza por $\|J_G\| < 1$, donde $J_G$ es la [[Matriz Jacobiana y Sistema Lineal Asociado|jacobiana]] de $G$ y $\|\cdot\|$ una norma matricial inducida. Es una alternativa a [[Newton Raphson Multivariable/index|Newton]]: más barata por paso (no resuelve sistemas), pero solo lineal.

---

## Teorema de la aplicación contractiva (Banach)

> [!teorema]
> Sea $D \subseteq \mathbb{R}^n$ cerrado y $G: D \to D$ una contracción de constante $L < 1$ en una norma $\|\cdot\|$. Entonces:
> 1. $G$ tiene un **único** punto fijo $x^* \in D$.
> 2. Para todo $x^{(0)} \in D$, la sucesión $x^{(k+1)} = G(x^{(k)})$ converge a $x^*$.
> 3. Se cumplen las cotas de error
> $$\|x^{(k)} - x^*\| \leq \frac{L^k}{1-L}\,\|x^{(1)} - x^{(0)}\| \quad\text{(a priori)}, \qquad \|x^{(k)} - x^*\| \leq \frac{L}{1-L}\,\|x^{(k)} - x^{(k-1)}\| \quad\text{(a posteriori)}.$$

> [!demostracion]
> **Sucesión de Cauchy.** Por contracción, $\|x^{(k+1)} - x^{(k)}\| = \|G(x^{(k)}) - G(x^{(k-1)})\| \leq L\|x^{(k)} - x^{(k-1)}\| \leq L^k\|x^{(1)} - x^{(0)}\|$. Para $m > k$, por desigualdad triangular y suma geométrica:
> $$\|x^{(m)} - x^{(k)}\| \leq \sum_{j=k}^{m-1} L^j\|x^{(1)} - x^{(0)}\| \leq \frac{L^k}{1-L}\|x^{(1)} - x^{(0)}\| \xrightarrow{k\to\infty} 0.$$
> Luego $\{x^{(k)}\}$ es de Cauchy y converge a algún $x^* \in D$ (cerrado). Por continuidad de $G$, $x^* = G(x^*)$.
>
> **Unicidad.** Si $x^*$ e $y^*$ fueran fijos, $\|x^* - y^*\| = \|G(x^*) - G(y^*)\| \leq L\|x^* - y^*\|$, y como $L < 1$ esto fuerza $\|x^* - y^*\| = 0$.

---

## Criterio práctico vía la jacobiana

> [!teorema]
> Si $G \in C^1$ en una vecindad convexa del punto fijo $x^*$, una cota de la constante de contracción es
> $$L = \max_{x}\,\|J_G(x)\|,$$
> con $J_G = \partial G/\partial x$ y cualquier norma matricial inducida. En particular, **la convergencia local está garantizada si**
> $$\rho(J_G(x^*)) \leq \|J_G(x^*)\| < 1,$$
> donde $\rho$ es el [[Criterio Radio Espectral Convergencia|radio espectral]]. El criterio exacto de convergencia local es $\rho(J_G(x^*)) < 1$.

> [!demostracion]
> Por el teorema del valor medio en forma integral, para $x, y$ en la vecindad convexa,
> $$G(x) - G(y) = \int_0^1 J_G\big(y + t(x - y)\big)(x - y)\,dt,$$
> de donde $\|G(x) - G(y)\| \leq \big(\max_x \|J_G(x)\|\big)\|x - y\|$. Si ese máximo es $< 1$, $G$ es contracción. La condición sobre $\rho(J_G(x^*))$ se obtiene porque, para alguna norma inducida, $\|J_G(x^*)\|$ se acerca arbitrariamente a $\rho(J_G(x^*))$.

> [!info]
> **Paralelo con el caso lineal.** Para la iteración lineal $y^{(k+1)} = Ty^{(k)} + c$, $J_G = T$ constante y la condición se reduce exactamente a $\rho(T) < 1$, el [[Criterio Radio Espectral Convergencia|criterio espectral]] de [[Jacobi]] y [[Gauss Seidel]]. La contracción no lineal es su extensión, con $J_G$ variable.

---

## Elección de la norma

> [!warning]
> La constante $L = \|J_G\|$ **depende de la norma** elegida. Una misma $G$ puede no ser contracción en $\|\cdot\|_\infty$ y sí serlo en $\|\cdot\|_2$ (o viceversa), porque $\rho(J_G) \leq \|J_G\|$ para *toda* norma pero la cota es más o menos ajustada según cuál. Normas inducidas útiles:
> $$\|A\|_\infty = \max_i \sum_j |a_{ij}|, \qquad \|A\|_1 = \max_j \sum_i |a_{ij}|, \qquad \|A\|_2 = \sigma_{\max}(A).$$
> Basta encontrar **una** norma en la que $\|J_G\| < 1$ para garantizar convergencia: conviene probar varias antes de descartar $G$.

---

## Ejemplo

> [!ejemplo]
> **Sistema $x = G(x)$.** Reescribir
> $$\begin{cases} x = \tfrac{1}{10}(x^2 + y + 3) \\ y = \tfrac{1}{10}(x + y^2 + 2) \end{cases} \;\Rightarrow\; G(x,y) = \frac{1}{10}\begin{pmatrix} x^2 + y + 3 \\ x + y^2 + 2 \end{pmatrix}.$$
> Cerca del punto fijo $x^* \approx (0.36, 0.25)$, la jacobiana es
> $$J_G = \frac{1}{10}\begin{pmatrix} 2x & 1 \\ 1 & 2y \end{pmatrix} \approx \begin{pmatrix} 0.072 & 0.1 \\ 0.1 & 0.05 \end{pmatrix}, \qquad \|J_G\|_\infty = \max(0.172,\,0.15) = 0.172 < 1.$$
> Como $L \approx 0.17 < 1$, $G$ es contracción. Iterando desde $(0,0)$:
>
> | $k$ | $x^{(k)}$ | $y^{(k)}$ | $\|x^{(k)} - x^{(k-1)}\|_\infty$ |
> |:---:|:---:|:---:|:---:|
> | 0 | 0.0000 | 0.0000 | — |
> | 1 | 0.3000 | 0.2000 | 0.300 |
> | 2 | 0.3290 | 0.2340 | 0.034 |
> | 3 | 0.3342 | 0.2384 | 0.0052 |
> | 4 | 0.3351 | 0.2390 | 0.0009 |
>
> El error decae con factor $\approx L = 0.17$ por iteración (lineal), como predice la cota a posteriori.

---

## Contracción frente a Newton

> [!info]
> | | Punto fijo contractivo | [[Newton Raphson Multivariable/index\|Newton]] |
> |:---|:---|:---|
> | Iteración | $x^{(k+1)} = G(x^{(k)})$ | $x^{(k+1)} = x^{(k)} - J_F^{-1}F$ |
> | Costo/iter | una evaluación de $G$, $O(n)$–$O(n^2)$ | resolver sistema lineal, $O(n^3)$ |
> | Orden | lineal (factor $L$) | [[Convergencia Local Cuadratica\|cuadrático]] |
> | Requiere | $\|J_G\| < 1$ | $J_F(r)$ no singular |
> | Diseño de $G$ | libre (varias reformulaciones posibles) | fijo |
>
> Newton **es** un caso de punto fijo con $G_N(x) = x - J_F(x)^{-1}F(x)$, para el cual $J_{G_N}(x^*) = 0$: contracción con $L = 0$ localmente, lo que explica su orden cuadrático (la cota lineal se anula y domina el término de segundo orden).

---

## Relación con otras notas

> [!info]
> - Caso escalar del que generaliza: [[Punto Fijo Aproximaciones Sucesivas/index]] y [[Teorema Punto Fijo Banach Contraccion]].
> - El criterio espectral que comparte con los métodos lineales: [[Criterio Radio Espectral Convergencia]].
> - La alternativa cuadrática: [[Newton Raphson Multivariable/index]] y [[Convergencia Local Cuadratica]].
> - Las normas matriciales inducidas usadas para acotar $L$: [[Condicionamiento Numerico Numero Condicion|número de condición y normas]].
> - Panorama del problema: [[Sistemas Ecuaciones No Lineales/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Iteración | $x^{(k+1)} = G(x^{(k)})$, $x^* = G(x^*)$ |
| Contracción | $\|G(x)-G(y)\| \leq L\|x-y\|$, $L<1$ |
| Criterio práctico | $\|J_G(x^*)\| < 1$ en alguna norma; exacto $\rho(J_G(x^*)) < 1$ |
| Orden | lineal, factor $L$ |
| Cota a posteriori | $\|x^{(k)}-x^*\| \leq \frac{L}{1-L}\|x^{(k)}-x^{(k-1)}\|$ |
| vs Newton | más barato/iter, pero solo lineal |

> [!corolario]
> La iteración de punto fijo multivariable $x^{(k+1)} = G(x^{(k)})$ converge cuando $G$ es una contracción, condición que el teorema de Banach traduce en existencia y unicidad del punto fijo más cotas de error a priori y a posteriori. El criterio operativo es $\|J_G(x^*)\| < 1$ en **alguna** norma matricial inducida —exacto en $\rho(J_G(x^*)) < 1$—, extensión directa de $|g'(r)|<1$ escalar y del $\rho(T)<1$ de los [[Criterio Radio Espectral Convergencia|métodos lineales]]. Frente a [[Newton Raphson Multivariable/index|Newton]] es más barata por paso pero solo lineal; de hecho, Newton es el punto fijo óptimo con $J_G(x^*) = 0$, lo que explica su [[Convergencia Local Cuadratica|orden cuadrático]]. Con esto se cierra el estudio de los [[Sistemas Ecuaciones No Lineales/index|sistemas de ecuaciones no lineales]].

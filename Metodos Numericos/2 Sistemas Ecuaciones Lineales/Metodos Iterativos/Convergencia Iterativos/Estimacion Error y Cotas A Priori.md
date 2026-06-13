---
title: Estimación de Error y Cotas A Priori
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - convergencia
draft: false
aliases:
  - Cotas a priori
  - Estimación de error iterativo
  - Cota a posteriori
  - A priori error bounds
---

# Estimación de Error y Cotas A Priori

> [!definicion]
> Para un método iterativo lineal $y^{(k+1)} = T y^{(k)} + c$ con [[Fundamentos de Iteración de Punto Fijo Lineal|matriz de iteración]] $T$ y solución exacta $x = A^{-1}b$, una **cota a priori** acota el error $\varepsilon^{(k)} = y^{(k)} - x$ usando solo $T$, el vector inicial y $k$ —antes de iterar—. Una **cota a posteriori** lo estima con la diferencia entre iteradas consecutivas, ya calculadas.

> [!info]
> Las cotas a priori responden *cuántas iteraciones harán falta* para una tolerancia dada; las a posteriori dan un criterio de parada *durante* la ejecución. Ambas se apoyan en la ecuación del error $\varepsilon^{(k+1)} = T\varepsilon^{(k)}$ y en el [[Criterio Radio Espectral Convergencia|radio espectral]] $\rho(T)$.

---

## Ecuación del error y cota básica

> [!teorema]
> Sea $\|\cdot\|$ una norma vectorial y su norma matricial inducida, con $\|T\| < 1$. El error de la iteración satisface $\varepsilon^{(k)} = T^k \varepsilon^{(0)}$, de donde
> $$\|\varepsilon^{(k)}\| \leq \|T\|^k\,\|\varepsilon^{(0)}\|.$$

> [!demostracion]
> Restando $x = Tx + c$ de $y^{(k+1)} = T y^{(k)} + c$:
> $$\varepsilon^{(k+1)} = y^{(k+1)} - x = T(y^{(k)} - x) = T\varepsilon^{(k)}.$$
> Por inducción $\varepsilon^{(k)} = T^k\varepsilon^{(0)}$, y por submultiplicatividad de la norma inducida
> $$\|\varepsilon^{(k)}\| = \|T^k\varepsilon^{(0)}\| \leq \|T\|^k\|\varepsilon^{(0)}\|.$$
> Como $\|T\| < 1$, $\|T\|^k \to 0$ y el método converge.

> [!info]
> La cota usa $\|T\|$ (calculable: $\|T\|_\infty$ es el máximo de sumas de filas) en lugar de $\rho(T)$ (más ajustado pero costoso). Siempre $\rho(T) \leq \|T\|$, así que $\|T\| < 1$ es suficiente pero no necesario para converger; el criterio exacto es $\rho(T) < 1$, desarrollado en [[Criterio Radio Espectral Convergencia]].

---

## Cota a priori (en función de iteradas consecutivas)

> [!teorema]
> Si $\|T\| < 1$, con $d^{(k)} = y^{(k)} - y^{(k-1)}$ se cumplen las cotas
> $$\|\varepsilon^{(k)}\| \leq \frac{\|T\|^k}{1 - \|T\|}\,\|y^{(1)} - y^{(0)}\| \qquad \text{(a priori)},$$
> $$\|\varepsilon^{(k)}\| \leq \frac{\|T\|}{1 - \|T\|}\,\|y^{(k)} - y^{(k-1)}\| \qquad \text{(a posteriori)}.$$

> [!demostracion]
> Para $m > k$, por la desigualdad triangular y $\|y^{(j+1)}-y^{(j)}\| = \|T(y^{(j)}-y^{(j-1)})\| \leq \|T\|\,\|y^{(j)}-y^{(j-1)}\|$:
> $$\|y^{(m)} - y^{(k)}\| \leq \sum_{j=k}^{m-1}\|y^{(j+1)}-y^{(j)}\| \leq \sum_{j=k}^{m-1}\|T\|^{\,j-k}\,\|y^{(k)} - y^{(k-1)}\|\cdot\|T\|.$$
> Sumando la serie geométrica y tomando $m \to \infty$ ($y^{(m)} \to x$):
> $$\|\varepsilon^{(k)}\| = \|x - y^{(k)}\| \leq \frac{\|T\|}{1-\|T\|}\,\|y^{(k)}-y^{(k-1)}\|.$$
> Iterando $\|y^{(k)}-y^{(k-1)}\| \leq \|T\|^{k-1}\|y^{(1)}-y^{(0)}\|$ se obtiene la versión a priori.

---

## Número de iteraciones para una tolerancia

> [!proposicion]
> Para garantizar $\|\varepsilon^{(k)}\| \leq \texttt{tol}$ basta tomar
> $$k \geq \frac{\log\!\big(\texttt{tol}\,(1-\|T\|)/\|y^{(1)}-y^{(0)}\|\big)}{\log\|T\|}.$$
> El número de iteraciones crece como $1/|\log\|T\||$: cuanto más cerca esté $\|T\|$ (o $\rho(T)$) de $1$, más lenta la convergencia.

> [!ejemplo]
> **Sistema $4\times4$ con [[Jacobi]].** Para
> $$A = \begin{pmatrix} 4 & -1 & 0 & 0 \\ -1 & 4 & -1 & 0 \\ 0 & -1 & 4 & -1 \\ 0 & 0 & -1 & 4 \end{pmatrix},$$
> la matriz de Jacobi $T_J = D^{-1}(E+F)$ tiene $\|T_J\|_\infty = 2/4 = 0.5$. Partiendo de $y^{(0)} = 0$ con $b = (1,1,1,1)^T$:
>
> | $k$ | $\|y^{(k)}-y^{(k-1)}\|_\infty$ | Cota a posteriori $\frac{\|T\|}{1-\|T\|}\|d^{(k)}\|$ | $\|\varepsilon^{(k)}\|_\infty$ real |
> |:---:|:---:|:---:|:---:|
> | 1 | 0.2500 | 0.2500 | 0.0464 |
> | 2 | 0.0625 | 0.0625 | 0.0089 |
> | 3 | 0.0156 | 0.0156 | 0.0018 |
> | 4 | 0.0039 | 0.0039 | 0.00036 |
>
> La cota a posteriori (calculable sin conocer $x$) acota correctamente el error real, que es bastante menor porque $\rho(T_J) \approx 0.45 < \|T_J\|_\infty = 0.5$.

---

## A priori frente a a posteriori

> [!info]
> | | A priori | A posteriori |
> |:---|:---|:---|
> | **Datos** | $\|T\|$, $y^{(0)}$, $y^{(1)}$ | iteradas $y^{(k)}, y^{(k-1)}$ |
> | **Momento** | antes de iterar | durante la iteración |
> | **Uso** | dimensionar el cómputo | criterio de parada |
> | **Ajuste** | pesimista (depende de $\|T\|$) | más fino |
>
> En la práctica se itera hasta que $\|y^{(k)}-y^{(k-1)}\|$ baja del umbral, usando la cota a posteriori como certificado; la a priori sirve para estimar de antemano el coste total.

> [!warning]
> El criterio de parada por diferencias $\|y^{(k)}-y^{(k-1)}\| < \texttt{tol}$ puede ser engañoso si $\|T\|$ está cerca de $1$: el factor $\|T\|/(1-\|T\|)$ se dispara y un avance pequeño entre iteradas **no** implica error pequeño. Conviene combinarlo con el residuo $\|b - Ay^{(k)}\|$.

---

## Relación con otras notas

> [!info]
> - El marco $y^{(k+1)} = Ty^{(k)}+c$ y la construcción de $T$ están en [[Fundamentos de Iteración de Punto Fijo Lineal]].
> - El criterio exacto de convergencia $\rho(T) < 1$ y la relación $\rho(T) \leq \|T\|$ se desarrollan en [[Criterio Radio Espectral Convergencia]].
> - La condición suficiente que garantiza $\|T\| < 1$ por inspección de $A$ es el [[Teorema Diagonal Dominante Estricta]].
> - Aplicaciones concretas a [[Jacobi]] y [[Gauss Seidel]].

---

## Resumen

| Cota | Expresión |
|:---|:---|
| Error directo | $\|\varepsilon^{(k)}\| \leq \|T\|^k\|\varepsilon^{(0)}\|$ |
| A priori | $\|\varepsilon^{(k)}\| \leq \frac{\|T\|^k}{1-\|T\|}\|y^{(1)}-y^{(0)}\|$ |
| A posteriori | $\|\varepsilon^{(k)}\| \leq \frac{\|T\|}{1-\|T\|}\|y^{(k)}-y^{(k-1)}\|$ |
| Iteraciones | $k \geq \log(\cdots)/\log\|T\|$ |

> [!corolario]
> El error de un método iterativo lineal obedece $\varepsilon^{(k)} = T^k\varepsilon^{(0)}$, lo que produce una cota geométrica $\|\varepsilon^{(k)}\| \leq \|T\|^k\|\varepsilon^{(0)}\|$ y, mediante la serie de las diferencias, cotas a priori (cuántas iteraciones hacen falta) y a posteriori (criterio de parada). Ambas dependen del factor $\|T\|/(1-\|T\|)$, que se degrada cuando $\|T\|$ —o más finamente $\rho(T)$— se acerca a $1$. Estas estimaciones convierten el [[Criterio Radio Espectral Convergencia|criterio de convergencia]] cualitativo en una herramienta cuantitativa de dimensionamiento y control de [[Jacobi]] y [[Gauss Seidel]].

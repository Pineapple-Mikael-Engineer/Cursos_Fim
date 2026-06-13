---
title: Error de Interpolación y Fórmula de Cauchy
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - error-numerico
draft: false
aliases:
  - Error de interpolación
  - Fórmula de Cauchy
  - Término de error de interpolación
  - Interpolation error
---

# Error de Interpolación y Fórmula de Cauchy

> [!definicion]
> El **error de interpolación** en un punto $x$ es la diferencia entre la función y su [[Existencia Unicidad Polinomio Interpolador|interpolador]] de grado $n$:
> $$e_n(x) = f(x) - p_n(x).$$

> [!teorema]
> **Fórmula de Cauchy del error.** Si $f \in C^{n+1}[a,b]$ y los nodos $x_0,\dots,x_n \in [a,b]$, entonces para cada $x \in [a,b]$ existe $\xi_x \in (a,b)$ tal que
> $$e_n(x) = f(x) - p_n(x) = \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\,\prod_{i=0}^n (x - x_i).$$

> [!info]
> El error se factoriza en dos partes: una **analítica** ($f^{(n+1)}/(n+1)!$, propiedad de la función) y otra **geométrica** ($\prod(x-x_i)$, el polinomio nodal, propiedad de los nodos). Minimizar el error es minimizar el polinomio nodal, lo que conduce a los [[Fenomeno Runge y Nodos Chebyshev|nodos de Chebyshev]].

---

## Demostración

> [!demostracion]
> Fíjese $x \neq x_i$. Defínase el polinomio nodal $\omega(t) = \prod_{i=0}^n (t - x_i)$ y la función auxiliar
> $$g(t) = f(t) - p_n(t) - \frac{f(x) - p_n(x)}{\omega(x)}\,\omega(t).$$
> Entonces $g$ se anula en los $n+1$ nodos $x_i$ (porque allí $f = p_n$ y $\omega = 0$) y también en $t = x$ (por construcción): tiene $n+2$ ceros distintos en $[a,b]$.
>
> Por el teorema de Rolle aplicado $n+1$ veces, $g^{(n+1)}$ tiene al menos un cero $\xi_x$. Como $p_n^{(n+1)} \equiv 0$ y $\omega^{(n+1)} \equiv (n+1)!$:
> $$0 = g^{(n+1)}(\xi_x) = f^{(n+1)}(\xi_x) - \frac{f(x) - p_n(x)}{\omega(x)}\,(n+1)!.$$
> Despejando $f(x) - p_n(x) = \dfrac{f^{(n+1)}(\xi_x)}{(n+1)!}\,\omega(x)$.

> [!info]
> **Forma con diferencias divididas.** El error también se escribe con la diferencia dividida del nodo siguiente:
> $$f(x) - p_n(x) = f[x_0, \dots, x_n, x]\,\prod_{i=0}^n (x - x_i),$$
> coherente con [[Relacion Diferencias Divididas Derivadas|$f[\cdots] = f^{(n+1)}(\xi)/(n+1)!$]]. Esto da una estimación *calculable* del error añadiendo un nodo de prueba.

---

## Cota de error

> [!corolario]
> Acotando ambos factores,
> $$|e_n(x)| \leq \frac{M_{n+1}}{(n+1)!}\,\max_{x\in[a,b]}\Big|\prod_{i=0}^n(x-x_i)\Big|, \qquad M_{n+1} = \max_{[a,b]}|f^{(n+1)}|.$$

> [!ejemplo]
> **Nodos equiespaciados en $[a,b]$ con paso $h = (b-a)/n$.** El polinomio nodal cumple $\max|\prod(x-x_i)| \leq \frac{n!}{4}h^{n+1}$, de donde
> $$|e_n(x)| \leq \frac{M_{n+1}}{4(n+1)}\,h^{n+1}.$$
>
> | Grado $n$ | Orden del error |
> |:---:|:---:|
> | 1 (lineal) | $O(h^2)$ |
> | 2 (cuadrática) | $O(h^3)$ |
> | $n$ | $O(h^{n+1})$ |
>
> A paso fijo, subir el grado mejora el orden **solo si** $M_{n+1}$ no crece más rápido que $(n+1)!$ — condición que falla en el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]].

---

## Minimización del error: nodos óptimos

> [!teoria]
> El único factor controlable es el polinomio nodal $\omega(x) = \prod(x-x_i)$. Elegir los nodos para **minimizar** $\max_{[a,b]}|\omega(x)|$ lleva a los ceros del polinomio de **Chebyshev**, que reparten el error de forma equioscilante y reducen drásticamente la cota frente a nodos equiespaciados. Es la base de [[Fenomeno Runge y Nodos Chebyshev]].

> [!warning]
> El error **no** está controlado solo por $h$: el factor $f^{(n+1)}$ puede explotar. Para funciones con derivadas de alto orden grandes (p. ej. $1/(1+25x^2)$), aumentar el grado **empeora** la interpolación equiespaciada pese a que $h^{n+1}\to 0$.

---

## Relación con otras notas

> [!info]
> - La diferencia dividida que aparece en el error: [[Relacion Diferencias Divididas Derivadas]] y [[Tabla Diferencias Divididas y Coeficientes]].
> - La minimización del polinomio nodal: [[Fenomeno Runge y Nodos Chebyshev]].
> - El error análogo en integración (vía interpolante): [[Trapecio Error Truncamiento Segunda Derivada]] y [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]].
> - Panorama: [[Newton Diferencias Divididas/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $e_n(x) = \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\prod(x-x_i)$ |
| Con dif. divididas | $f[x_0,\dots,x_n,x]\prod(x-x_i)$ |
| Cota | $\frac{M_{n+1}}{(n+1)!}\max|\omega(x)|$ |
| Orden (equiespaciado) | $O(h^{n+1})$ |
| Factor controlable | el polinomio nodal $\omega(x)$ |
| Minimización | nodos de Chebyshev |

> [!corolario]
> El error de interpolación se factoriza, por la fórmula de Cauchy, en una parte analítica $f^{(n+1)}(\xi)/(n+1)!$ y una geométrica $\prod(x-x_i)$; la demostración usa Rolle $n+1$ veces sobre una función auxiliar. Con nodos equiespaciados el orden es $O(h^{n+1})$, pero solo si $M_{n+1}$ no crece más rápido que el factorial —condición que el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]] viola—. Como único factor controlable es el polinomio nodal, minimizarlo conduce a los nodos de Chebyshev. Esta fórmula es además la base de las cotas de error de la [[Integracion Numerica Newton Cotes/index|cuadratura de Newton-Cotes]].

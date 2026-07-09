---
title: Polinomios Cardinales de Lagrange
order: 1
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - lagrange
draft: false
aliases:
  - Polinomios cardinales
  - Bases de Lagrange
  - Cardinal polynomials
  - L_i(x)
---

# Polinomios Cardinales de Lagrange $L_i(x)$

> [!definicion]
> Para nodos distintos $x_0, \dots, x_n$, el **$i$-ésimo polinomio cardinal** (o base de Lagrange) es
> $$L_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j} \in \mathbb{P}_n,$$
> caracterizado por la propiedad de **delta de Kronecker** $L_i(x_k) = \delta_{ik}$.

> [!info]
> Los $\{L_i\}_{i=0}^n$ forman una base de $\mathbb{P}_n$ adaptada a los nodos: en ella las coordenadas de cualquier polinomio son simplemente sus valores en los nodos. Por eso el [[Lagrange/index|interpolador]] es $p_n = \sum_i y_i L_i$ sin resolver sistema alguno.

---

## Propiedades

> [!proposicion]
> 1. **Grado:** $L_i \in \mathbb{P}_n$ (producto de $n$ factores lineales).
> 2. **Delta de Kronecker:** $L_i(x_k) = \delta_{ik}$.
> 3. **Partición de la unidad:** $\sum_{i=0}^n L_i(x) \equiv 1$ para todo $x$.
> 4. **Reproducción de polinomios:** $\sum_{i=0}^n x_i^m L_i(x) = x^m$ para $0 \leq m \leq n$.

> [!demostracion]
> **Propiedad 2.** En $x = x_k$ con $k \neq i$, el factor $(x - x_k)$ del producto se anula, luego $L_i(x_k) = 0$. En $x = x_i$, cada factor es $(x_i - x_j)/(x_i - x_j) = 1$, luego $L_i(x_i) = 1$.
>
> **Propiedad 3.** La función constante $g(x) = 1$ pertenece a $\mathbb{P}_n$ y toma el valor $1$ en todos los nodos. Por [[Existencia Unicidad Polinomio Interpolador|unicidad]], su interpolador es ella misma: $\sum_i 1\cdot L_i(x) = 1$.

---

## Ejemplo

> [!ejemplo]
> **Cardinales para nodos $x_0=0, x_1=1, x_2=2$.**
> $$L_0(x) = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{x^2-3x+2}{2}, \quad L_1(x) = \frac{x(x-2)}{(1)(-1)} = -x^2+2x, \quad L_2(x) = \frac{x(x-1)}{2}.$$
>
> | $x$ | $L_0$ | $L_1$ | $L_2$ | $\sum L_i$ |
> |:---:|:---:|:---:|:---:|:---:|
> | 0 | 1 | 0 | 0 | 1 |
> | 1 | 0 | 1 | 0 | 1 |
> | 2 | 0 | 0 | 1 | 1 |
> | 0.5 | 0.375 | 0.75 | $-0.125$ | 1 |
>
> Se verifican la delta de Kronecker (filas $0,1,2$) y la partición de la unidad (última columna). Nótese que un cardinal puede ser **negativo** entre nodos: origen de la inestabilidad de grado alto.

---

## Construcción del interpolador

> [!teorema]
> Dado $y_i = f(x_i)$, el polinomio
> $$p_n(x) = \sum_{i=0}^n y_i\, L_i(x)$$
> es el único interpolador de grado $\leq n$. La aplicación $f \mapsto p_n$ es lineal y los $L_i$ son su "núcleo": $p_n(x) = \sum_i f(x_i)L_i(x)$ es la versión interpolatoria de una fórmula de cuadratura.

> [!info] **Función de Lebesgue.**
>  La sensibilidad de la interpolación a errores en los datos la mide la **constante de Lebesgue** $\Lambda_n = \max_x \sum_i |L_i(x)|$: un error $\varepsilon$ en los $y_i$ produce error $\leq \Lambda_n\varepsilon$ en $p_n$. Con nodos equiespaciados $\Lambda_n$ crece exponencialmente (ligado al [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]); con nodos de Chebyshev crece solo como $\log n$.

---

## Conexión con cuadratura e integración

> [!teoria]
> Integrando $p_n = \sum_i f(x_i)L_i$ se obtienen las fórmulas de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]]:
> $$\int_a^b f(x)\,dx \approx \sum_{i=0}^n w_i\, f(x_i), \qquad w_i = \int_a^b L_i(x)\,dx.$$
> Los pesos de cuadratura son las integrales de los polinomios cardinales. Esta es la razón de que Lagrange sea la base teórica preferida.

---

## Relación con otras notas

> [!info]
> - El uso en el interpolador y la forma baricéntrica eficiente: [[Lagrange/index]] y [[Costo Computacional Evaluacion Directa]].
> - La unicidad que sustenta la partición de la unidad: [[Existencia Unicidad Polinomio Interpolador]].
> - La constante de Lebesgue y la oscilación: [[Fenomeno Runge y Nodos Chebyshev]].
> - Su integración da los pesos de cuadratura: [[Integracion Numerica Newton Cotes/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Definición | $L_i(x) = \prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ |
| Grado | $n$ |
| Delta de Kronecker | $L_i(x_k) = \delta_{ik}$ |
| Partición de la unidad | $\sum_i L_i \equiv 1$ |
| Interpolador | $p_n = \sum_i y_i L_i$ |
| Sensibilidad | constante de Lebesgue $\Lambda_n$ |

> [!corolario]
> Los polinomios cardinales $L_i(x) = \prod_{j\neq i}(x-x_j)/(x_i-x_j)$ forman la base de Lagrange adaptada a los nodos: valen $\delta_{ik}$ en ellos y suman la unidad, de modo que el interpolador es directamente $\sum_i y_i L_i$ sin resolver sistemas. Su signo cambiante entre nodos y el crecimiento de la constante de Lebesgue con nodos equiespaciados anuncian la inestabilidad del [[Fenomeno Runge y Nodos Chebyshev|grado alto]]. Integrados, producen los pesos de las fórmulas de [[Integracion Numerica Newton Cotes/index|cuadratura de Newton-Cotes]]; su [[Costo Computacional Evaluacion Directa|evaluación eficiente]] se logra con la forma baricéntrica.

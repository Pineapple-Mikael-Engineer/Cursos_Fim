---
title: Punto Fijo Aproximaciones Sucesivas
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-abiertos
  - punto-fijo
  - index
draft: false
aliases:
  - Fixed point iteration
  - Iteración de punto fijo
  - Aproximaciones sucesivas
---

# Método de Punto Fijo (Aproximaciones Sucesivas)

> [!definicion]
> El **método de punto fijo** (o de aproximaciones sucesivas) transforma la ecuación $f(x)=0$ en una ecuación equivalente $x = g(x)$. La iteración se define como:
> $$x^{(k+1)} = g(x^{(k)})$$
> partiendo de una aproximación inicial $x^{(0)}$. Si la sucesión $\{x^{(k)}\}$ converge, su límite $r$ satisface $r = g(r)$, es decir, $r$ es un **punto fijo** de $g$.

> [!info]
> A diferencia de los [[Metodos Cerrados Una Variable|métodos cerrados]] (bisección, regula falsi), el método de punto fijo no requiere un intervalo que contenga la raíz, pero su convergencia no está garantizada. La elección de $g$ es fundamental.

---

## Ejemplo

> [!ejemplo]
> **Resolver $f(x) = x^2 - x - 1 = 0$ (raíz áurea $\phi \approx 1.618$) mediante punto fijo.**
>
> La ecuación puede reescribirse como $x = g(x)$ de varias formas:
>
> | Forma | $g(x)$ | Convergencia |
> |:---|:---|:---|
> | 1 | $x = x^2 - 1$ | Divergente |
> | 2 | $x = \sqrt{x + 1}$ | Convergente (lenta) |
> | 3 | $x = 1 + \frac{1}{x}$ | Convergente (rápida) |
>
> **Iteración con $g(x) = 1 + 1/x$, $x^{(0)} = 1.5$:**
>
> | $k$ | $x^{(k)}$ | $g(x^{(k)})$ |
> |:---|:---|:---|
> | 0 | 1.5000 | 1.6667 |
> | 1 | 1.6667 | 1.6000 |
> | 2 | 1.6000 | 1.6250 |
> | 3 | 1.6250 | 1.6154 |
> | 4 | 1.6154 | 1.6190 |
> | 5 | 1.6190 | 1.6176 |
> | 6 | 1.6176 | 1.6182 |
> | 7 | 1.6182 | 1.6180 |
>
> La sucesión converge a $\phi \approx 1.618$.

---

## En qué consiste el método

> [!teoria]
> **Algoritmo de punto fijo.**
>
> Dada una función $g$ continua y una aproximación inicial $x^{(0)}$:
>
> 1. Calcular $x^{(1)} = g(x^{(0)})$
> 2. Si $|x^{(1)} - x^{(0)}| < \text{tol}$, parar
> 3. Actualizar $x^{(0)} = x^{(1)}$ y repetir
>
> **Relación con $f(x)=0$:**
>
> Para aplicar el método, se debe reescribir $f(x)=0$ como $x = g(x)$. Hay infinitas maneras de hacerlo:
> - $g(x) = x - f(x)$
> - $g(x) = x + c f(x)$ con $c \neq 0$
> - $g(x) = \sqrt{x+1}$ (del ejemplo)
> - $g(x) = 1 + 1/x$ (del ejemplo)
>
> La elección de $g$ determina si el método converge y qué tan rápido.

---

## Teorema de punto fijo de Banach (contracción)

> [!info]
> El teorema fundamental que garantiza existencia, unicidad y convergencia del punto fijo bajo condiciones de contracción.
>
> Desarrollado en [[Teorema Punto Fijo Banach Contraccion]]

---

## Construcción de la función de iteración

> [!info]
> Estrategias para construir $g$ a partir de $f$ y análisis de la convergencia local ($|g'(r)| < 1$).
>
> Desarrollado en [[Funcion Iteracion g x y Convergencia Local]]

---

## Orden de convergencia lineal

> [!info]
> El método de punto fijo tiene convergencia lineal con constante asintótica $|g'(r)|$, donde $r$ es la raíz.
>
> Desarrollado en [[Orden Convergencia Lineal Constante Asintotica]]

---

## Relación con otros métodos

> [!info]
> **Conexiones importantes:**
>
> - El [[Newton Raphson/index]] es un caso particular de punto fijo con $g(x) = x - f(x)/f'(x)$, que logra convergencia cuadrática porque $g'(r)=0$.
>
> - El [[Metodo Secante Orden Convergencia Fi]] también puede verse como una aproximación a punto fijo sin usar derivadas.
>
> - Los métodos cerrados ([[Biseccion]], [[Regula Falsi]]) pueden interpretarse como esquemas de punto fijo aplicados a funciones de intervalo.

---

## Limitaciones

> [!warning]
> **Limitaciones del método de punto fijo.**
>
> 1. **Convergencia no garantizada:** Depende críticamente de la elección de $g$.
> 2. **Requiere $|g'(r)| < 1$:** Si $|g'(r)| \geq 1$, el método diverge.
> 3. **Convergencia lenta:** Si $|g'(r)|$ es cercano a $1$, se necesitan muchas iteraciones.
> 4. **Elección de $g$:** No hay una regla única para construir $g$ a partir de $f$.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Tipo** | Método abierto (no requiere intervalo) |
| **Iteración** | $x^{(k+1)} = g(x^{(k)})$ |
| **Convergencia** | Garantizada si $g$ es contracción |
| **Orden de convergencia** | Lineal ($p=1$) |
| **Constante asintótica** | $\|g'(r) \|$ |
| **Ventaja** | Simple, unifica muchos métodos |
| **Desventaja** | Convergencia lenta, crítica elección de $g$ |

> [!corolario]
> El método de punto fijo es el marco teórico unificador de los métodos iterativos para ecuaciones no lineales. Su convergencia está determinada por la condición de contracción $|g'(r)| < 1$. El teorema de punto fijo de Banach proporciona condiciones suficientes para convergencia global. La velocidad de convergencia es lineal con constante $|g'(r)|$, y métodos como [[Newton Raphson/index]] logran aceleración cuadrática haciendo $g'(r) = 0$.